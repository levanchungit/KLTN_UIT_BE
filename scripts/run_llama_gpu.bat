@echo off
REM ========================================
REM KLTN_UIT_BE - Optimized llama.cpp Server (GPU)
REM Requires: NVIDIA GPU with CUDA support
REM ========================================

echo [INFO] Starting llama-server with GPU optimization...
echo.

REM Configuration
set MODEL_PATH=qwen2.5-1.5b-instruct-q4_0.gguf
set PORT=8080
set CONTEXT_SIZE=1024
set GPU_LAYERS=99
set CPU_THREADS=8
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
echo [CONFIG] GPU Layers: %GPU_LAYERS% (all)
echo [CONFIG] CPU Threads: %CPU_THREADS%
echo [CONFIG] Batch Size: %BATCH_SIZE%
echo.

REM Run llama-server with GPU optimizations
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
