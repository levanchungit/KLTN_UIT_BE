"""
KLTN_UIT_BE Preprocessing Module
Text preprocessing for Vietnamese transaction descriptions
"""
import re
from typing import Dict, List, Optional, Tuple
def normalize_text(text: str) -> str:
    """
    Normalize Vietnamese transaction text
    
    Args:
        text: Raw transaction text
    
    Returns:
        Normalized text
    """
    if not text:
        return ""
    
    # Strip whitespace
    text = text.strip()
    
    # Normalize multiple spaces to single space
    text = re.sub(r'\s+', ' ', text)
    
    # Normalize Vietnamese number abbreviations
    text = _normalize_number_abbreviations(text)
    
    # Normalize common patterns
    text = _normalize_common_patterns(text)
    
    return text.strip()
def _normalize_number_abbreviations(text: str) -> str:
    """
    Normalize Vietnamese number abbreviations like "1tr", "200k"
    
    Args:
        text: Input text
    
    Returns:
        Text with normalized numbers
    """
    # Pattern for "Xtr" or "X tr" = X * 1,000,000
    # Pattern for "Xk" or "X K" = X * 1,000
    # Pattern for "X nghìn" = X * 1,000
    # Pattern for "X triệu" = X * 1,000,000
    
    result = text
    
    # Handle "1tr", "1.5tr", "2.5tr" -> multiply by 1,000,000
    result = re.sub(
        r'(\d+\.?\d*)\s*tr',
        lambda m: f"{float(m.group(1)) * 1000000:,.0f}".replace(",", "."),
        result,
        flags=re.IGNORECASE
    )
    
    # Handle "200k", "500k", "50.5k" -> multiply by 1,000
    result = re.sub(
        r'(\d+\.?\d*)\s*k',
        lambda m: f"{float(m.group(1)) * 1000:,.0f}".replace(",", "."),
        result,
        flags=re.IGNORECASE
    )
    
    # Handle "X nghìn" -> multiply by 1,000
    result = re.sub(
        r'(\d+\.?\d*)\s*nghìn',
        lambda m: f"{float(m.group(1)) * 1000:,.0f}".replace(",", "."),
        result,
        flags=re.IGNORECASE
    )
    
    # Handle "X triệu" -> multiply by 1,000,000
    result = re.sub(
        r'(\d+\.?\d*)\s*triệu',
        lambda m: f"{float(m.group(1)) * 1000000:,.0f}".replace(",", "."),
        result,
        flags=re.IGNORECASE
    )
    
    return result
def _normalize_common_patterns(text: str) -> str:
    """Normalize common patterns in Vietnamese transaction text"""
    result = text
    
    # Normalize "cho" patterns (parents giving money)
    result = re.sub(r'\b(mẹ|bố|cha|mẹ|ba|chồng|vợ|anh|chị|em)\s*cho\b', ' nhận từ ', result, flags=re.IGNORECASE)
    
    # Normalize "thanh toán" patterns
    result = re.sub(r'\b(thanh toán|trả tiền|pay)\b', ' thanh toán ', result, flags=re.IGNORECASE)
    
    # Normalize "mua" patterns
    result = re.sub(r'\b(mua|sắm|shopping)\b', ' mua ', result, flags=re.IGNORECASE)
    
    # Normalize "nhận lương" patterns
    result = re.sub(r'\b(nhận\s*)?lương\b', ' nhận lương ', result, flags=re.IGNORECASE)
    
    # Normalize "gửi tiền" patterns
    result = re.sub(r'\b(gửi tiền|nạp tiền)\b', ' gửi tiền ', result, flags=re.IGNORECASE)
    
    return result
def extract_keywords(text: str) -> Dict[str, List[str]]:
    """
    Extract keywords from transaction text
    
    Args:
        text: Transaction text
    
    Returns:
        Dictionary of keyword categories
    """
    keywords = {
        "money_in": [],
        "money_out": [],
        "persons": [],
        "places": [],
        "actions": []
    }
    
    text_lower = text.lower()
    
    # Money in keywords
    money_in_patterns = [
        r'nhận', r'được', r'cho', r'tặng', r'lương', r'thu', r'tiền\s*vào',
        r'hoàn\s*trả', r'hoàn\s*tiền', r'bonus', r'thưởng'
    ]
    for pattern in money_in_patterns:
        if re.search(pattern, text_lower):
            match = re.search(pattern, text_lower)
            keywords["money_in"].append(match.group(0))
    
    # Money out keywords
    money_out_patterns = [
        r'trả', r'thanh toán', r'mua', r'chi\s*tiêu', r'支出', r'pay',
        r'gửi', r'nạp', r'chuyển\s*đi', r'tiền\s*ra'
    ]
    for pattern in money_out_patterns:
        if re.search(pattern, text_lower):
            match = re.search(pattern, text_lower)
            keywords["money_out"].append(match.group(0))
    
    # Person keywords
    person_patterns = [
        r'mẹ', r'bố', r'cha', r'ba', r'chồng', r'vợ', r'anh', r'chị', r'em',
        r'bạn', r'đồng\s*nghiệp', r'sếp', r'cô', r'thầy', r'bạn\s*bè'
    ]
    for pattern in person_patterns:
        if re.search(pattern, text_lower):
            match = re.search(pattern, text_lower)
            keywords["persons"].append(match.group(0))
    
    # Action keywords
    action_patterns = [
        r'ăn', r'uống', r'cà\s*phê', r'đi\s*xe', r'grab', r'uber',
        r'shopping', r'mua\s*sắm', r'điện\s*thoại', r'wifi', r'điện',
        r'nước', r'gas', r'xăng', r'\d+'
    ]
    for pattern in action_patterns:
        if re.search(pattern, text_lower):
            match = re.search(pattern, text_lower)
            keywords["actions"].append(match.group(0))
    
    return keywords
