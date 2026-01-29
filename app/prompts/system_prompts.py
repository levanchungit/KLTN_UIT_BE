"""
KLTN_UIT_BE System Prompts
Enhanced prompt templates with Open-domain and Closed-domain classification
"""
from typing import List, Dict, Optional

# =====================
# Category Descriptions - Giúp LLM hiểu context của từng category
# =====================
CATEGORY_DESCRIPTIONS: Dict[str, Dict[str, any]] = {
    "Ăn uống": {
        "description": "Đồ ăn, thức uống, cà phê, trà sữa, nhà hàng",
        "keywords": ["ăn", "uống", "cơm", "phở", "bún", "cafe", "cà phê", "trà sữa", "highlands", "starbucks"],
        "examples": ["Ăn trưa 50k", "Cafe sáng 35k", "Trà sữa 45k"]
    },
    "Di chuyển": {
        "description": "Chi phí đi lại: grab, xăng, vé xe, taxi, gửi xe",
        "keywords": ["grab", "be", "xăng", "taxi", "xe ôm", "vé xe", "gửi xe", "đi lại"],
        "examples": ["Grab đi làm 45k", "Đổ xăng 150k", "Vé xe về quê 200k"]
    },
    "Mua sắm": {
        "description": "Quần áo, giày dép, đồ dùng, shopping",
        "keywords": ["mua", "shopping", "quần", "áo", "giày", "dép", "đồ dùng"],
        "examples": ["Mua áo 300k", "Shopping 500k"]
    },
    "Giải trí": {
        "description": "Xem phim, game, nhạc, Netflix, Spotify",
        "keywords": ["phim", "game", "netflix", "spotify", "youtube", "cgv", "rạp", "karaoke"],
        "examples": ["Vé xem phim 150k", "Nạp game 100k", "Netflix tháng 180k"]
    },
    "Hóa đơn": {
        "description": "Điện, nước, internet, wifi, gas",
        "keywords": ["điện", "nước", "internet", "wifi", "gas", "hóa đơn"],
        "examples": ["Tiền điện 500k", "Internet tháng 200k"]
    },
    "Sức khỏe": {
        "description": "Khám bệnh, thuốc, bệnh viện, gym, thể dục",
        "keywords": ["thuốc", "bệnh viện", "khám", "gym", "tập gym", "sức khỏe", "y tế"],
        "examples": ["Mua thuốc cảm 150k", "Khám bệnh 500k", "Thẻ gym tháng 800k"]
    },
    "Giáo dục": {
        "description": "Học phí, sách vở, khóa học, học online",
        "keywords": ["học", "sách", "khóa học", "học phí", "udemy", "coursera", "trường"],
        "examples": ["Đóng học phí 5tr", "Mua sách 200k", "Khóa học tiếng Anh 1tr"]
    },
    "Lương": {
        "description": "Thu nhập từ lương, thưởng, bonus công ty",
        "keywords": ["lương", "salary", "thưởng", "bonus", "thu nhập"],
        "examples": ["Nhận lương tháng 5 12tr", "Thưởng KPI 3tr", "Bonus cuối năm 5tr"]
    },
    "Quà tặng": {
        "description": "Tiền được cho/tặng từ người thân, bạn bè",
        "keywords": ["cho", "tặng", "mẹ cho", "bố cho", "được cho", "quà"],
        "examples": ["Mẹ cho 1tr", "Bạn tặng sinh nhật 500k", "Được bà ngoại cho 2tr"]
    },
    "Mỹ phẩm": {
        "description": "Kem dưỡng, serum, mặt nạ, son, make up, skincare",
        "keywords": ["mỹ phẩm", "kem", "serum", "mặt nạ", "son", "make up", "skincare", "dưỡng da"],
        "examples": ["Mua son 350k", "Serum vitamin C 450k", "Mặt nạ 120k"]
    },
    "Viễn thông": {
        "description": "Cước điện thoại, data 4G/5G, nạp tiền điện thoại",
        "keywords": ["4g", "5g", "data", "cước", "điện thoại", "mobifone", "viettel", "vinaphone"],
        "examples": ["Nạp tiền điện thoại 50k", "Mua gói data 4G 70k"]
    },
    "Đám tiệc": {
        "description": "Đám cưới, đám giỗ, sinh nhật, liên hoan",
        "keywords": ["đám cưới", "đám giỗ", "sinh nhật", "tiệc", "liên hoan", "mừng"],
        "examples": ["Mừng cưới bạn 500k", "Đám giỗ ông nội 300k", "Tiệc sinh nhật 200k"]
    },
    "Làm đẹp": {
        "description": "Cắt tóc, làm tóc, spa, nail, uốn, nhuộm",
        "keywords": ["tóc", "cắt tóc", "hớt tóc", "nhuộm", "uốn", "salon", "spa", "nail"],
        "examples": ["Cắt tóc 80k", "Nhuộm tóc 500k", "Làm nail 200k"]
    },
    "Cho vay": {
        "description": "Cho người khác mượn tiền",
        "keywords": ["cho vay", "cho mượn", "mượn"],
        "examples": ["Cho bạn mượn 500k", "Cho vay 1tr"]
    },
    "Trả nợ": {
        "description": "Trả nợ vay, trả góp, trả tiền mượn trước đó",
        "keywords": ["trả nợ", "trả góp", "hoàn nợ", "trả tiền"],
        "examples": ["Trả nợ bạn 1tr", "Trả góp điện thoại 2tr"]
    },
    "Khác": {
        "description": "Các giao dịch không thuộc danh mục nào ở trên",
        "keywords": [],
        "examples": ["Giao dịch khác"]
    }
}

