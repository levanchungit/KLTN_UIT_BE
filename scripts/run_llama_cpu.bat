@echo off
REM ========================================
REM KLTN_UIT_BE - Optimized llama.cpp Server (CPU Only)
REM For systems without NVIDIA GPU
REM ========================================

echo [INFO] Starting llama-server with CPU optimization...
echo.

REM Configuration
set MODEL_PATH=qwen2.5-1.5b-instruct-q4_0.gguf
set PORT=8080
set CONTEXT_SIZE=1024
set CPU_THREADS=12
set BATCH_SIZE=512

REM Check if model exists
if not exist "%MODEL_PATH%" (
    echo [ERROR] Model not found: %MODEL_PATH%
    echo [INFO] Please download the model first or update MODEL_PATH
    pause
    exit /b 1
)

echo [CONFIG] Model: %MODEL_PATH%
echo [CONFIG] Port: %PORT%
echo [CONFIG] Context: %CONTEXT_SIZE%
echo [CONFIG] CPU Threads: %CPU_THREADS%
echo [CONFIG] Batch Size: %BATCH_SIZE%
echo.

REM Run llama-server with CPU optimizations
llama-server ^
    -m %MODEL_PATH% ^
    -c %CONTEXT_SIZE% ^
    -t %CPU_THREADS% ^
    -b %BATCH_SIZE% ^
    --cont-batching ^
    --cache-prompt ^
    --mlock ^
    --host 0.0.0.0 ^
    --port %PORT%

pause
