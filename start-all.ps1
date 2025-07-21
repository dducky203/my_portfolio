# PowerShell script để khởi động cả Portfolio và Chatbot
Write-Host "=====================================" -ForegroundColor Green
Write-Host "   Portfolio + Chatbot Auto Start" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green
Write-Host ""

Write-Host "Khởi động cả Web Portfolio và AI Chatbot..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Web Portfolio: http://localhost:5173" -ForegroundColor Cyan
Write-Host "AI Chatbot: http://localhost:5000" -ForegroundColor Cyan
Write-Host ""

# Khởi động cả hai service
npm run start:all

Read-Host "Nhấn Enter để thoát..."