@echo off
REM ========================================
REM KLTN_UIT_BE - Start FastAPI Backend
REM ========================================

echo [INFO] Starting FastAPI backend server...
echo.

cd /d %~dp0..

REM Activate virtual environment if exists
if exist "venv\Scripts\activate.bat" (
    echo [INFO] Activating virtual environment...
    call venv\Scripts\activate.bat
)

echo [INFO] Starting uvicorn server on http://0.0.0.0:8000
echo.

py -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
