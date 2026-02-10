"""
KLTN_UIT_BE System Prompts - Optimized for Transaction Classification
Enhanced prompts for better accuracy with Qwen2.5-7B
Updated: 9 danh mục chuẩn (Ăn uống, Đi lại, Nhà ở, Mua sắm, Giải trí, Giáo dục, Y tế, Thu nhập, Chưa xác định)
"""
from typing import List, Tuple
from functools import lru_cache

# =====================
# OPTIMIZED FAST PROMPT (Recommended for performance)
# Compact but accurate - reduces token count by 60%
# =====================
FAST_SYSTEM_PROMPT = """Phân loại giao dịch tiếng Việt.

DANH MỤC: Ăn uống, Đi lại, Nhà ở, Mua sắm, Giải trí, Giáo dục, Y tế, Thu nhập, Chưa xác định

QUY TẮC:
- note: nội dung gốc cho từng giao dịch (lấy phần text tương ứng với mỗi số tiền)
- type: "Thu nhập" (tiền vào) | "Chi phí" (tiền ra)
- amount: "1tr"=1000000, "500k"=500000, "50k"=50000
- category: CHỌN TỪ DANH SÁCH trên
- confidence: 0.0-1.0

QUAN TRỌNG - NHIỀU SỐ TIỀN = NHIỀU GIAO DỊCH:
- Đếm SỐ TIỀN trong câu (20k, 30k, 50.000, 1tr...)
- 1 số tiền → 1 giao dịch
- 2+ số tiền → NHIỀU giao dịch (tách riêng!)

VÍ DỤ ĐƠN (1 số tiền):
"lương 10tr" → {"transactions": [{"note": "lương 10tr", "amount": 10000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.95}]}
"đi chợ 60k" → {"transactions": [{"note": "đi chợ 60k", "amount": 60000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}]}
"cafe 40k" → {"transactions": [{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}]}

VÍ DỤ NHIỀU (2 số tiền):
"cafe 40k grab 80k" → {"transactions": [{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 80k", "amount": 80000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}
"Ăn sáng 20k grab 30k" → {"transactions": [{"note": "Ăn sáng 20k", "amount": 20000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 30k", "amount": 30000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}
"trà sữa 60k xem phim 100k" → {"transactions": [{"note": "trà sữa 60k", "amount": 60000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "xem phim 100k", "amount": 100000, "category": "Giải trí", "type": "Chi phí", "confidence": 0.90}]}

CHỈ JSON! KHÔNG text thêm! LUÔN có "transactions" array!"""

