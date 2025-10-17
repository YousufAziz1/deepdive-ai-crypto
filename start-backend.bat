@echo off
echo ========================================
echo  DeepDive AI - Starting Backend Server
echo ========================================
echo.

cd backend

if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

echo Activating virtual environment...
call venv\Scripts\activate

if not exist ".env" (
    echo WARNING: .env file not found!
    echo Please copy .env.example to .env and add your API keys
    pause
    exit
)

echo Installing/updating dependencies...
pip install -q -r requirements.txt

echo.
echo Starting FastAPI server...
echo Server will run at: http://localhost:8000
echo API docs available at: http://localhost:8000/docs
echo.

python main.py
