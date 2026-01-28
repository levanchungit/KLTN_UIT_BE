"""
KLTN_UIT_BE Test Suite
Unit tests for preprocessing module
"""
import pytest
from app.services.preprocessing import (
    normalize_text,
    extract_keywords,
    detect_transaction_type,
    extract_amount_from_text,
    preprocess_transaction
)
class TestNormalizeText:
    """Tests for text normalization"""
    def test_strip_whitespace(self):
        assert normalize_text("  hello world  ") == "hello world"
    def test_multiple_spaces(self):
        assert normalize_text("hello    world") == "hello world"
    def test_normalize_number_abbreviations_1tr(self):
        result = normalize_text("Mẹ cho 1tr")
        assert "1000000" in result or "1.000.000" in result
    def test_normalize_number_abbreviations_200k(self):
        result = normalize_text("Mua cà phê 200k")
        assert "200000" in result or "200.000" in result
    def test_normalize_number_abbreviations_triệu(self):
        result = normalize_text("Lương 5 triệu")
        assert "5000000" in result or "5.000.000" in result
class TestDetectTransactionType:
    """Tests for transaction type detection"""
    def test_income_from_lương(self):
        assert detect_transaction_type("Nhận lương tháng") == "Thu nhập"
    def test_income_from_quà(self):
        assert detect_transaction_type("Mẹ cho tiền") == "Thu nhập"
    def test_income_from_bonus(self):
        assert detect_transaction_type("Thưởng cuối năm") == "Thu nhập"
    def test_expense_from_mua(self):
        assert detect_transaction_type("Mua áo 200k") == "Chi tiêu"
    def test_expense_from_cà_phê(self):
        assert detect_transaction_type("Uống cà phê 50k") == "Chi tiêu"
    def test_expense_from_hóa_đơn(self):
        assert detect_transaction_type("Tiền điện 500k") == "Chi tiêu"
    def test_transfer(self):
        assert detect_transaction_type("Chuyển khoản cho bạn") == "Chuyển khoản"
    def test_transfer_vietqr(self):
        assert detect_transaction_type("Thanh toán VietQR") == "Chuyển khoản"
class TestExtractAmountFromText:
    """Tests for amount extraction"""
    def test_extract_tr(self):
        amount = extract_amount_from_text("Mẹ cho 1tr")
        assert amount == 1000000
    def test_extract_k(self):
        amount = extract_amount_from_text("Mua cà phê 200k")
        assert amount == 200000
    def test_extract_vnd_format(self):
        amount = extract_amount_from_text("Tiền 500.000 đ")
        assert amount == 500000
    def test_extract_triệu(self):
        amount = extract_amount_from_text("Lương 5 triệu")
        assert amount == 5000000
    def test_no_amount(self):
        amount = extract_amount_from_text("Mẹ cho tiền")
        assert amount is None
class TestExtractKeywords:
    """Tests for keyword extraction"""
    def test_extract_money_in_keywords(self):
        keywords = extract_keywords("Mẹ cho 1tr")
        assert len(keywords["money_in"]) > 0
    def test_extract_money_out_keywords(self):
        keywords = extract_keywords("Mua cà phê 50k")
        assert len(keywords["money_out"]) > 0
    def test_extract_person_keywords(self):
        keywords = extract_keywords("Mẹ cho 1tr")
        assert len(keywords["persons"]) > 0
class TestPreprocessTransaction:
    """Tests for complete preprocessing pipeline"""
    def test_preprocess_complete(self):
        text, trans_type, amount = preprocess_transaction("Mẹ cho 1tr")
        assert trans_type == "Thu nhập"
        assert amount == 1000000
    def test_preprocess_expense(self):
        text, trans_type, amount = preprocess_transaction("Mua cà phê 50k")
        assert trans_type == "Chi tiêu"
        assert amount == 50000