# =====================
# COMPREHENSIVE SYSTEM PROMPT (Recommended for best accuracy)
# =====================
COMPREHENSIVE_SYSTEM_PROMPT = """Bạn là AI chuyên phân loại giao dịch tài chính cá nhân tiếng Việt.

## NHIỆM VỤ CHÍNH
Phân tích câu mô tả giao dịch và trích xuất:
- note: nội dung gốc cho từng giao dịch (lấy phần text tương ứng với mỗi số tiền)
- amount: Số tiền VND
- category: Danh mục giao dịch
- type: Loại giao dịch (Thu nhập/Chi phí)
- confidence: Độ tin cậy (0.0-1.0)

## DANH MỤC GIAO DỊCH (BẮT BUỘC chọn 1 trong list):
| Category | Ví dụ |
|----------|-------|
| "Ăn uống" | Đi chợ, thực phẩm, cơm, bún, phở, cafe, trà sữa, nhà hàng, quán ăn |
| "Đi lại" | Xăng xe, taxi, grab, bus, vé xe, đỗ xe, gửi xe, vận chuyển |
| "Nhà ở" | Tiền nhà, tiền phòng, tiền trọ, điện, nước, gas, wifi, internet |
| "Mua sắm" | Quần áo, giày dép, túi xách, đồ điện tử, đồ gia dụng, dụng cụ |
| "Giải trí" | Xem phim, netflix, game, karaoke, du lịch, spa, giải trí |
| "Giáo dục" | Học phí, sách vở, khóa học, chứng chỉ, gia sư, trung tâm |
| "Y tế" | Thuốc, khám bệnh, bệnh viện, bác sĩ, spa chăm sóc sức khỏe |
| "Thu nhập" | Lương, thưởng, tiền lãi, lợi nhuận, buôn bán, được cho tiền |
| "Chưa xác định" | Phí linh tinh, chi tiêu không rõ, đóng góp từ thiện, thuế |

## LOẠI GIAO DỊCH:
- "Thu nhập": tiền VÀO (lương, thưởng, quà tặng tiền, được cho, bán hàng)
- "Chi phí": tiền RA (mua sắm, thanh toán, ăn uống, di chuyển, dịch vụ)

## QUY TẮC SỐ TIỀN:
- "1tr", "1 triệu", "1.000.000" = 1000000 VND
- "500k", "500 nghìn", "500.000" = 500000 VND
- "50k" = 50000 VND
- "10d", "10đ" = 10 VND
- Nếu có dấu phẩy/đ hoặc chữ: tách số ra
- Giữ nguyên số nếu đã là số

## QUY TẮC PHÂN LOẠI:
1. Đọc kỹ câu mô tả, hiểu ngữ cảnh
2. Xác định loại (thu nhập/chi phí)
3. Chọn category phù hợp nhất
4. Trích xuất số tiền

## VÍ DỤ:
"Lương tháng 10tr" → {"transactions": [{"note": "lương 10tr", "amount": 10000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.95}]}
"Đi chợ 60k" → {"transactions": [{"note": "đi chợ 60k", "amount": 60000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}]}
"Mẹ cho 1 triệu" → {"transactions": [{"note": "mẹ cho 1 triệu", "amount": 1000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.90}]}
"Grab đi làm 45k" → {"transactions": [{"note": "Grab đi làm 45k", "amount": 45000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.85}]}
"Netflix tháng 47k" → {"transactions": [{"note": "Netflix tháng 47k", "amount": 47000, "category": "Giải trí", "type": "Chi phí", "confidence": 0.95}]}
"Thuốc cảm 25k" → {"transactions": [{"note": "Thuốc cảm 25k", "amount": 25000, "category": "Y tế", "type": "Chi phí", "confidence": 0.90}]}

## QUY TẮC OUTPUT:
- Chỉ trả JSON với "transactions" array, KHÔNG có text thêm
- Mỗi transaction PHẢI có "note": nội dung gốc tương ứng với số tiền đó
- Nếu câu có 1 giao dịch: {"transactions": [...]}
- Nếu câu có nhiều giao dịch: {"transactions": [...]}
- Confidence: 1.0 = chắc chắn, 0.5 = không chắc, 0.1 = đoán

VÍ DỤ ĐƠN (1 số tiền):
Input: "Lương tháng 10tr"
Output: {"transactions": [{"note": "Lương tháng 10tr", "amount": 10000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.95}]}

Input: "Đi chợ 60k"
Output: {"transactions": [{"note": "Đi chợ 60k", "amount": 60000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}]}

VÍ DỤ NHIỀU (2 số tiền):
Input: "Sáng uống cafe 40k, chiều grab 80k"
Output: {"transactions": [{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 80k", "amount": 80000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}

Input: "Ăn sáng 20k grab 30k"
Output: {"transactions": [{"note": "Ăn sáng 20k", "amount": 20000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 30k", "amount": 30000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}"""