# =====================
# OPEN-DOMAIN System Prompt - AI tự xác định category
# =====================
OPEN_DOMAIN_SYSTEM_PROMPT = """Bạn là AI chuyên gia phân loại giao dịch tài chính cá nhân Việt Nam.

## NHIỆM VỤ:
Phân tích câu mô tả giao dịch và TỰ XÁC ĐỊNH category phù hợp nhất.

## QUY TẮC:

### 1. Xác định loại giao dịch (type):
- "Thu nhập": Tiền VÀO (lương, quà, được cho, bán đồ, hoàn tiền, người khác trả)
- "Chi phí": Tiền RA (mua đồ, thanh toán, tiêu dùng)

### 2. Trích xuất số tiền (amount):
- "1tr" hoặc "1 triệu" = 1000000
- "500k" = 500000
- "50k" = 50000
- "10k" = 10000
- Không có số tiền → amount = 0

### 3. TỰ XÁC ĐỊNH category (quan trọng):
Dựa vào nội dung, xác định category NGẮN GỌN (1-3 từ tiếng Việt).

Các category phổ biến để tham khảo:
- Ăn uống (cơm, phở, cafe, trà sữa, nhà hàng, đồ ăn)
- Di chuyển (grab, taxi, xăng, vé xe, gửi xe, be)
- Mua sắm (quần áo, giày dép, đồ dùng, shopping)
- Giải trí (phim, game, Netflix, karaoke, Spotify)
- Hóa đơn (điện, nước, internet, wifi, gas)
- Sức khỏe (thuốc, khám bệnh, gym, bệnh viện)
- Giáo dục (học phí, sách, khóa học)
- Lương (salary, thưởng, bonus, lương tháng)
- Quà tặng (mẹ cho, bố cho, được tặng, quà)
- Mỹ phẩm (son, kem, skincare, mặt nạ)
- Viễn thông (4G, 5G, cước điện thoại, nạp tiền)
- Đám tiệc (cưới, giỗ, sinh nhật, liên hoan, mừng)
- Làm đẹp (cắt tóc, spa, nail, nhuộm tóc)
- Cho vay (cho mượn tiền)
- Trả nợ (trả tiền mượn, trả góp)
- Sửa chữa (sửa xe, sửa đồ)
- Khác (nếu không xác định được)

## VÍ DỤ PHÂN LOẠI:

Input: "Mẹ cho 1tr"
Output: {"amount": 1000000, "category": "Quà tặng", "type": "Thu nhập", "confidence": 0.95}

Input: "Grab đi làm sáng 45k"
Output: {"amount": 45000, "category": "Di chuyển", "type": "Chi phí", "confidence": 0.95}

Input: "Nhận lương tháng 5 15tr"
Output: {"amount": 15000000, "category": "Lương", "type": "Thu nhập", "confidence": 0.98}

Input: "Highlands 55k"
Output: {"amount": 55000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.92}

Input: "Mua son MAC 650k"
Output: {"amount": 650000, "category": "Mỹ phẩm", "type": "Chi phí", "confidence": 0.93}

Input: "Sửa xe máy 300k"
Output: {"amount": 300000, "category": "Sửa chữa", "type": "Chi phí", "confidence": 0.90}

Input: "Mừng cưới bạn Hùng 500k"
Output: {"amount": 500000, "category": "Đám tiệc", "type": "Chi phí", "confidence": 0.94}

Input: "Nạp game Liên Quân 100k"
Output: {"amount": 100000, "category": "Giải trí", "type": "Chi phí", "confidence": 0.92}

Input: "Cắt tóc 80k"
Output: {"amount": 80000, "category": "Làm đẹp", "type": "Chi phí", "confidence": 0.95}

Input: "Nạp 4G Viettel 70k"
Output: {"amount": 70000, "category": "Viễn thông", "type": "Chi phí", "confidence": 0.94}

Input: "Cho Minh mượn 2tr"
Output: {"amount": 2000000, "category": "Cho vay", "type": "Chi phí", "confidence": 0.90}

Input: "Bán điện thoại cũ 3tr"
Output: {"amount": 3000000, "category": "Thu nhập khác", "type": "Thu nhập", "confidence": 0.88}

## YÊU CẦU OUTPUT:
- CHỈ trả về JSON hợp lệ, KHÔNG có text thêm
- KHÔNG sử dụng markdown code block
- Category phải ngắn gọn, tiếng Việt
- Confidence từ 0.0 đến 1.0 (cao nếu chắc chắn)
"""

