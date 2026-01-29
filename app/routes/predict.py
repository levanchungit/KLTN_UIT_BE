"""
KLTN_UIT_BE Prediction Route
API endpoint for transaction classification
Supports Open-domain, Closed-domain, and Multi-transaction parsing
"""
import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from app.config import get_settings
from app.prompts.system_prompts import (
    MULTI_TRANSACTION_SYSTEM_PROMPT,
    build_multi_transaction_closed_domain_prompt,
    build_multi_transaction_user_prompt,
    get_cache_info as get_prompt_cache_info
)
from app.schemas.request_response import (
    PredictRequest,
    PredictionResponse,
    TransactionItem,
    ErrorResponse,
    HealthCheckResponse
)
from app.services.llm_service import (
    get_llm_service,
    LLMServiceError
)
from app.services.preprocessing import (
    normalize_text,
    preprocess_transaction,
    extract_keywords,
    detect_transaction_type
)
from app.services.postprocessing import (
    process_multi_transaction_response,
    PostprocessingError
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1", tags=["prediction"])


@router.get("/health")
async def health_check() -> HealthCheckResponse:
    """
    Health check endpoint
    
    Returns:
        Health status and LLM availability
    """
    llm_service = get_llm_service()
    llm_available = llm_service.is_available()
    
    return HealthCheckResponse(
        status="healthy" if llm_available else "degraded",
        llm_available=llm_available,
        version="3.0.0"  # Updated for multi-transaction support
    )


@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictRequest) -> PredictionResponse:
    """
    Predict transaction category from Vietnamese text
    
    Supports:
    - Open-domain: When categories is empty, AI determines the category
    - Closed-domain: When categories is provided, AI classifies into given list
    - Multi-transaction: Automatically detects and splits multiple transactions
    
    Args:
        request: PredictRequest with text and optional categories
    
    Returns:
        PredictionResponse with amount, category, type, confidence, and transactions
    
    Raises:
        HTTPException: If prediction fails
    """
    settings = get_settings()
    llm_service = get_llm_service()
    valid_types = settings.app.transaction_types
    
    # Determine classification mode
    is_open_domain = not request.categories or len(request.categories) == 0
    valid_categories = None if is_open_domain else request.categories
    
    try:
        # Preprocess text - extract hints
        normalized_text, detected_type, detected_amount = preprocess_transaction(request.text)
        keywords = extract_keywords(request.text)
        
        logger.info(f"Processing: '{normalized_text}' | Mode: {'Open-domain' if is_open_domain else 'Closed-domain'}")
        logger.debug(f"Preprocessing hints - Type: {detected_type}, Amount: {detected_amount}")
        
        if is_open_domain:
            # ========================
            # OPEN-DOMAIN MODE
            # AI tự xác định category, hỗ trợ multi-transaction
            # ========================
            system_prompt = MULTI_TRANSACTION_SYSTEM_PROMPT
            user_prompt = build_multi_transaction_user_prompt(normalized_text)
            
        else:
            # ========================
            # CLOSED-DOMAIN MODE
            # Phân loại vào danh sách cho trước, hỗ trợ multi-transaction
            # ========================
            # Ensure "Khác" is in the list for fallback
            if "Khác" not in valid_categories:
                valid_categories = valid_categories + ["Khác"]
            
            # Convert to tuple for prompt caching
            cat_tuple = tuple(valid_categories)
            system_prompt = build_multi_transaction_closed_domain_prompt(cat_tuple)
            user_prompt = build_multi_transaction_user_prompt(normalized_text, valid_categories)
        
        # Get LLM prediction
        raw_output = llm_service.get_prediction(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.0
        )
        logger.debug(f"Raw LLM output: {raw_output}")
        
        # Process response (handles both single and multi-transaction)
        prediction = process_multi_transaction_response(
            raw_output=raw_output,
            valid_categories=valid_categories,
            valid_types=valid_types
        )
        
        # Use preprocessing hints as fallback when confidence is low
        if prediction.get("confidence", 0) < 0.5:
            logger.info("Low confidence, using preprocessing hints as fallback")
            if detected_type and not prediction.get("type"):
                prediction["type"] = detected_type
            if detected_amount and prediction.get("amount", 0) == 0:
                prediction["amount"] = detected_amount
        
        # Ensure type is valid
        if prediction.get("type") not in valid_types:
            if detected_type and detected_type in valid_types:
                prediction["type"] = detected_type
            else:
                prediction["type"] = "Chi phí"  # Default
        
        logger.info(f"Prediction result: amount={prediction.get('amount')}, category={prediction.get('category')}, transactions={len(prediction.get('transactions', []) or [])}")
        
        # Build transactions list for response
        transactions = None
        if prediction.get("transactions"):
            transactions = [
                TransactionItem(
                    item=tx.get("item", ""),
                    amount=tx.get("amount", 0),
                    category=tx.get("category", "Khác"),
                    type=tx.get("type", "Chi phí"),
                    confidence=tx.get("confidence", 0.9)
                )
                for tx in prediction["transactions"]
            ]
        
        # Return response
        return PredictionResponse(
            amount=prediction.get("amount", 0),
            category=prediction.get("category", "Khác"),
            type=prediction.get("type", "Chi phí"),
            confidence=prediction.get("confidence", 0.5),
            transactions=transactions,
            raw_output=raw_output if settings.server.debug else None
        )
        
    except LLMServiceError as e:
        logger.error(f"LLM service error: {e}")
        raise HTTPException(
            status_code=503,
            detail=ErrorResponse(
                error="LLM_SERVICE_ERROR",
                message=str(e),
                details={"llm_base_url": settings.llm.base_url}
            ).model_dump()
        )
        
    except PostprocessingError as e:
        logger.error(f"Postprocessing error: {e}")
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                error="POSTPROCESSING_ERROR",
                message=str(e)
            ).model_dump()
        )
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                error="INTERNAL_ERROR",
                message="An unexpected error occurred"
            ).model_dump()
        )


