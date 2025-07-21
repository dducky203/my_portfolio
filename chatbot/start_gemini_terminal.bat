@echo off
echo ====================================
echo   AI Portfolio Chatbot - Terminal Mode
echo   Powered by Google Gemini AI
echo ====================================
echo.

call venv\Scripts\activate.bat
echo Luu y: Dam bao da cau hinh GEMINI_API_KEY trong file .env
echo.
python -c "from gemini_chatbot import GeminiPortfolioChatbot; bot = GeminiPortfolioChatbot(); print('🤖 AI Chatbot khoi dong thanh cong!'); print('Gõ quit để thoát\n'); import sys; [print('Bot:', bot.chat(input('Bạn: '))['response'], '\n') if (user_input := input('Bạn: ').strip()) and user_input.lower() not in ['quit', 'exit'] else sys.exit('Bot: Tạm biệt! 👋') for _ in iter(int, 1)]"

pause
