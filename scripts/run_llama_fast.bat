@echo off
REM ========================================
REM KLTN_UIT_BE - FASTEST llama.cpp Server
REM Uses smaller model (0.5B) for maximum speed
REM Trade-off: ~85% accuracy vs ~92% with 1.5B
REM ========================================

echo [INFO] Starting llama-server with FAST mode (0.5B model)...
echo.

REM Configuration - Smaller model for speed
set MODEL_PATH=qwen2.5-0.5b-instruct-q4_0.gguf
set PORT=8080
set CONTEXT_SIZE=512
set GPU_LAYERS=99
set CPU_THREADS=8
set BATCH_SIZE=256

REM Check if model exists
if not exist "%MODEL_PATH%" (
    echo [ERROR] Model not found: %MODEL_PATH%
    echo [INFO] Download from: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF
    pause
    exit /b 1
)

echo [CONFIG] Model: %MODEL_PATH% (FAST - 0.5B)
echo [CONFIG] Port: %PORT%
echo [CONFIG] Context: %CONTEXT_SIZE%
echo [CONFIG] GPU Layers: %GPU_LAYERS%
echo.
echo [WARNING] Using smaller model - accuracy ~85%% vs 92%% with 1.5B
echo.

REM Run llama-server with speed optimizations
llama-server ^
    -m %MODEL_PATH% ^
    -c %CONTEXT_SIZE% ^
    -ngl %GPU_LAYERS% ^
    -t %CPU_THREADS% ^
    -b %BATCH_SIZE% ^
    --flash-attn ^
    --cont-batching ^
    --cache-prompt ^
    --host 0.0.0.0 ^
    --port %PORT%

pause
