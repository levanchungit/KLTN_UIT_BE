"""
Conversation Message Generator Service
Generates context-aware, friendly responses based on transaction data and user input using LLM
"""
import random
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.services.llm_service import get_llm_service, LLMServiceError

logger = logging.getLogger(__name__)


# =====================
# Time-based Context
# =====================
def get_time_period() -> str:
    """Get current time period for contextual messages"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "sáng"
    elif 12 <= hour < 17:
        return "chiều"
    elif 17 <= hour < 22:
        return "tối"
    else:
        return "khuya"


def get_time_emoji() -> str:
    """Get emoji based on time"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "🌅"
    elif 12 <= hour < 17:
        return "🌤️"
    elif 17 <= hour < 22:
        return "🌙"
    else:
        return "🌃"


# =====================
# LLM-based Message Generator
# =====================
def generate_conversation_message(
    amount: int,
    transactions: Optional[List[Dict[str, Any]]] = None,
    original_text: str = ""
) -> str:
    """
    Generate a natural, context-aware conversational message using LLM
    
    The LLM reads the user's input and generates a response that:
    - Understands the context (what they bought, who with, time of day, etc.)
    - Speaks naturally like a Vietnamese friend
    - Adds appropriate emojis based on context
    
    Args:
        amount: Total transaction amount
        transactions: List of individual transactions (if multi-transaction)
        original_text: Original user input text
    
    Returns:
        Natural, context-aware message for user interaction
    """
    llm_service = get_llm_service()
    
    # Check if LLM is available
    if not llm_service.is_available():
        logger.warning("LLM not available, using fallback message")
        return _generate_fallback_message(amount, original_text)
    
    try:
        # Build transactions summary
        tx_list = []
        if transactions:
            for i, tx in enumerate(transactions, 1):
                note = tx.get("note", "").strip()
                amount_tx = tx.get("amount", 0)
                category = tx.get("category", "Khác")
                tx_type = tx.get("type", "Chi phí")
                tx_list.append({
                    "stt": i,
                    "nội dung": note,
                    "số tiền": f"{amount_tx:,}đ",
                    "danh mục": category,
                    "loại": tx_type
                })
        else:
            tx_list = [{"nội dung": original_text, "số tiền": f"{amount:,}đ"}]
        
        # Build the LLM prompt
        time_period = get_time_period()
        time_emoji = get_time_emoji()
        
        prompt = f"""Bạn là một người bạn thân thiện, nói chuyện tự nhiên bằng tiếng Việt.

## Giao dịch của user:
{tx_list}

## Input gốc của user:
"{original_text}"

## Thời điểm trong ngày: {time_period}

## Yêu cầu:
Viết MỘT câu trả lời NGẮN GỌN, THÂN THIỆN như bạn bè:

📌 QUAN TRỌNG - Đọc kỹ input để hiểu ngữ cảnh:
- User nói gì? (mua gì, với ai, ở đâu, thời gian nào)
- Áp dụng kiến thức thường thức:
  • "cafe sáng/buổi sáng" → ☕🌅
  • "ăn trưa" → 🍚🌤️
  • "ăn tối" → 🍽️🌙
  • "grab/xe" → 🚗🛵
  • "mẹ/ba/cha cho tiền" → 💰❤️ family
  • "lương thưởng" → 💼🎉
  • "mua đồ ăn" → 🍜🍕
  • "uống trà sữa" → 🧋😋
  • "xem phim/giải trí" → 🎬🎮
  • "mua quần áo" → 🛍️👕
  • "tiền điện/nước/wifi" → 📱💡
  • "thể thao/gym" → 💪🏃

📝 Ví dụ:
- Input: "Cà phê sáng 40k" → "☕🌅 Sáng nay nhấm nháp cà phê thơm ngon!"
- Input: "Mẹ cho 1tr" → "💰❤️ Mẹ cho tiền rồi! Mẹ yêu thương quá!"
- Input: "Grab về nhà 50k" → "🚗🏠 Về nhà an toàn nhé!"
- Input: "Trà sữa 30k với bạn" → "🧋😄 Uống trà sữa với bạn vui quá!"
- Input: "Lương 10tr" → "💼🎉 Lương về rồi! Chúc mừng bạn!"

❌ KHÔNG viết:
- "Giao dịch đã được xử lý" (quá máy móc)
- "Tổng tiền: Xđ" (đã hiển thị riêng)
- "Chi phí cho: Y" (lặp lại thông tin)
- Quá dài dòng (>15 từ)

✅ VIẾT:
- Như một người bạn thật sự đang trò chuyện
- Dựa vào NGỮ CẢNH thực tế trong input
- Thêm emoji phù hợp với hoạt động
- 1-2 câu ngắn gọn

Câu trả lời:"""

        # Get LLM response
        response = llm_service.get_prediction(
            system_prompt="Bạn là một người bạn thân thiện, nói chuyện tự nhiên bằng tiếng Việt. Bạn hiểu ngữ cảnh và phản hồi tự nhiên như bạn bè đang trò chuyện.",
            user_prompt=prompt,
            temperature=0.8,
            max_tokens=80
        )
        
        # Clean up response
        message = response.strip()
        
        # Remove quotes if present
        if message.startswith('"') and message.endswith('"'):
            message = message[1:-1]
        
        # Ensure message is valid
        if not message or len(message) < 5:
            logger.warning(f"Invalid LLM response: '{message}', using fallback")
            return _generate_fallback_message(amount, original_text)
        
        # Truncate if too long
        if len(message) > 150:
            message = message[:147] + "..."
        
        logger.info(f"LLM generated message: '{message}'")
        return message
        
    except LLMServiceError as e:
        logger.error(f"LLM service error: {e}, using fallback")
        return _generate_fallback_message(amount, original_text)
    except Exception as e:
        logger.error(f"Error generating message: {e}", exc_info=True)
        return _generate_fallback_message(amount, original_text)