# =====================
# CLOSED-DOMAIN System Prompt - Phân loại vào danh sách cho trước
# =====================
def build_closed_domain_system_prompt(categories: List[str]) -> str:
    """
    Build system prompt for closed-domain classification with category descriptions
    """
    # Build category context with descriptions
    category_context = []
    for cat in categories:
        if cat in CATEGORY_DESCRIPTIONS:
            info = CATEGORY_DESCRIPTIONS[cat]
            category_context.append(
                f"- **{cat}**: {info['description']}"
            )
        else:
            category_context.append(f"- **{cat}**")
    
    categories_detail = "\n".join(category_context)
    categories_list = ", ".join(f'"{cat}"' for cat in categories)
    
    # Use first category for example (or "Khác" if available)
    example_category = "Khác" if "Khác" in categories else categories[0]
    
    return f"""Bạn là AI phân loại giao dịch tài chính. 

## DANH SÁCH CATEGORY ĐƯỢC PHÉP (CHỈ ĐƯỢC CHỌN TỪ ĐÂY):
[{categories_list}]

## QUY TẮC BẮT BUỘC:

1. **Category**: BẮT BUỘC phải là MỘT trong các giá trị: [{categories_list}]
   - KHÔNG ĐƯỢC tự tạo category mới
   - KHÔNG ĐƯỢC dùng category khác ngoài danh sách
   - Nếu không khớp category nào → dùng "{example_category}"

2. **Type**: "Thu nhập" (tiền vào) hoặc "Chi phí" (tiền ra)

3. **Amount**: Quy đổi VND (1tr=1000000, 500k=500000, 50k=50000)

## MÔ TẢ CATEGORIES:
{categories_detail}

## OUTPUT FORMAT (chỉ JSON, không text thêm):
{{"amount": <số>, "category": "<PHẢI từ danh sách trên>", "type": "<Thu nhập|Chi phí>", "confidence": <0-1>}}

## LƯU Ý QUAN TRỌNG:
- Nếu giao dịch là "Grab đi làm" nhưng danh sách KHÔNG có "Di chuyển" → chọn category gần nhất hoặc "{example_category}"
- Nếu giao dịch là "Mua cà phê" nhưng danh sách KHÔNG có "Ăn uống" → chọn category gần nhất hoặc "{example_category}"
- LUÔN LUÔN kiểm tra category trả về có trong danh sách [{categories_list}] không!
"""

