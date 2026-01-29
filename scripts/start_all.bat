@echo off
REM ========================================
REM KLTN_UIT_BE - Start All Services
REM Starts both llama-server and FastAPI backend
REM ========================================

echo ========================================
echo   KLTN_UIT_BE - Transaction Classifier
echo ========================================
echo.

REM Check for GPU
nvidia-smi >nul 2>&1
if %errorlevel%==0 (
    echo [INFO] NVIDIA GPU detected - using GPU mode
    set LLAMA_SCRIPT=run_llama_gpu.bat
) else (
    echo [INFO] No NVIDIA GPU - using CPU mode
    set LLAMA_SCRIPT=run_llama_cpu.bat
)

echo.
echo [STEP 1] Starting llama-server in new window...
start "llama-server" cmd /k "%~dp0%LLAMA_SCRIPT%"

echo [INFO] Waiting 5 seconds for llama-server to start...
timeout /t 5 /nobreak >nul

echo.
echo [STEP 2] Starting FastAPI backend in new window...
start "FastAPI Backend" cmd /k "%~dp0run_backend.bat"

echo.
echo ========================================
echo   Services Started:
echo   - llama-server: http://localhost:8080
echo   - FastAPI:      http://localhost:8000
echo   - API Docs:     http://localhost:8000/docs
echo   - Health:       http://localhost:8000/api/v1/health
echo ========================================
echo.
echo Press any key to exit this window (services will keep running)
pause >nul
