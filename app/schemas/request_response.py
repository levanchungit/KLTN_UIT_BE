"""
KLTN_UIT_BE Pydantic Schemas
Request and Response models for the transaction classification API
Supports both single and multi-transaction parsing
"""
from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator


# =====================
# Request Models
# =====================
class PredictRequest(BaseModel):
    """
    Request model for transaction prediction endpoint
    
    Attributes:
        text: The transaction description in Vietnamese
        categories: List of valid categories for the user/app
        locale: Optional locale specification (default: vi-VN)
        currency: Optional currency code (default: VND)
    """
    text: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Mô tả giao dịch bằng tiếng Việt (có thể chứa nhiều giao dịch)",
        examples=["Mẹ cho 1tr", "Kem 50k sữa chua 42k trà đào 50k"]
    )
    categories: List[str] = Field(
        default_factory=list,
        description="Danh sách danh mục hợp lệ để AI chọn (rỗng = open-domain)",
        examples=[["Quà tặng", "Lương", "Ăn uống", "Mượn tiền"]]
    )
    locale: Optional[str] = Field(
        default="vi-VN",
        description="Ngôn ngữ và khu vực (ví dụ: vi-VN)"
    )
    currency: Optional[str] = Field(
        default="VND",
        description="Mã tiền tệ (ví dụ: VND, USD)"
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, v: str) -> str:
        """Strip whitespace and validate text"""
        v = v.strip()
        if not v:
            raise ValueError("Text không được để trống")
        return v

    @field_validator("categories")
    @classmethod
    def validate_categories(cls, v: List[str]) -> List[str]:
        """Ensure categories list is valid"""
        if not v:
            return []  # Empty list is OK, will use defaults
        # Remove duplicates while preserving order
        seen = set()
        unique_categories = []
        for cat in v:
            cat = cat.strip()
            if cat and cat not in seen:
                seen.add(cat)
                unique_categories.append(cat)
        return unique_categories


class HealthCheckResponse(BaseModel):
    """Response model for health check endpoint"""
    status: str = Field(..., description="Trạng thái service")
    llm_available: bool = Field(..., description="LLM server có khả dụng không")
    version: str = Field(..., description="Phiên bản API")


# =====================
# Transaction Item (for multi-transaction)
# =====================
class TransactionItem(BaseModel):
    """
    Single transaction item in multi-transaction response
    """
    item: str = Field(
        ...,
        description="Tên/mô tả ngắn của giao dịch",
        examples=["Kem", "Sữa chua", "Trà đào"]
    )
    amount: int = Field(
        ...,
        description="Số tiền giao dịch (VND)",
        examples=[50000]
    )
    category: str = Field(
        ...,
        description="Danh mục giao dịch",
        examples=["Ăn uống"]
    )
    type: str = Field(
        ...,
        description="Loại giao dịch (Thu nhập/Chi phí)",
        examples=["Chi phí"]
    )
    confidence: float = Field(
        default=0.9,
        ge=0.0,
        le=1.0,
        description="Độ tin cậy của dự đoán (0-1)"
    )


# =====================
# Response Models
# =====================
class PredictionResponse(BaseModel):
    """
    Response model for transaction prediction
    Supports both single transaction and multi-transaction
    
    Attributes:
        amount: Total transaction amount in VND
        category: Predicted category (for single transaction)
        type: Transaction type (Thu nhập/Chi phí)
        confidence: Confidence score between 0 and 1
        transactions: List of individual transactions (for multi-transaction)
        raw_output: Raw LLM output (for debugging)
    """
    amount: int = Field(
        ...,
        description="Tổng số tiền giao dịch (VND)",
        examples=[142000]
    )
    category: str = Field(
        ...,
        description="Danh mục giao dịch chính",
        examples=["Ăn uống"]
    )
    type: str = Field(
        ...,
        description="Loại giao dịch (Thu nhập/Chi phí)",
        examples=["Chi phí"]
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Độ tin cậy của dự đoán (0-1)",
        examples=[0.88]
    )
    transactions: Optional[List[TransactionItem]] = Field(
        default=None,
        description="Danh sách các giao dịch chi tiết (nếu có nhiều giao dịch trong câu)"
    )
    raw_output: Optional[str] = Field(
        default=None,
        description="Raw LLM output for debugging"
    )

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "amount": 142000,
                "category": "Ăn uống",
                "type": "Chi phí",
                "confidence": 0.95,
                "transactions": [
                    {"item": "Kem", "amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95},
                    {"item": "Sữa chua", "amount": 42000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95},
                    {"item": "Trà đào", "amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}
                ]
            }
        }


class ErrorResponse(BaseModel):
    """Response model for errors"""
    error: str = Field(..., description="Loại lỗi")
    message: str = Field(..., description="Thông báo lỗi chi tiết")
    details: Optional[dict] = Field(default=None, description="Chi tiết bổ sung")
    raw_output: Optional[str] = Field(default=None, description="Raw LLM output nếu có")


# =====================
# Model Aliases (for easier imports)
# =====================
__all__ = [
    "PredictRequest",
    "PredictionResponse",
    "TransactionItem",
    "HealthCheckResponse",
    "ErrorResponse"
]
