# PowerShell script để khởi động chatbot
Write-Host "=====================================" -ForegroundColor Green
Write-Host "   AI Portfolio Chatbot - Web Interface" -ForegroundColor Green
Write-Host "   Powered by Google Gemini AI" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green
Write-Host ""

# Chuyển đến thư mục chatbot
Set-Location -Path ".\chatbot"

# Kiểm tra xem virtual environment có tồn tại không
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    Write-Host "Khởi động virtual environment..." -ForegroundColor Yellow
    & ".\venv\Scripts\Activate.ps1"
    
    Write-Host "Khởi động AI chatbot server..." -ForegroundColor Yellow
    Write-Host "Truy cập: http://localhost:5000" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Lưu ý: Đảm bảo đã cấu hình GEMINI_API_KEY trong file .env" -ForegroundColor Red
    Write-Host ""
    
    # Set encoding to UTF-8 for Python
    $env:PYTHONIOENCODING = "utf-8"
    
    # Khởi động chatbot
    python gemini_app.py
} else {
    Write-Host "Lỗi: Không tìm thấy virtual environment tại .\venv\" -ForegroundColor Red
    Write-Host "Vui lòng chạy setup.bat trước để cài đặt môi trường" -ForegroundColor Red
    Write-Host "Hoặc chuyển sang thư mục chatbot và chạy: python -m venv venv" -ForegroundColor Yellow
    Write-Host "Sau đó: .\venv\Scripts\activate && pip install -r requirements.txt" -ForegroundColor Yellow
    pause
}
