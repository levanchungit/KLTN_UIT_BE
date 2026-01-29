"""
KLTN_UIT_BE System Prompts - Optimized for Speed
Compact prompts for fast LLM inference while maintaining accuracy
"""
from typing import List
from functools import lru_cache

# =====================
# OPTIMIZED OPEN-DOMAIN System Prompt - Compact version
# =====================
OPEN_DOMAIN_SYSTEM_PROMPT = """Bạn là AI phân loại giao dịch tài chính Việt Nam.

RULES:
1. type: "Thu nhập" (tiền vào: lương, quà, được cho) | "Chi phí" (tiền ra: mua, trả)
2. amount: "1tr"=1000000, "500k"=500000, "50k"=50000
3. category: Xác định ngắn gọn (Ăn uống, Di chuyển, Lương, Quà tặng, Mua sắm, Giải trí, Sức khỏe, Làm đẹp, Khác...)
4. confidence: 0.0-1.0

OUTPUT: Chỉ JSON, không text thêm.
{"amount": <số>, "category": "<tên>", "type": "<loại>", "confidence": <0-1>}"""

# =====================
# OPTIMIZED CLOSED-DOMAIN System Prompt Builder
# =====================
@lru_cache(maxsize=64)
def build_closed_domain_system_prompt(categories: tuple) -> str:
    """Build compact system prompt for closed-domain classification (cached)"""
    categories_list = ", ".join(f'"{cat}"' for cat in categories)
    fallback = "Khác" if "Khác" in categories else categories[0]
    
    return f"""Bạn là AI phân loại giao dịch tài chính.

CATEGORIES (BẮT BUỘC chọn từ đây): [{categories_list}]

RULES:
1. category: PHẢI từ danh sách trên. Không khớp → "{fallback}"
2. type: "Thu nhập" (tiền vào) | "Chi phí" (tiền ra)
3. amount: "1tr"=1000000, "500k"=500000
4. confidence: 0.0-1.0

OUTPUT: Chỉ JSON
{{"amount": <số>, "category": "<từ danh sách>", "type": "<loại>", "confidence": <0-1>}}"""

# =====================
# OPTIMIZED MULTI-TRANSACTION System Prompt
# =====================
MULTI_TRANSACTION_SYSTEM_PROMPT = """Bạn là AI phân loại giao dịch tài chính Việt Nam.

RULES:
1. Nếu có NHIỀU giao dịch trong câu → tách thành "transactions" array
2. amount: "1tr"=1000000, "500k"=500000
3. type: "Thu nhập" | "Chi phí"

OUTPUT FORMAT:
- 1 giao dịch: {"amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}
- Nhiều giao dịch: {"transactions": [{"item": "X", "amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}, ...]}

Chỉ trả JSON, không text thêm."""

# =====================
# OPTIMIZED Multi-Transaction Closed-Domain
# =====================
@lru_cache(maxsize=64)
def build_multi_transaction_closed_domain_prompt(categories: tuple) -> str:
    """Build compact multi-transaction prompt for closed-domain (cached)"""
    categories_list = ", ".join(f'"{cat}"' for cat in categories)
    fallback = "Khác" if "Khác" in categories else categories[0]
    
    return f"""Bạn là AI phân loại giao dịch tài chính.

CATEGORIES: [{categories_list}]

RULES:
1. Nhiều giao dịch → tách thành "transactions" array
2. category: PHẢI từ danh sách trên. Không khớp → "{fallback}"
3. amount: "1tr"=1000000, "500k"=500000
4. type: "Thu nhập" | "Chi phí"

OUTPUT:
- 1 giao dịch: {{"amount": <số>, "category": "<từ danh sách>", "type": "<loại>", "confidence": <0-1>}}
- Nhiều: {{"transactions": [{{"item": "<tên>", "amount": <số>, "category": "<từ danh sách>", "type": "<loại>", "confidence": <0-1>}}, ...]}}

Chỉ JSON."""

# =====================
# User Prompt Templates - Compact
# =====================
def build_open_domain_user_prompt(transaction_text: str) -> str:
    """Compact user prompt for open-domain"""
    return f'"{transaction_text}" → JSON:'


def build_closed_domain_user_prompt(transaction_text: str, categories: List[str]) -> str:
    """Compact user prompt for closed-domain"""
    return f'"{transaction_text}" (chỉ category từ danh sách) → JSON:'


def build_multi_transaction_user_prompt(transaction_text: str, categories: List[str] = None) -> str:
    """Compact user prompt for multi-transaction"""
    if categories:
        return f'"{transaction_text}" (tách nhiều giao dịch nếu có, category từ danh sách) → JSON:'
    return f'"{transaction_text}" (tách nhiều giao dịch nếu có) → JSON:'


# =====================
# Backward Compatibility
# =====================
SYSTEM_PROMPT = OPEN_DOMAIN_SYSTEM_PROMPT


def get_system_prompt() -> str:
    """Get the default system prompt"""
    return OPEN_DOMAIN_SYSTEM_PROMPT


def build_user_prompt(transaction_text: str, categories: List[str]) -> str:
    """Backward compatible function"""
    if categories and len(categories) > 0:
        return build_closed_domain_user_prompt(transaction_text, categories)
    return build_open_domain_user_prompt(transaction_text)


def build_prompts(transaction_text: str, categories: List[str] = None) -> tuple:
    """Build both system and user prompts"""
    if categories and len(categories) > 0:
        # Convert to tuple for caching
        cat_tuple = tuple(categories)
        return (
            build_closed_domain_system_prompt(cat_tuple),
            build_closed_domain_user_prompt(transaction_text, categories)
        )
    return (
        OPEN_DOMAIN_SYSTEM_PROMPT,
        build_open_domain_user_prompt(transaction_text)
    )


# =====================
# Cache utilities
# =====================
def clear_prompt_cache():
    """Clear all cached prompts"""
    build_closed_domain_system_prompt.cache_clear()
    build_multi_transaction_closed_domain_prompt.cache_clear()


def get_cache_info():
    """Get cache statistics"""
    return {
        "closed_domain": build_closed_domain_system_prompt.cache_info(),
        "multi_transaction": build_multi_transaction_closed_domain_prompt.cache_info()
    }
