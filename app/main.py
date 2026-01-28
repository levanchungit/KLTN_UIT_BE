"""
KLTN_UIT_BE - AI Backend for Transaction Classification
Main FastAPI Application Entry Point

FastAPI + llama.cpp Integration
Architecture:
    React Native → POST /predict → FastAPI → llama.cpp /v1/chat/completions → JSON
"""
import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import load_config, get_settings
from app.routes.predict import router as predict_router
from app.services.llm_service import close_llm_service
# =====================
# Logging Configuration
# =====================
def setup_logging():
    """Configure logging for the application"""
    settings = get_settings()
    
    logging.basicConfig(
        level=getattr(logging, settings.logging.level.upper()),
        format=settings.logging.format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Reduce log noise from some libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
# =====================
# Lifespan Manager
# =====================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager
    Handles startup and shutdown events
    """
    # Startup
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting KLTN_UIT_BE AI Backend...")
    
    # Load configuration
    config = load_config()
    logger.info(f"Configuration loaded: LLM URL = {config.llm.base_url}")
    
    # Log startup complete
    logger.info("KLTN_UIT_BE AI Backend started successfully")
    
    yield
    
    # Shutdown
    logger = logging.getLogger(__name__)
    logger.info("Shutting down KLTN_UIT_BE AI Backend...")
    
    # Close LLM service
    close_llm_service()
    
    logger.info("KLTN_UIT_BE AI Backend shutdown complete")
# =====================
# FastAPI Application
# =====================
def create_app() -> FastAPI:
    """
    Create and configure FastAPI application
    
    Returns:
        Configured FastAPI application instance
    """
    settings = get_settings()
    
    app = FastAPI(
        title="KLTN_UIT_BE - AI Transaction Classification",
        description="""
        ## AI Backend for Transaction Classification
        
        This API extracts transaction information (amount, category, type) 
        from Vietnamese text descriptions using local LLM (llama.cpp).
        
        ### Features:
        - **Vietnamese Text Processing**: Understands Vietnamese transaction descriptions
        - **Local LLM**: Runs Qwen/Gemma locally via llama.cpp
        - **JSON Output**: Returns structured transaction data
        - **Category Validation**: Ensures categories are from valid list
        
        ### Architecture:
        ```
        React Native → POST /predict → FastAPI → llama.cpp → JSON
        ```
        """,
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.server.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    app.include_router(predict_router)
    
    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "name": "KLTN_UIT_BE - AI Transaction Classification",
            "version": "1.0.0",
            "docs": "/docs",
            "health": "/api/v1/health"
        }
    
    return app
# Create application instance
app = create_app()
# =====================
# Entry Point
# =====================
if __name__ == "__main__":
    import uvicorn
    
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.debug,
        log_level=settings.logging.level.lower()
    )