def detect_transaction_type(text: str) -> Optional[str]:
    """
    Detect transaction type from text
    
    Args:
        text: Transaction text
    
    Returns:
        Transaction type: "Thu nhập", "Chi phí", "Chuyển khoản" or None
    """
    text_lower = text.lower()
    
    # Check for transfer patterns first
    transfer_patterns = [
        r'chuyển\s*khoản', r'chuyển\s*tiền', r'vietqr',
        r'transfer', r'banking', r'ví\s*điện\s*tử'
    ]
    for pattern in transfer_patterns:
        if re.search(pattern, text_lower):
            return "Chuyển khoản"
    
    # Check for income patterns
    income_patterns = [
        r'nhận\s*lương', r'lương', r'thưởng', r'bonus', r'quà\s*tặng',
        r'được\s*cho', r'được\s*tặng', r'hay\s*tiền', r'thu\s*nhập',
        r'hoàn\s*tiền', r'hoàn\s*trả', r'bán\s*đồ', r'tiền\s*từ'
    ]
    # Explicit patterns cho các trường hợp hay gặp trong giao dịch cá nhân
    extra_income_patterns = [
        # "Mẹ cho tiền", "Bố cho tiền", ...
        r'(mẹ|bố|ba|cha|anh|chị|em|bạn)\s*cho\s*tiền',
        # "Mẹ cho 1tr", "Bố cho 500k", ...
        r'(mẹ|bố|ba|cha|anh|chị|em|bạn)\s*cho\s*\d',
    ]
    income_patterns.extend(extra_income_patterns)
    for pattern in income_patterns:
        if re.search(pattern, text_lower):
            return "Thu nhập"
    
    # Check for expense patterns
    expense_patterns = [
        r'mua', r'trả', r'thanh\s*toán', r'chi\s*tiêu', r'支出',
        r'cà\s*phê', r'ăn\s*uống', r'di\s*chuyển', r'xăng', r'vé',
        r'hóa\s*đơn', r'điện', r'nước', r'wifi', r'internet',
        r'shopping', r'mua\s*sắm', r'giải\s*trí', r'sức\s*khỏe'
    ]
    for pattern in expense_patterns:
        if re.search(pattern, text_lower):
            return "Chi phí"
    
    # Default to expense if money amount is detected with spending verbs
    if re.search(r'\d+[ktr]\s*(?:cho|mua|thanh\s*toán)', text_lower):
        return "Chi phí"
    
    return None
def extract_amount_from_text(text: str) -> Optional[int]:
    """
    Extract amount from transaction text
    
    Args:
        text: Transaction text
    
    Returns:
        Amount in VND or None if not found
    """
    # Pattern for numbers with suffixes
    patterns = [
        # "1tr" or "1 triệu"
        (r'(\d+\.?\d*)\s*tr', 1000000),
        (r'(\d+\.?\d*)\s*triệu', 1000000),
        # "200k" or "200 K"
        (r'(\d+\.?\d*)\s*k', 1000),
        (r'(\d+\.?\d*)\s*nghìn', 1000),
        # "1.000.000", "1000000" format (không có hậu tố)
        (r'(\d{1,3}(?:\.\d{3})+|\d+)', 1),
    ]
    
    for pattern, multiplier in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            # Take the largest number found
            numbers = [float(m.replace('.', '').replace(',', '')) for m in matches]
            max_num = max(numbers)
            return int(max_num * multiplier)
    
    return None
# =====================
# Convenience Functions
# =====================
def preprocess_transaction(text: str) -> Tuple[str, Optional[str], Optional[int]]:
    """
    Complete preprocessing pipeline for transaction text
    
    Args:
        text: Raw transaction text
    
    Returns:
        Tuple of (normalized_text, detected_type, extracted_amount)
    """
    normalized = normalize_text(text)
    # Dùng text gốc để đoán loại giao dịch (giữ lại thông tin "Mẹ cho", "Bố cho", ...)
    trans_type = detect_transaction_type(text)
    # Dùng text đã chuẩn hoá để trích xuất số tiền
    amount = extract_amount_from_text(normalized)
    
    return normalized, trans_type, amount