# =====================
# User Prompt Templates
# =====================
def build_open_domain_user_prompt(transaction_text: str) -> str:
    """Build user prompt for open-domain classification"""
    return f"""Phân loại giao dịch sau:

"{transaction_text}"

Trả về JSON:"""


def build_closed_domain_user_prompt(transaction_text: str, categories: List[str]) -> str:
    """Build user prompt for closed-domain classification"""
    categories_str = ", ".join(f'"{cat}"' for cat in categories)
    
    return f"""Giao dịch: "{transaction_text}"

CHỈ ĐƯỢC chọn category từ: [{categories_str}]

Trả về JSON (category PHẢI nằm trong danh sách trên):"""

# =====================
# Backward Compatibility
# =====================
SYSTEM_PROMPT = OPEN_DOMAIN_SYSTEM_PROMPT

def get_system_prompt() -> str:
    """Get the default system prompt (open-domain)"""
    return OPEN_DOMAIN_SYSTEM_PROMPT

def build_user_prompt(transaction_text: str, categories: List[str]) -> str:
    """Backward compatible function"""
    if categories and len(categories) > 0:
        return build_closed_domain_user_prompt(transaction_text, categories)
    return build_open_domain_user_prompt(transaction_text)

def build_prompts(transaction_text: str, categories: List[str] = None) -> tuple:
    """
    Build both system and user prompts
    
    Args:
        transaction_text: The Vietnamese transaction description
        categories: List of valid categories (None for open-domain)
    
    Returns:
        Tuple of (system_prompt, user_prompt)
    """
    if categories and len(categories) > 0:
        # Closed-domain: phân loại vào danh sách cho trước
        return (
            build_closed_domain_system_prompt(categories),
            build_closed_domain_user_prompt(transaction_text, categories)
        )
    else:
        # Open-domain: AI tự xác định category
        return (
            OPEN_DOMAIN_SYSTEM_PROMPT,
            build_open_domain_user_prompt(transaction_text)
        )

# =====================
# MULTI-TRANSACTION System Prompt - Xử lý nhiều giao dịch trong một câu
# =====================
MULTI_TRANSACTION_SYSTEM_PROMPT = """Bạn là AI chuyên gia phân loại giao dịch tài chính cá nhân Việt Nam.

## NHIỆM VỤ:
Phân tích câu mô tả và TÁCH RIÊNG từng giao dịch nếu có NHIỀU giao dịch trong một câu.

## QUY TẮC:

### 1. Nhận diện nhiều giao dịch:
- Nếu câu có NHIỀU món/item với giá riêng → tách thành array
- Ví dụ: "Kem 50k sữa chua 42k" → 2 giao dịch riêng biệt

### 2. Trích xuất số tiền (amount):
- "1tr" = 1000000, "500k" = 500000, "50k" = 50000

### 3. Type:
- "Thu nhập": Tiền VÀO (lương, quà, được cho)
- "Chi phí": Tiền RA (mua đồ, thanh toán)

## OUTPUT FORMAT:

### Nếu CHỈ CÓ 1 giao dịch:
{"amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}

### Nếu CÓ NHIỀU giao dịch:
{
  "transactions": [
    {"item": "Kem", "amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95},
    {"item": "Sữa chua", "amount": 42000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}
  ]
}

## VÍ DỤ:

Input: "Kem 50k sữa chua 42k trà đào 50k"
Output: {"transactions": [{"item": "Kem", "amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}, {"item": "Sữa chua", "amount": 42000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}, {"item": "Trà đào", "amount": 50000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}]}

Input: "Grab 45k cafe 35k"
Output: {"transactions": [{"item": "Grab", "amount": 45000, "category": "Di chuyển", "type": "Chi phí", "confidence": 0.95}, {"item": "Cafe", "amount": 35000, "category": "Ăn uống", "type": "Chi phí", "confidence": 0.95}]}

Input: "Mẹ cho 1tr"
Output: {"amount": 1000000, "category": "Quà tặng", "type": "Thu nhập", "confidence": 0.95}

Input: "Nhận lương 15tr thưởng 3tr"
Output: {"transactions": [{"item": "Lương", "amount": 15000000, "category": "Lương", "type": "Thu nhập", "confidence": 0.95}, {"item": "Thưởng", "amount": 3000000, "category": "Lương", "type": "Thu nhập", "confidence": 0.95}]}

## YÊU CẦU:
- CHỈ trả về JSON, KHÔNG có text thêm
- KHÔNG dùng markdown code block
- Nếu có nhiều giao dịch → BẮT BUỘC dùng format "transactions" array
"""


