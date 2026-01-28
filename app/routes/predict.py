"""
KLTN_UIT_BE Prediction Route
API endpoint for transaction classification
"""
import logging
from typing import List
from fastapi import APIRouter, HTTPException
from app.config import get_settings
from app.prompts.system_prompts import build_prompts
from app.schemas.request_response import (
    PredictRequest,
    PredictionResponse,
    ErrorResponse,
    HealthCheckResponse
)
from app.services.llm_service import (
    get_llm_service,
    LLMServiceError
)
from app.services.preprocessing import normalize_text
from app.services.postprocessing import (
    process_llm_response,
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
        version="1.0.0"
    )
@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictRequest) -> PredictionResponse:
    """
    Predict transaction category from Vietnamese text
    
    Args:
        request: PredictRequest with text and categories
    
    Returns:
        PredictionResponse with amount, category, type, and confidence
    
    Raises:
        HTTPException: If prediction fails
    """
    settings = get_settings()
    llm_service = get_llm_service()
    
    # Get valid categories (use request categories or defaults)
    valid_categories = request.categories if request.categories else settings.app.default_categories
    valid_types = settings.app.transaction_types
    
    try:
        # Preprocess text
        normalized_text = normalize_text(request.text)
        logger.info(f"Processing transaction: '{normalized_text}'")
        
        # Build prompts
        system_prompt, user_prompt = build_prompts(normalized_text, valid_categories)
        
        # Get LLM prediction
        raw_output = llm_service.get_prediction(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.0  # Deterministic output
        )
        logger.debug(f"Raw LLM output: {raw_output}")
        
        # Postprocess response
        prediction = process_llm_response(
            raw_output=raw_output,
            valid_categories=valid_categories,
            valid_types=valid_types,
            fix_invalid=True
        )
        
        logger.info(f"Prediction result: {prediction}")
        
        # Return response
        return PredictionResponse(
            amount=prediction.get("amount", 0),
            category=prediction.get("category", "Khác"),
            type=prediction.get("type", "Chi phí"),
            confidence=prediction.get("confidence", 0.5),
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
        logger.error(f"Unexpected error: {e}")
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
        categories: Optional list of valid categories
    
    Returns:
        List of PredictionResponse
    """
    settings = get_settings()
    valid_categories = categories if categories else settings.app.default_categories
    
    responses = []
    for text in texts:
        try:
            # Create request manually
            request = PredictRequest(text=text, categories=valid_categories)
            response = await predict(request)
            responses.append(response)
        except HTTPException as e:
            # Add error response for failed predictions
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
    Get available categories
    
    Returns:
        Dictionary with default categories and transaction types
    """
    settings = get_settings()
    return {
        "categories": settings.app.default_categories,
        "transaction_types": settings.app.transaction_types
    }