# =====================
# Fallback Messages (when LLM unavailable)
# =====================
def _generate_fallback_message(
    amount: int,
    original_text: str = ""
) -> str:
    """Generate fallback message when LLM is unavailable"""
    text_lower = original_text.lower()
    time_emoji = get_time_emoji()
    
    # Detect context from text
    if any(w in text_lower for w in ["lương", "thưởng", "lương thưởng"]):
        return f"💼🎉 Lương về rồi! Tuyệt vời!"
    
    if any(w in text_lower for w in ["mẹ", "ba", "cha", "cho", "tặng", "mình"]):
        return f"💰❤️ Tiền vào rồi! Tốt lắm!"
    
    if any(w in text_lower for w in ["ăn", "sáng", "trưa", "tối", "bún", "phở", "cơm", "bánh"]):
        return f"{time_emoji} Ăn uống ngon miệng nhé!"
    
    if any(w in text_lower for w in ["cafe", "cà phê", "trà", "trà sữa", "nước"]):
        return f"☕ Uống gì ngon lắm đấy!"
    
    if any(w in text_lower for w in ["grab", "xe", "taxi", "di chuyển"]):
        return f"🚗 Di chuyển an toàn nhé!"
    
    if any(w in text_lower for w in ["mua", "shop", "quần áo", "đồ"]):
        return f"🛍️ Mua sắm vui vẻ nhé!"
    
    if any(w in text_lower for w in ["phim", "game", "giải trí", "hát"]):
        return f"🎬 Giải trí vui nhé!"
    
    if any(w in text_lower for w in ["điện", "nước", "wifi", "tiền nhà"]):
        return f"✅ Tiện ích đã thanh toán!"
    
    # Default
    formatted_amount = f"{amount:,}đ"
    return f"✅ Xong rồi nhé! {formatted_amount}"


# Export function
__all__ = ["generate_conversation_message"]
