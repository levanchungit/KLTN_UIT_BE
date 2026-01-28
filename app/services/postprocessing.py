"""
KLTN_UIT_BE Postprocessing Module
JSON parsing, validation, and error handling for LLM responses
"""
import json
import logging
import re
from typing import Any, Dict, List, Optional, Tuple
from app.config import get_settings
logger = logging.getLogger(__name__)
class PostprocessingError(Exception):
    """Custom exception for postprocessing errors"""
    pass
def clean_llm_output(raw_output: str) -> str:
    """
    Clean LLM output by removing markdown code blocks and extra whitespace
    
    Args:
        raw_output: Raw LLM output
    
    Returns:
        Cleaned text
    """
    if not raw_output:
        return ""
    
    # Remove markdown code blocks (```json or ```)
    cleaned = re.sub(r'```(?:json)?\s*', '', raw_output)
    cleaned = re.sub(r'\s*```', '', cleaned)
    
    # Remove any leading/trailing whitespace
    cleaned = cleaned.strip()
    
    # Remove any explanatory text before JSON
    # Look for the first { and last }
    start_idx = cleaned.find('{')
    end_idx = cleaned.rfind('}')
    
    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        cleaned = cleaned[start_idx:end_idx+1]
    elif start_idx == -1:
        # Try finding [ for arrays
        start_idx = cleaned.find('[')
        end_idx = cleaned.rfind(']')
        if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
            cleaned = cleaned[start_idx:end_idx+1]
    
    return cleaned
def parse_json_response(raw_output: str) -> Dict[str, Any]:
    """
    Parse LLM output as JSON
    
    Args:
        raw_output: Raw LLM output
    
    Returns:
        Parsed JSON dictionary
    
    Raises:
        PostprocessingError: If JSON parsing fails
    """
    cleaned = clean_llm_output(raw_output)
    
    try:
        result = json.loads(cleaned)
        logger.debug(f"Successfully parsed JSON: {result}")
        return result
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {cleaned[:200]}...")
        raise PostprocessingError(f"Invalid JSON format: {e}")
def validate_prediction(
    prediction: Dict[str, Any],
    valid_categories: List[str],
    valid_types: List[str],
    min_amount: int = 0,
    max_amount: int = 10_000_000_000,
    min_confidence: float = 0.0,
    max_confidence: float = 1.0
) -> Tuple[bool, List[str]]:
    """
    Validate prediction against constraints
    
    Args:
        prediction: Prediction dictionary with amount, category, type, confidence
        valid_categories: List of valid categories
        valid_types: List of valid transaction types
        min_amount: Minimum valid amount
        max_amount: Maximum valid amount
        min_confidence: Minimum valid confidence
        max_confidence: Maximum valid confidence
    
    Returns:
        Tuple of (is_valid, list of validation errors)
    """
    errors = []
    
    # Validate amount
    amount = prediction.get("amount")
    if amount is None:
        errors.append("Missing 'amount' field")
    elif not isinstance(amount, (int, float)):
        errors.append(f"'amount' must be a number, got {type(amount).__name__}")
    elif amount < min_amount:
        errors.append(f"'amount' ({amount}) is below minimum ({min_amount})")
    elif amount > max_amount:
        errors.append(f"'amount' ({amount}) exceeds maximum ({max_amount})")
    
    # Validate category
    category = prediction.get("category")
    if category is None:
        errors.append("Missing 'category' field")
    elif not isinstance(category, str):
        errors.append(f"'category' must be a string, got {type(category).__name__}")
    elif category not in valid_categories:
        errors.append(f"Category '{category}' is not in valid categories: {valid_categories}")
    
    # Validate type
    trans_type = prediction.get("type")
    if trans_type is None:
        errors.append("Missing 'type' field")
    elif not isinstance(trans_type, str):
        errors.append(f"'type' must be a string, got {type(trans_type).__name__}")
    elif trans_type not in valid_types:
        errors.append(f"Type '{trans_type}' is not in valid types: {valid_types}")
    
    # Validate confidence
    confidence = prediction.get("confidence")
    if confidence is None:
        errors.append("Missing 'confidence' field")
    elif not isinstance(confidence, (int, float)):
        errors.append(f"'confidence' must be a number, got {type(confidence).__name__}")
    elif confidence < min_confidence:
        errors.append(f"'confidence' ({confidence}) is below minimum ({min_confidence})")
    elif confidence > max_confidence:
        errors.append(f"'confidence' ({confidence}) exceeds maximum ({max_confidence})")
    
    return len(errors) == 0, errors
