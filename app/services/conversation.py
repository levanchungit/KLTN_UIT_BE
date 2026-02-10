"""
Conversation Message Generator — LLM-based friendly responses for transactions.
"""
import re, json, logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.services.llm_service import get_llm_service, LLMServiceError

logger = logging.getLogger(__name__)

# ── Compiled regex for CJK / garbage detection ──
_CJK_RE = re.compile(r'[\u3000-\u9fff\u2e80-\u2eff\uff00-\uffef\u3040-\u30ff]+')
_VN_RE  = re.compile(r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ]', re.I)
_EMOJI_RE = re.compile(r'[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u27BF]')
_META_RE = re.compile(r'(?:生命周期|以下是|翻译\s*结果|在一次.*对话中|(?:Here|The|This)\s+(?:is|are)|(?:Note|Output|Result|Response)\s*:).*', re.I | re.DOTALL)

# ── Time helpers ──
_TIME_MAP = [(5, 12, "sáng", "🌅"), (12, 17, "chiều", "🌤️"), (17, 22, "tối", "🌙")]

def _time_info() -> tuple:
    h = datetime.now().hour
    for lo, hi, name, emoji in _TIME_MAP:
        if lo <= h < hi:
            return name, emoji
    return "khuya", "🌃"

# ── Clean LLM output ──
def _clean(raw: str) -> str:
    """Strip JSON wrappers, CJK, meta-text, markdown from LLM output."""
    if not raw:
        return ""
    msg = raw.strip()

    # Extract from JSON wrapper: {"key": "value"} or {"raw text"}
    if msg.startswith('{') and '}' in msg:
        try:
            d = json.loads(msg)
            if isinstance(d, dict):
                for k in ('message', 'text', 'response', 'reply', 'content'):
                    if k in d:
                        msg = str(d[k]); break
                else:
                    msg = next((str(v) for v in d.values() if isinstance(v, str) and len(v) > 3), msg)
        except (json.JSONDecodeError, TypeError):
            inner = msg[1:msg.find('}')]
            m = re.match(r'^"[^"]*?"\s*:\s*"(.+)"$', inner)
            if m:
                msg = m.group(1)
            elif len(inner.strip().strip('"\'')) > 3:
                msg = inner.strip().strip('"\'')

    # Strip wrapping quotes
    for _ in range(3):
        msg = msg.strip()
        if len(msg) >= 2 and msg[0] in '"\'':
            if msg[-1] == msg[0]:
                msg = msg[1:-1]
                continue
        break

    # Clean garbage
    msg = msg.replace('\\n', ' ').replace('\\t', ' ')
    msg = _CJK_RE.sub('', msg)
    msg = _META_RE.sub('', msg)
    msg = re.sub(r'```\w*\s*|\s*```', '', msg)
    msg = re.sub(r'\*\*([^*]+)\*\*', r'\1', msg)

    # Keep first Vietnamese/emoji line only
    for line in (l.strip() for l in msg.split('\n') if l.strip()):
        if _VN_RE.search(line) or _EMOJI_RE.search(line):
            msg = line; break

    # Final cleanup
    msg = re.sub(r'\s+', ' ', msg).strip()
    msg = re.sub(r'[{}\[\]<>]+', '', msg).strip().strip('"\'')
    return msg

# ── Fallback (no LLM) ──
_FALLBACK_RULES = [
    (["lương", "thưởng"],                           "💼🎉 Lương về rồi! Tuyệt vời!"),
    (["mẹ", "ba", "cha", "cho", "tặng"],            "💰❤️ Tiền vào rồi! Tốt lắm!"),
    (["ăn", "sáng", "trưa", "tối", "bún", "phở", "cơm", "bánh"], None),  # uses time_emoji
    (["cafe", "cà phê", "trà sữa", "trà", "nước"],  "☕ Uống gì ngon lắm đấy!"),
    (["grab", "xe", "taxi", "di chuyển"],            "🚗 Di chuyển an toàn nhé!"),
    (["mua", "shop", "quần áo", "đồ"],              "🛍️ Mua sắm vui vẻ nhé!"),
    (["phim", "game", "giải trí", "hát"],            "🎬 Giải trí vui nhé!"),
    (["điện", "nước", "wifi", "tiền nhà"],           "✅ Tiện ích đã thanh toán!"),
]

def _fallback(amount: int, text: str) -> str:
    low = text.lower()
    _, emoji = _time_info()
    for keywords, msg in _FALLBACK_RULES:
        if any(w in low for w in keywords):
            return msg if msg else f"{emoji} Ăn uống ngon miệng nhé!"
    return f"✅ Xong rồi nhé! {amount:,}đ"

# ── Main generator ──
_SYSTEM = "Bạn là chatbot tiếng Việt. CHỈ trả lời ĐÚNG 1 câu tiếng Việt ngắn gọn với emoji. KHÔNG JSON. KHÔNG giải thích. KHÔNG tiếng Trung/Anh."

_PROMPT = """Giao dịch: {tx_list}
Input gốc: "{text}"
Thời điểm: {period}

Viết 1 câu THÂN THIỆN, NGẮN GỌN bằng tiếng Việt với emoji phù hợp.
Ví dụ: "☕🌅 Sáng nay nhấm nháp cà phê thơm ngon!" / "💰❤️ Mẹ cho tiền rồi!"
CHỈ 1 câu. KHÔNG giải thích thêm.

Câu trả lời:"""


def generate_conversation_message(
    amount: int,
    transactions: Optional[List[Dict[str, Any]]] = None,
    original_text: str = ""
) -> str:
    """Generate a friendly, context-aware message for transaction confirmation."""
    llm = get_llm_service()
    if not llm.is_available():
        return _fallback(amount, original_text)

    try:
        # Build compact tx summary
        if transactions:
            tx_list = ", ".join(
                f"{tx.get('note','').strip()} ({tx.get('amount',0):,}đ - {tx.get('category','Khác')})"
                for tx in transactions
            )
        else:
            tx_list = f"{original_text} ({amount:,}đ)"

        period, _ = _time_info()
        prompt = _PROMPT.format(tx_list=tx_list, text=original_text, period=period)

        response = llm.get_prediction(
            system_prompt=_SYSTEM,
            user_prompt=prompt,
            temperature=0.7,
            max_tokens=60,
            json_mode=False
        )

        message = _clean(response)

        # Validate: must have Vietnamese chars, emoji, or at least latin text
        if not message or len(message) < 5 or not (_VN_RE.search(message) or _EMOJI_RE.search(message) or re.search(r'[a-zA-Z]', message)):
            logger.warning(f"Invalid LLM message: '{message}', fallback")
            return _fallback(amount, original_text)

        # Smart truncate at sentence boundary
        if len(message) > 120:
            cut = max(message.rfind('!', 0, 120), message.rfind('.', 0, 120), message.rfind('?', 0, 120))
            message = message[:cut + 1] if cut > 20 else message[:117] + "..."

        logger.info(f"Conversation message: '{message}'")
        return message

    except (LLMServiceError, Exception) as e:
        logger.error(f"Conversation error: {e}")
        return _fallback(amount, original_text)


__all__ = ["generate_conversation_message"]