def build_multi_transaction_closed_domain_prompt(categories: List[str]) -> str:
    """Build system prompt for multi-transaction closed-domain classification"""
    categories_list = ", ".join(f'"{cat}"' for cat in categories)
    example_category = "Khác" if "Khác" in categories else categories[0]
    
    return f"""Bạn là AI phân loại giao dịch tài chính.

## DANH SÁCH CATEGORY ĐƯỢC PHÉP:
[{categories_list}]

## NHIỆM VỤ:
Phân tích câu mô tả và TÁCH RIÊNG từng giao dịch nếu có NHIỀU giao dịch trong một câu.
Category BẮT BUỘC phải từ danh sách trên. Nếu không khớp → dùng "{example_category}".

## QUY TẮC:
1. Nếu câu có NHIỀU món/item với giá riêng → tách thành array
2. Amount: "1tr"=1000000, "500k"=500000, "50k"=50000
3. Type: "Thu nhập" (tiền vào) hoặc "Chi phí" (tiền ra)
4. Category: CHỈ được chọn từ [{categories_list}]

## OUTPUT FORMAT:

### Nếu CHỈ CÓ 1 giao dịch:
{{"amount": 50000, "category": "<từ danh sách>", "type": "Chi phí", "confidence": 0.95}}

### Nếu CÓ NHIỀU giao dịch:
{{
  "transactions": [
    {{"item": "Tên item 1", "amount": 50000, "category": "<từ danh sách>", "type": "Chi phí", "confidence": 0.95}},
    {{"item": "Tên item 2", "amount": 42000, "category": "<từ danh sách>", "type": "Chi phí", "confidence": 0.95}}
  ]
}}

## VÍ DỤ:
Input: "Kem 50k sữa chua 42k"
Output: {{"transactions": [{{"item": "Kem", "amount": 50000, "category": "{example_category}", "type": "Chi phí", "confidence": 0.95}}, {{"item": "Sữa chua", "amount": 42000, "category": "{example_category}", "type": "Chi phí", "confidence": 0.95}}]}}

## YÊU CẦU:
- CHỈ trả về JSON, KHÔNG text thêm
- Category PHẢI nằm trong danh sách [{categories_list}]
"""


def build_multi_transaction_user_prompt(transaction_text: str, categories: List[str] = None) -> str:
    """Build user prompt for multi-transaction parsing"""
    if categories and len(categories) > 0:
        categories_str = ", ".join(f'"{cat}"' for cat in categories)
        return f"""Giao dịch: "{transaction_text}"

CHỈ ĐƯỢC chọn category từ: [{categories_str}]
Nếu có NHIỀU giao dịch trong câu → tách thành array "transactions".

Trả về JSON:"""
    else:
        return f"""Giao dịch: "{transaction_text}"

Nếu có NHIỀU giao dịch trong câu → tách thành array "transactions".

Trả về JSON:"""


# =====================
# Fallback Prompt (simpler)
# =====================
FALLBACK_PROMPT = """Phân tích câu giao dịch sau và trả về JSON:

Câu: "{text}"

Output JSON với các trường: amount, category, type, confidence

Chỉ trả về JSON, không giải thích."""