def normalize_category(category: str, valid_categories: List[str]) -> str:
    """
    Normalize category to match valid categories
    
    Args:
        category: Predicted category
        valid_categories: List of valid categories
    
    Returns:
        Normalized category that exists in valid list, or "Khác" if not found
    """
    if not category:
        return "Khác"
    
    # Direct match
    for valid in valid_categories:
        if category.lower() == valid.lower():
            return valid
    
    # Partial match (category is contained in valid or vice versa)
    category_lower = category.lower().strip()
    for valid in valid_categories:
        valid_lower = valid.lower()
        if category_lower in valid_lower or valid_lower in category_lower:
            return valid
    
    # Check for similar categories
    category_mapping = {
        "ăn": "Ăn uống",
        "đồ ăn": "Ăn uống",
        "cà phê": "Ăn uống",
        "cafe": "Ăn uống",
        "coffee": "Ăn uống",
        "shop": "Mua sắm",
        "shopping": "Mua sắm",
        "mua sắm": "Mua sắm",
        "di chuyển": "Di chuyển",
        "đi lại": "Di chuyển",
        "grab": "Di chuyển",
        "vé": "Di chuyển",
        "xăng": "Di chuyển",
        "giải trí": "Giải trí",
        "game": "Giải trí",
        "phim": "Giải trí",
        "sức khỏe": "Sức khỏe",
        "thuốc": "Sức khỏe",
        "bệnh viện": "Sức khỏe",
        "hóa đơn": "Hóa đơn",
        "điện": "Hóa đơn",
        "nước": "Hóa đơn",
        "wifi": "Hóa đơn",
        "internet": "Hóa đơn",
        "lương": "Lương",
        "thưởng": "Lương",
        "quà": "Quà tặng",
        "tặng": "Quà tặng",
        "cho": "Quà tặng",
        "vay": "Mượn tiền",
        "nợ": "Mượn tiền",
        "trả nợ": "Mượn tiền",
        "học": "Giáo dục",
        "khóa học": "Giáo dục",
        "sách": "Giáo dục",
    }
    
    for key, mapped in category_mapping.items():
        if key in category_lower:
            # Check if mapped category is valid
            for valid in valid_categories:
                if mapped.lower() == valid.lower():
                    return valid
    
    # Default to "Khác"
    for valid in valid_categories:
        if valid.lower() == "khác":
            return valid
    
    return valid_categories[-1] if valid_categories else "Khác"
def normalize_type(trans_type: str, valid_types: List[str]) -> str:
    """
    Normalize transaction type to match valid types
    
    Args:
        trans_type: Predicted transaction type
        valid_types: List of valid types
    
    Returns:
        Normalized type that exists in valid list
    """
    if not trans_type:
        return valid_types[1] if len(valid_types) > 1 else "Chi phí"  # Default to expense
    
    # Direct match
    for valid in valid_types:
        if trans_type.lower() == valid.lower():
            return valid
    
    # Check for income indicators
    income_indicators = ["thu", "nhận", "lương", "bonus", "thưởng", "vào", "income"]
    if any(ind in trans_type.lower() for ind in income_indicators):
        for valid in valid_types:
            if "thu" in valid.lower():
                return valid
    
    # Check for expense indicators
    expense_indicators = ["chi", "tiêu", "trả", "mua", "ra", "支出", "expense"]
    if any(ind in trans_type.lower() for ind in expense_indicators):
        for valid in valid_types:
            if "tiêu" in valid.lower():
                return valid
    
    # Check for transfer indicators
    transfer_indicators = ["chuyển", "khoản", "banking", "transfer"]
    if any(ind in trans_type.lower() for ind in transfer_indicators):
        for valid in valid_types:
            if "khoản" in valid.lower():
                return valid
    
    # Default to "Chi phí"
    return valid_types[1] if len(valid_types) > 1 else "Chi phí"