@router.post("/predict/batch")
async def predict_batch(
    texts: List[str],
    categories: List[str] = None
) -> List[PredictionResponse]:
    """
    Batch predict transaction categories
    
    Args:
        texts: List of transaction texts
        categories: Optional list of valid categories (None for open-domain)
    
    Returns:
        List of PredictionResponse
    """
    responses = []
    for text in texts:
        try:
            request = PredictRequest(
                text=text, 
                categories=categories if categories else []
            )
            response = await predict(request)
            responses.append(response)
        except HTTPException as e:
            responses.append(PredictionResponse(
                amount=0,
                category="Khác",
                type="Chi phí",
                confidence=0.0,
                raw_output=f"Error: {e.detail}"
            ))
    
    return responses


@router.get("/categories")
async def get_categories() -> dict:
    """
    Get available default categories
    
    Returns:
        Dictionary with default categories and transaction types
    """
    settings = get_settings()
    return {
        "categories": settings.app.default_categories,
        "transaction_types": settings.app.transaction_types,
        "note": "These are default categories. In open-domain mode (empty categories), AI will determine the category automatically."
    }


@router.get("/cache/stats")
async def get_cache_stats() -> dict:
    """
    Get cache statistics for monitoring performance
    
    Returns:
        Dictionary with prompt and response cache stats
    """
    llm_service = get_llm_service()
    return {
        "prompt_cache": {
            "closed_domain": str(get_prompt_cache_info()["closed_domain"]),
            "multi_transaction": str(get_prompt_cache_info()["multi_transaction"])
        },
        "response_cache": llm_service.get_cache_stats()
    }


@router.get("/categories/suggested")
async def get_suggested_categories() -> dict:
    """
    Get list of commonly suggested categories for open-domain mode
    
    Returns:
        Dictionary with suggested categories organized by type
    """
    return {
        "income_categories": [
            "Lương",
            "Quà tặng", 
            "Thu nhập khác",
            "Hoàn tiền",
            "Bán đồ"
        ],
        "expense_categories": [
            "Ăn uống",
            "Di chuyển",
            "Mua sắm",
            "Giải trí",
            "Hóa đơn",
            "Sức khỏe",
            "Giáo dục",
            "Mỹ phẩm",
            "Viễn thông",
            "Đám tiệc",
            "Làm đẹp",
            "Cho vay",
            "Trả nợ",
            "Sửa chữa",
            "Khác"
        ],
        "note": "In open-domain mode, AI may return these or other relevant categories based on the transaction description."
    }
