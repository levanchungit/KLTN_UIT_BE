"""
Receipt OCR Analysis Route — AI-powered receipt total extraction using LLM.
Replaces rule-based regex strategies with LLM reasoning.
"""
import json
import logging
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

from app.services.llm_service import get_llm_service, LLMServiceError
from app.prompts.receipt_prompts import RECEIPT_SYSTEM_PROMPT, RECEIPT_USER_PROMPT_TEMPLATE

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1", tags=["receipt"])


# ── Request / Response schemas ──

class OCRBlock(BaseModel):
    """Individual text block from ML Kit OCR with position info"""
    text: str
    top: Optional[float] = None
    left: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None

class ReceiptRequest(BaseModel):
    """Request for receipt analysis"""
    ocr_text: str = Field(..., min_length=3, max_length=5000,
                          description="Full OCR text from ML Kit Text Recognition")
    blocks: Optional[List[OCRBlock]] = Field(
        default=None,
        description="Optional text blocks with position info for better accuracy"
    )
    user_categories: Optional[List[str]] = Field(
        default=None,
        description="Optional list of user-defined categories for better classification"
    )

class ReceiptResponse(BaseModel):
    """Response from receipt analysis"""
    total_amount: int = Field(..., description="Tổng tiền cuối cùng (VND)")
    merchant_name: str = Field(default="Hoá đơn", description="Tên cửa hàng")
    category: str = Field(default="Chưa xác định", description="Danh mục chi tiêu")
    items_count: Optional[int] = Field(
        default=None,
        description="Number of items found in receipt"
    )
    confidence: float = Field(
        default=0.0,
        description="Confidence score (0.0-1.0)"
    )
    raw_ocr_text: Optional[str] = Field(
        default=None,
        description="Original OCR text (for debugging)"
    )
    message: Optional[str] = Field(
        default=None,
        description="Friendly conversational message from AI"
    )


# ── Endpoint ──

@router.post("/predict-receipt", response_model=ReceiptResponse)
async def predict_receipt(request: ReceiptRequest):
    """
    Analyze receipt OCR text using LLM to extract total amount.
    
    The LLM understands receipt structure and can distinguish:
    - Total vs subtotal vs tax vs discount
    - Phone numbers vs amounts
    - Tax IDs vs amounts
    """
    llm_service = get_llm_service()

    if not llm_service.is_available():
        raise HTTPException(status_code=503, detail="LLM server không khả dụng")

    # Build OCR text — if blocks provided, format with position context
    ocr_text = request.ocr_text.strip()
    if request.blocks:
        # Sort blocks top-to-bottom, add position hints for LLM
        sorted_blocks = sorted(request.blocks, key=lambda b: b.top or 0)
        lines = []
        for b in sorted_blocks:
            pos_hint = f"[y={int(b.top or 0)}]" if b.top is not None else ""
            lines.append(f"{pos_hint} {b.text}")
        ocr_text = "\n".join(lines)

    # Truncate if too long (LLM context limit) - Optimized to 2000 for speed
    if len(ocr_text) > 2000:
        ocr_text = ocr_text[:2000]

    # Build category context
    categories_context = ""
    if request.user_categories and len(request.user_categories) > 0:
        cat_list = ", ".join([f'"{c}"' for c in request.user_categories])
        categories_context = f"## DANH SÁCH DANH MỤC KHẢ DỤNG (BẮT BUỘC CHỌN 1):\n{cat_list}\n\nNếu không khớp, chọn danh mục có ý nghĩa gần nhất hoặc 'Chưa xác định'."
    else:
        categories_context = "## DANH MỤC GỢI Ý:\nĂn uống, Đi lại, Nhà ở, Mua sắm, Giải trí, Giáo dục, Y tế, Chưa xác định"

    user_prompt = RECEIPT_USER_PROMPT_TEMPLATE.format(
        ocr_text=ocr_text,
        categories_context=categories_context
    )

    try:
        raw_response = llm_service.get_prediction(
            system_prompt=RECEIPT_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            temperature=0.1,    # Low temp for accuracy
            max_tokens=150,     # Optimized for speed (receipt JSON is short)
            json_mode=True      # Force JSON output
        )

        logger.debug(f"Receipt LLM raw response: {raw_response}")

        # Parse JSON response
        parsed = json.loads(raw_response)

        total_amount = int(parsed.get("total_amount", 0))
        if total_amount <= 0:
            raise HTTPException(
                status_code=422,
                detail="Không thể xác định tổng tiền từ hoá đơn"
            )

        return ReceiptResponse(
            total_amount=total_amount,
            merchant_name=parsed.get("merchant_name", "Hoá đơn"),
            category=parsed.get("category", "Chưa xác định"),
            items_count=parsed.get("items_count"),
            confidence=float(parsed.get("confidence", 0.8)),
            raw_ocr_text=request.ocr_text[:500] if logger.isEnabledFor(logging.DEBUG) else None,
            message=parsed.get("message")
        )

    except json.JSONDecodeError as e:
        logger.error(f"Receipt LLM JSON parse error: {e}, raw: {raw_response[:200]}")
        raise HTTPException(status_code=422, detail="LLM trả về format không hợp lệ")
    except LLMServiceError as e:
        logger.error(f"Receipt LLM error: {e}")
        raise HTTPException(status_code=503, detail=f"LLM lỗi: {e}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Receipt analysis error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Lỗi phân tích hoá đơn: {e}")