def clamp_confidence(confidence: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """
    Clamp confidence value to valid range
    
    Args:
        confidence: Confidence value
        min_val: Minimum value
        max_val: Maximum value
    
    Returns:
        Clamped confidence value
    """
    return max(min_val, min(max_val, confidence))
def fix_prediction(
    prediction: Dict[str, Any],
    valid_categories: List[str],
    valid_types: List[str],
    min_amount: int = 0,
    max_amount: int = 10_000_000_000
) -> Dict[str, Any]:
    """
    Try to fix an invalid prediction
    
    Args:
        prediction: Raw prediction dictionary
        valid_categories: List of valid categories
        valid_types: List of valid types
        min_amount: Minimum valid amount
        max_amount: Maximum valid amount
    
    Returns:
        Fixed prediction dictionary
    """
    fixed = prediction.copy()
    
    # Fix category
    if "category" not in fixed or fixed.get("category") not in valid_categories:
        fixed["category"] = normalize_category(
            fixed.get("category", ""), valid_categories
        )
    
    # Fix type
    if "type" not in fixed or fixed.get("type") not in valid_types:
        fixed["type"] = normalize_type(fixed.get("type", ""), valid_types)
    
    # Fix amount
    amount = fixed.get("amount", 0)
    if not isinstance(amount, (int, float)) or amount < min_amount or amount > max_amount:
        fixed["amount"] = 0
    
    # Fix confidence
    confidence = fixed.get("confidence", 0.5)
    if not isinstance(confidence, (int, float)):
        confidence = 0.5
    fixed["confidence"] = clamp_confidence(float(confidence))
    
    return fixed
def process_llm_response(
    raw_output: str,
    valid_categories: List[str],
    valid_types: List[str],
    fix_invalid: bool = True
) -> Dict[str, Any]:
    """
    Complete postprocessing pipeline for LLM response
    
    Args:
        raw_output: Raw LLM output
        valid_categories: List of valid categories
        valid_types: List of valid transaction types
        fix_invalid: Whether to try fixing invalid predictions
    
    Returns:
        Processed prediction dictionary
    
    Raises:
        PostprocessingError: If parsing fails and fix_invalid is False
    """
    settings = get_settings()
    validation = settings.validation
    
    # Parse JSON
    try:
        prediction = parse_json_response(raw_output)
    except PostprocessingError as e:
        if fix_invalid:
            logger.warning(f"JSON parse failed, creating fallback prediction: {e}")
            return create_fallback_prediction(valid_categories, valid_types, raw_output)
        raise
    
    # Validate
    is_valid, errors = validate_prediction(
        prediction,
        valid_categories,
        valid_types,
        min_amount=validation.min_amount,
        max_amount=validation.max_amount,
        min_confidence=validation.confidence_min,
        max_confidence=validation.confidence_max
    )
    
    if is_valid:
        logger.debug(f"Prediction valid: {prediction}")
        return prediction
    
    # Log validation errors
    logger.warning(f"Validation errors: {errors}")
    
    if fix_invalid:
        logger.info("Attempting to fix invalid prediction...")
        return fix_prediction(prediction, valid_categories, valid_types)
    
    # Return original prediction with errors
    return {
        **prediction,
        "_validation_errors": errors,
        "_raw_output": raw_output
    }
def create_fallback_prediction(
    valid_categories: List[str],
    valid_types: List[str],
    raw_output: str = ""
) -> Dict[str, Any]:
    """
    Create a fallback prediction when parsing fails
    
    Args:
        valid_categories: List of valid categories
        valid_types: List of valid types
        raw_output: Raw LLM output for debugging
    
    Returns:
        Fallback prediction dictionary
    """
    # Try to extract basic info from raw output
    amount = 0
    category = "Khác"
    trans_type = "Chi phí"
    
    # Try to extract amount from raw output
    import re
    amount_patterns = [
        r'"amount"\s*:\s*(\d+)',
        r'amount[:\s]+(\d+)',
        r'(\d+(?:\.\d+)?)\s*(?:vnd|đ)'
    ]
    for pattern in amount_patterns:
        match = re.search(pattern, raw_output, re.IGNORECASE)
        if match:
            try:
                amount = int(float(match.group(1)))
                break
            except ValueError:
                pass
    
    # Try to extract category
    cat_pattern = r'"category"\s*:\s*"([^"]+)"'
    match = re.search(cat_pattern, raw_output)
    if match:
        category = normalize_category(match.group(1), valid_categories)
    
    # Try to extract type
    type_pattern = r'"type"\s*:\s*"([^"]+)"'
    match = re.search(type_pattern, raw_output)
    if match:
        trans_type = normalize_type(match.group(1), valid_types)
    
    return {
        "amount": amount,
        "category": category,
        "type": trans_type,
        "confidence": 0.0,
        "_fallback": True,
        "_raw_output": raw_output
    }
