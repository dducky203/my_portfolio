@echo off
echo ====================================
echo   AI Portfolio Chatbot Setup
echo   Powered by Google Gemini AI
echo ====================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python khong duoc cai dat hoac khong co trong PATH!
    echo Vui long cai dat Python tu: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Checking requirements.txt...
if not exist requirements.txt (
    echo Error: File requirements.txt khong ton tai!
    echo Vui long dam bao file requirements.txt co trong thu muc hien tai.
    pause
    exit /b 1
)

echo [1/4] Tao virtual environment...
if exist venv (
    echo Virtual environment da ton tai, dang xoa...
    rmdir /s /q venv
)
python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo Error: Khong the tao virtual environment!
    echo Chi tiet loi: %ERRORLEVEL%
    pause
    exit /b 1
)

echo [2/4] Kich hoat virtual environment...
if not exist venv\Scripts\activate.bat (
    echo Error: Virtual environment khong duoc tao dung cach!
    pause
    exit /b 1
)
call venv\Scripts\activate.bat

echo [3/4] Cai dat dependencies...
echo Dang cai dat cac package can thiet...
pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Khong the cai dat dependencies!
    echo Chi tiet loi: %ERRORLEVEL%
    echo.
    echo Dang thu cai dat tung package rieng le...
    pip install streamlit
    pip install google-generativeai
    pip install python-dotenv
    if %ERRORLEVEL% NEQ 0 (
        echo Error: Van khong the cai dat dependencies!
        pause
        exit /b 1
    )
)

echo [4/4] Tao file .env...
if not exist .env (
    if exist .env.example (
        copy .env.example .env
        echo File .env da duoc tao tu .env.example
    ) else (
        echo GEMINI_API_KEY=your_gemini_api_key_here > .env
        echo File .env da duoc tao
    )
) else (
    echo File .env da ton tai
)

echo.
echo ====================================
echo   Setup hoan tat!
echo ====================================
echo.
echo QUAN TRONG: Vui long cau hinh API key:
echo 1. Mo file .env
echo 2. Lay API key tu: https://makersuite.google.com/app/apikey  
echo 3. Thay the "your_gemini_api_key_here" bang API key that
echo.
echo Cach su dung:
echo 1. Chay web interface: start_web.bat
echo 2. Chay terminal mode: start_terminal.bat
echo.
pause