# =====================
# DEFAULT PROMPTS (Backward compatible)
# =====================
OPEN_DOMAIN_SYSTEM_PROMPT = """Phân loại giao dịch tiếng Việt.

DANH MỤC: Ăn uống, Đi lại, Nhà ở, Mua sắm, Giải trí, Giáo dục, Y tế, Thu nhập, Chưa xác định

QUY TẮC:
- note: nội dung gốc cho từng giao dịch (lấy phần text tương ứng với mỗi số tiền)
- type: "Thu nhập" (tiền vào) | "Chi phí" (tiền ra)
- amount: "1tr"=1000000, "500k"=500000, "50k"=50000
- category: CHỌN TỪ DANH SÁCH trên
- confidence: 0.0-1.0

QUAN TRỌNG - NHIỀU SỐ TIỀN = NHIỀU GIAO DỊCH:
- Đếm SỐ TIỀN trong câu (20k, 30k, 50.000, 1tr...)
- 1 số tiền → 1 giao dịch
- 2+ số tiền → NHIỀU giao dịch (tách riêng!)

VÍ DỤ ĐƠN (1 số tiền):
"lương 10tr" → {"transactions": [{"note": "lương 10tr", "amount": 10000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.95}]}
"đi chợ 60k" → {"transactions": [{"note": "đi chợ 60k", "amount": 60000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}]}
"cafe 40k" → {"transactions": [{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}]}

VÍ DỤ NHIỀU (2 số tiền):
"cafe 40k grab 80k" → {"transactions": [{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 80k", "amount": 80000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}
"Ăn sáng 20k grab 30k" → {"transactions": [{"note": "Ăn sáng 20k", "amount": 20000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 30k", "amount": 30000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}
"trà sữa 60k xem phim 100k" → {"transactions": [{"note": "trà sữa 60k", "amount": 60000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "xem phim 100k", "amount": 100000, "category": "Giải trí", "type": "Chi phí", "confidence": 0.90}]}

CHỈ JSON! KHÔNG text thêm! LUÔN có "transactions" array!"""

# =====================
# DYNAMIC PROMPT BUILDER (For user-specific categories)
# =====================
@lru_cache(maxsize=128)
def build_dynamic_system_prompt(categories: Tuple[str, ...]) -> str:
    """Build system prompt with user-specific categories (cached)"""
    if not categories:
        return OPEN_DOMAIN_SYSTEM_PROMPT
    
    cats_list = ", ".join(f'"{cat}"' for cat in categories)
    fallback = "Chưa xác định" if "Chưa xác định" in categories else categories[0]
    
    return f"""Phân loại giao dịch tiếng Việt với danh mục cho trước.

DANH MỤC: {cats_list}

QUY TẮC:
- note: nội dung gốc cho từng giao dịch (lấy phần text tương ứng với mỗi số tiền)
- type: "Thu nhập" (tiền vào) | "Chi phí" (tiền ra)
- amount: "1tr"=1000000, "500k"=500000, "50k"=50000
- category: CHỌN TỪ DANH SÁCH trên. Không khớp → "{fallback}"
- confidence: 0.0-1.0

QUAN TRỌNG - NHIỀU SỐ TIỀN = NHIỀU GIAO DỊCH:
- Đếm SỐ TIỀN trong câu (20k, 30k, 50.000, 1tr...)
- 1 số tiền → 1 giao dịch
- 2+ số tiền → NHIỀU giao dịch (tách riêng!)

VÍ DỤ ĐƠN (1 số tiền):
"lương 10tr" → {{"transactions": [{{"note": "lương 10tr", "amount": 10000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.95}}]}}
"cafe 40k" → {{"transactions": [{{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}}]}}

VÍ DỤ NHIỀU (2 số tiền):
"cafe 40k grab 80k" → {{"transactions": [{{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}}, {{"note": "grab 80k", "amount": 80000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}}]}}
"Ăn sáng 20k grab 30k" → {{"transactions": [{{"note": "Ăn sáng 20k", "amount": 20000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}}, {{"note": "grab 30k", "amount": 30000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}}]}}

CHỈ JSON! KHÔNG text thêm! LUÔN có "transactions" array!"""

# =====================
# USER PROMPT BUILDERS
# =====================
def build_user_prompt(transaction_text: str) -> str:
    """Build user prompt for open-domain"""
    return f'Phân tích giao dịch: "{transaction_text}"\n\nTrả lời JSON:'

def build_user_prompt_with_categories(transaction_text: str, categories: List[str]) -> str:
    """Build user prompt with category list"""
    cats = ", ".join(categories)
    return f'Phân tích: "{transaction_text}"\nCategories: {cats}\n\nJSON:'

