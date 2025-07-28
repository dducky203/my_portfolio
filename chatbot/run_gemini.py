#!/usr/bin/env python3
"""
Chạy Gemini chatbot trong terminal
"""

import sys
import os

# Thêm thư mục hiện tại vào Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gemini_chatbot import GeminiPortfolioChatbot

def main():
    """Hàm chính để chạy Gemini chatbot trong terminal"""
    print("=" * 60)
    print("🤖 AI PORTFOLIO CHATBOT - LÊ NGỌC DƯƠNG")
    print("🚀 Powered by Google Gemini AI")
    print("=" * 60)
    print("Chatbot AI có thể trả lời mọi câu hỏi về:")
    print("• Thông tin cá nhân và kinh nghiệm")
    print("• Kỹ năng lập trình và công nghệ")
    print("• Dự án đã thực hiện")
    print("• Thông tin liên hệ")
    print("• Và nhiều câu hỏi khác...")
    print()
    print("Gõ 'quit' để thoát, 'help' để xem hướng dẫn")
    print("=" * 60)
    print()
    
    # Khởi tạo Gemini chatbot
    try:
        bot = GeminiPortfolioChatbot()
        print("✅ Gemini AI đã sẵn sàng!")
        print()
    except Exception as e:
        print(f"❌ Lỗi khởi tạo Gemini AI: {e}")
        print("Vui lòng kiểm tra:")
        print("1. File .env đã được tạo và cấu hình GEMINI_API_KEY")
        print("2. API key hợp lệ từ https://makersuite.google.com/app/apikey")
        print("3. Kết nối internet ổn định")
        return
    
    # Hiển thị lời chào từ AI
    greeting_result = bot.chat("xin chào")
    print("🤖 AI Bot:", greeting_result['response'])
    print()
    
    # Vòng lặp chat chính
    while True:
        try:
            # Nhận input từ user
            user_input = input("👤 Bạn: ").strip()
            
            # Kiểm tra lệnh thoát
            if user_input.lower() in ['quit', 'exit', 'thoát', 'bye', 'goodbye']:
                print("🤖 AI Bot: Tạm biệt! Cảm ơn bạn đã trò chuyện với tôi! 👋")
                print("Hẹn gặp lại! 😊")
                break
            
            # Kiểm tra lệnh help
            elif user_input.lower() in ['help', 'hướng dẫn', '?']:
                help_text = """
🤖 **Hướng dẫn sử dụng AI Chatbot**

Tôi là AI assistant thông minh của Lê Ngọc Dương, được hỗ trợ bởi Google Gemini.

💬 **Bạn có thể hỏi tôi về:**
• Thông tin cá nhân và background
• Kinh nghiệm làm việc chi tiết  
• Kỹ năng lập trình và công nghệ
• Dự án đã thực hiện
• Cách thức liên hệ và hợp tác
• Những sở thích và đam mê
• Kế hoạch tương lai

🎯 **Ví dụ câu hỏi hay:**
• "Hãy kể về quá trình học tập và làm việc của bạn"
• "Dự án nào bạn thấy thách thức nhất?"
• "Bạn thích công nghệ nào nhất và tại sao?"
• "Làm thế nào để có thể hợp tác với bạn?"

Hãy hỏi tôi bất cứ điều gì! Tôi sẽ trả lời một cách thông minh và chi tiết! 🚀
                """
                print("🤖 AI Bot:", help_text)
                print()
                continue
            
            # Kiểm tra input rỗng
            elif not user_input:
                print("🤖 AI Bot: Bạn chưa nhập gì cả. Hãy hỏi tôi điều gì đó thú vị! 😄")
                print()
                continue
            
            # Xử lý tin nhắn với AI
            print("🤖 AI Bot đang suy nghĩ...")
            result = bot.chat(user_input)
            
            if result['success']:
                print(f"🤖 AI Bot: {result['response']}")
            else:
                print(f"❌ Lỗi AI: {result.get('error', 'Không xác định')}")
                print("🤖 AI Bot: Xin lỗi, tôi gặp chút vấn đề. Vui lòng thử lại!")
            print()
            
        except KeyboardInterrupt:
            print("\n\n🤖 AI Bot: Đã nhận tín hiệu dừng. Tạm biệt! 👋")
            break
        except Exception as e:
            print(f"❌ Lỗi hệ thống: {str(e)}")
            print("Vui lòng thử lại!")
            print()

if __name__ == "__main__":
    main()
