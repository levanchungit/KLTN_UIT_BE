"""
KLTN_UIT_BE Configuration Module
Load configuration from config.yaml and environment variables
"""
import os
from pathlib import Path
from typing import List, Optional

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


# =====================
# Configuration Models
# =====================

class LLMConfig(BaseModel):
    """LLM Server Configuration (llama.cpp)"""
    base_url: str = "http://127.0.0.1:8080"
    api_key: str = "no-key-required"
    model: str = "gemma-2-9b-it-Q4_K_M.gguf"
    temperature: float = 0.0
    max_tokens: int = 512
    timeout: int = 60


class ServerConfig(BaseModel):
    """FastAPI Server Configuration"""
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    cors_origins: List[str] = Field(default_factory=lambda: [
        "http://localhost:8081",
        "http://localhost:3000",
        "exp://localhost:8081"
    ])


class AppConfig(BaseModel):
    """Application Configuration"""
    default_categories: List[str] = Field(default_factory=lambda: [
        "Quà tặng", "Lương", "Ăn uống", "Mượn tiền", "Chuyển khoản",
        "Mua sắm", "Di chuyển", "Giải trí", "Sức khỏe", "Hóa đơn",
        "Giáo dục", "Khác"
    ])
    transaction_types: List[str] = Field(default_factory=lambda: [
        "Thu nhập", "Chi phí", "Chuyển khoản"
    ])
    supported_locales: List[str] = Field(default_factory=lambda: ["vi-VN"])
    default_currency: str = "VND"


class ValidationConfig(BaseModel):
    """Validation Configuration"""
    min_amount: int = 0
    max_amount: int = 10_000_000_000  # 10 tỷ VND
    confidence_min: float = 0.0
    confidence_max: float = 1.0


class LoggingConfig(BaseModel):
    """Logging Configuration"""
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class Settings(BaseModel):
    """Main Settings Class"""
    llm: LLMConfig = Field(default_factory=LLMConfig)
    server: ServerConfig = Field(default_factory=ServerConfig)
    app: AppConfig = Field(default_factory=AppConfig)
    validation: ValidationConfig = Field(default_factory=ValidationConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)


# =====================
# Configuration Loader
# =====================

_config: Optional[Settings] = None


def load_config(config_path: Optional[str] = None) -> Settings:
    """
    Load configuration from YAML file
    
    Args:
        config_path: Path to config.yaml file. If None, looks for config.yaml
                    in the project root directory.
    
    Returns:
        Settings object with loaded configuration
    """
    global _config
    
    if _config is not None:
        return _config
    
    # Determine config file path
    if config_path is None:
        # Look for config.yaml in project root
        project_root = Path(__file__).parent.parent
        config_path = project_root / "config.yaml"
    else:
        config_path = Path(config_path)
    
    # Load from YAML if exists
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config_data = yaml.safe_load(f) or {}
        
        # Create settings with loaded data
        _config = Settings(**config_data)
    else:
        # Use defaults
        _config = Settings()
    
    # Override with environment variables if set
    _config = _apply_env_overrides(_config)
    
    return _config


def _apply_env_overrides(settings: Settings) -> Settings:
    """Apply environment variable overrides to settings"""
    
    # LLM settings
    if os.getenv("LLM_BASE_URL"):
        settings.llm.base_url = os.getenv("LLM_BASE_URL")
    if os.getenv("LLM_MODEL"):
        settings.llm.model = os.getenv("LLM_MODEL")
    if os.getenv("LLM_TEMPERATURE"):
        settings.llm.temperature = float(os.getenv("LLM_TEMPERATURE"))
    
    # Server settings
    if os.getenv("SERVER_HOST"):
        settings.server.host = os.getenv("SERVER_HOST")
    if os.getenv("SERVER_PORT"):
        settings.server.port = int(os.getenv("SERVER_PORT"))
    if os.getenv("SERVER_DEBUG"):
        settings.server.debug = os.getenv("SERVER_DEBUG").lower() == "true"
    
    return settings


def get_settings() -> Settings:
    """Get current settings, loading if necessary"""
    global _config
    if _config is None:
        return load_config()
    return _config


def reset_config():
    """Reset configuration (useful for testing)"""
    global _config
    _config = None
