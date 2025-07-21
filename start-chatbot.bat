@echo off
echo ====================================
echo   AI Portfolio Chatbot - Web Interface
echo ====================================
echo.

cd chatbot

if exist "venv\Scripts\activate.bat" (
    echo Khoi dong virtual environment...
    call venv\Scripts\activate.bat
    
    echo Khoi dong AI chatbot server...
    echo Truy cap: http://localhost:5000
    echo.
    
    set PYTHONIOENCODING=utf-8
    python gemini_app.py
) else (
    echo Loi: Khong tim thay virtual environment tai .\venv\
    echo Vui long chay setup.bat truoc de cai dat moi truong
    pause
)
