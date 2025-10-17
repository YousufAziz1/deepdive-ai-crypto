@echo off
echo ========================================
echo  DeepDive AI - Starting Frontend
echo ========================================
echo.

cd frontend

if not exist "node_modules\" (
    echo Installing dependencies...
    echo This may take a few minutes...
    call npm install
    echo.
)

echo Starting development server...
echo Frontend will run at: http://localhost:3000
echo.

call npm run dev
