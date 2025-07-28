@echo off
echo ====================================
echo   AI Portfolio Chatbot - Web Interface
echo   Powered by Google Gemini AI  
echo ====================================
echo.

call venv\Scripts\activate.bat
echo Khoi dong AI chatbot server...
echo Truy cap: http://localhost:5000
echo.
echo Luu y: Dam bao da cau hinh GEMINI_API_KEY trong file .env
echo.
python gemini_app.py