# =====================
# FEW-SHOT EXAMPLES (Optional for better accuracy)
# =====================
FEW_SHOT_EXAMPLES = """
## VÍ DỤ ĐƠN:
- "Lương tháng 10tr" → {{"transactions": [{{"note": "Lương tháng 10tr", "amount": 10000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.95}}]}}
- "Đi chợ 60k" → {{"transactions": [{{"note": "Đi chợ 60k", "amount": 60000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}}]}}
- "Mẹ cho 1 triệu" → {{"transactions": [{{"note": "Mẹ cho 1 triệu", "amount": 1000000, "category": "Thu nhập", "type": "Thu nhập", "confidence": 0.90}}]}}

## VÍ DỤ NHIỀU:
- "cafe 40k grab 80k" → {{"transactions": [{{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}}, {{"note": "grab 80k", "amount": 80000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}}]}}
- "Ăn sáng 20k grab 30k" → {{"transactions": [{{"note": "Ăn sáng 20k", "amount": 20000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}}, {{"note": "grab 30k", "amount": 30000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}}]}}
"""

# =====================
# MULTI-TRANSACTION PROMPT
# =====================
MULTI_TRANSACTION_PROMPT = """Phân loại giao dịch tiếng Việt - TÁCH nhiều giao dịch nếu có!

DANH MỤC: Ăn uống, Đi lại, Nhà ở, Mua sắm, Giải trí, Giáo dục, Y tế, Thu nhập, Chưa xác định

QUY TẮC:
- note: nội dung gốc cho từng giao dịch (lấy phần text tương ứng với mỗi số tiền)
- type: "Thu nhập" (tiền vào) | "Chi phí" (tiền ra)
- amount: "1tr"=1000000, "500k"=500000, "50k"=50000
- category: CHỌN TỪ DANH SÁCH trên
- confidence: 0.0-1.0

QUAN TRỌNG:
- Đếm SỐ TIỀN trong câu → Mỗi số tiền = 1 giao dịch
- Nhiều số tiền → NHIỀU giao dịch (tách riêng!)

VÍ DỤ ĐƠN:
"cafe 40k" → {"transactions": [{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}]}

VÍ DỤ NHIỀU:
"cafe 40k grab 80k" → {"transactions": [{"note": "cafe 40k", "amount": 40000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 80k", "amount": 80000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}
"Ăn sáng 20k grab 30k" → {"transactions": [{"note": "Ăn sáng 20k", "amount": 20000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.90}, {"note": "grab 30k", "amount": 30000, "category": "Đi lại", "type": "Chi phí", "confidence": 0.90}]}

CHỈ JSON! LUÔN có "transactions" array!"""

# =====================
# DEFAULT EXPORTS - Use FAST prompt for performance
# =====================
SYSTEM_PROMPT = FAST_SYSTEM_PROMPT

def get_system_prompt() -> str:
    """Get the fast/optimized system prompt (recommended for performance)"""
    return FAST_SYSTEM_PROMPT

def get_comprehensive_system_prompt() -> str:
    """Get the comprehensive system prompt (for complex cases)"""
    return COMPREHENSIVE_SYSTEM_PROMPT

def get_fast_system_prompt() -> str:
    """Get the fast/compact system prompt"""
    return FAST_SYSTEM_PROMPT

def get_multi_transaction_prompt() -> str:
    """Get the multi-transaction prompt"""
    return MULTI_TRANSACTION_PROMPT

def build_prompts(transaction_text: str, categories: List[str] = None) -> Tuple[str, str]:
    """Build system and user prompts"""
    if categories and len(categories) > 0:
        sys_prompt = build_dynamic_system_prompt(tuple(categories))
        user_prompt = build_user_prompt_with_categories(transaction_text, categories)
    else:
        sys_prompt = COMPREHENSIVE_SYSTEM_PROMPT
        user_prompt = build_user_prompt(transaction_text)
    
    return sys_prompt, user_prompt

def clear_cache():
    """Clear prompt cache"""
    build_dynamic_system_prompt.cache_clear()
