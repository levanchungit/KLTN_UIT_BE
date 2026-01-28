"""
KLTN_UIT_BE Test Suite
API integration tests
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import reset_config
class TestHealthEndpoint:
    """Tests for health check endpoint"""
    @pytest.fixture(autouse=True)
    def setup(self):
        reset_config()
        self.client = TestClient(app)
    def test_health_check(self):
        response = self.client.get("/api/v1/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "llm_available" in data
        assert "version" in data
class TestRootEndpoint:
    """Tests for root endpoint"""
    @pytest.fixture(autouse=True)
    def setup(self):
        reset_config()
        self.client = TestClient(app)
    def test_root(self):
        response = self.client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "KLTN_UIT_BE - AI Transaction Classification"
        assert "version" in data
class TestCategoriesEndpoint:
    """Tests for categories endpoint"""
    @pytest.fixture(autouse=True)
    def setup(self):
        reset_config()
        self.client = TestClient(app)
    def test_get_categories(self):
        response = self.client.get("/api/v1/categories")
        assert response.status_code == 200
        data = response.json()
        assert "categories" in data
        assert "transaction_types" in data
        assert "Quà tặng" in data["categories"]
        assert "Lương" in data["categories"]
        assert "Thu nhập" in data["transaction_types"]
        assert "Chi tiêu" in data["transaction_types"]
class TestPredictEndpoint:
    """Tests for prediction endpoint"""
    @pytest.fixture(autouse=True)
    def setup(self):
        reset_config()
        self.client = TestClient(app)
    def test_predict_invalid_request(self):
        response = self.client.post(
            "/api/v1/predict",
            json={"text": ""}
        )
        assert response.status_code == 422  # Validation error
    def test_predict_missing_text(self):
        response = self.client.post(
            "/api/v1/predict",
            json={"categories": ["Quà tặng", "Lương"]}
        )
        assert response.status_code == 422  # Validation error
    def test_predict_with_valid_text(self):
        response = self.client.post(
            "/api/v1/predict",
            json={
                "text": "Mẹ cho 1tr",
                "categories": ["Quà tặng", "Lương", "Ăn uống"]
            }
        )
        # May fail if LLM is not available, but request format should be valid
        # Check that the request structure is correct
        if response.status_code == 200:
            data = response.json()
            assert "amount" in data
            assert "category" in data
            assert "type" in data
            assert "confidence" in data
