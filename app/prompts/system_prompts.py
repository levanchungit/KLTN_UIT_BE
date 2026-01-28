"""
KLTN_UIT_BE System Prompts
Prompt templates for JSON-based transaction classification
"""
from typing import List
# =====================
# System Prompt
# =====================
SYSTEM_PROMPT = """Bạn là một trợ lý AI chuyên phân loại giao dịch tài chính cá nhân.
Nhiệm vụ của bạn là phân tích câu mô tả giao dịch tiếng Việt và trích xuất thông tin dưới dạng JSON.

## Quy tắc phân loại:

### 1. Xác định loại giao dịch (type):
- "Thu nhập": Tiền vào, nhận tiền (lương, quà tặng, hoàn tiền, bán đồ, vay tiền)
- "Chi tiêu": Tiền ra, chi tiêu (mua đồ, ăn uống, di chuyển, hóa đơn)
- "Chuyển khoản": Chuyển tiền giữa tài khoản, ví điện tử

### 2. Trích xuất số tiền (amount):
- Quy đổi về đơn vị VND
- "1tr" = 1000000
- "200k" = 200000
- "500k" = 500000
- "10k" = 10000
- Nếu không tìm thấy số tiền, trả về 0

### 3. Chọn danh mục (category):
- CHỈ được chọn từ danh sách categories được cung cấp
- Nếu không phù hợp với bất kỳ danh mục nào, chọn "Khác"

## Yêu cầu output:
- LUÔN trả về JSON hợp lệ
- KHÔNG có thêm text hay giải thích
- KHÔNG sử dụng markdown code block
- Dùng tiếng Việt cho category
- Confidence score từ 0 đến 1

## Output Format:
```json
{
  "amount": <số tiền>,
  "category": "<danh mục từ list>",
  "type": "<Thu nhập|Chi tiêu|Chuyển khoản>",
  "confidence": <độ tin cậy 0-1>
}
```
"""
# =====================
# User Prompt Template
# =====================
def build_user_prompt(transaction_text: str, categories: List[str]) -> str:
    """
    Build the user prompt for transaction classification
    
    Args:
        transaction_text: The Vietnamese transaction description
        categories: List of valid categories
    
    Returns:
        Formatted user prompt
    """
    categories_str = "\n".join(f"- {cat}" for cat in categories)
    
    return f"""Phân loại giao dịch sau:

Câu mô tả: "{transaction_text}"

Danh mục hợp lệ:
{categories_str}

Trích xuất và phân loại thông tin giao dịch, trả về JSON:"""
# =====================
# Fallback Prompt (simpler)
# =====================
FALLBACK_PROMPT = """Phân tích câu giao dịch sau và trả về JSON:

Câu: "{text}"

Output JSON với các trường: amount, category, type, confidence

Chỉ trả về JSON, không giải thích."""
# =====================
# Prompt Utilities
# =====================
def get_system_prompt() -> str:
    """Get the system prompt for transaction classification"""
    return SYSTEM_PROMPT
def build_prompts(transaction_text: str, categories: List[str]) -> tuple:
    """
    Build both system and user prompts
    
    Args:
        transaction_text: The Vietnamese transaction description
        categories: List of valid categories
    
    Returns:
        Tuple of (system_prompt, user_prompt)
    """
    return (
        get_system_prompt(),
        build_user_prompt(transaction_text, categories)
    )
