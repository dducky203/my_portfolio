#!/usr/bin/env python3
"""
Chạy chatbot trong terminal
"""

import sys
import os

# Thêm thư mục hiện tại vào Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chatbot import PortfolioChatbot

def main():
    """Hàm chính để chạy chatbot trong terminal"""
    print("=" * 60)
    print("🤖 PORTFOLIO CHATBOT - LÊ NGỌC DƯƠNG")
    print("=" * 60)
    print("Chatbot có thể trả lời các câu hỏi về:")
    print("• Thông tin cá nhân và kinh nghiệm")
    print("• Kỹ năng lập trình và công nghệ")
    print("• Dự án đã thực hiện")
    print("• Thông tin liên hệ")
    print()
    print("Gõ 'quit' để thoát, 'help' để xem hướng dẫn")
    print("=" * 60)
    print()
    
    # Khởi tạo chatbot
    bot = PortfolioChatbot()
    
    # Hiển thị lời chào
    greeting_result = bot.chat("xin chào")
    print("🤖 Bot:", greeting_result['response'])
    print()
    
    # Vòng lặp chat chính
    while True:
        try:
            # Nhận input từ user
            user_input = input("👤 Bạn: ").strip()
            
            # Kiểm tra lệnh thoát
            if user_input.lower() in ['quit', 'exit', 'thoát', 'bye', 'goodbye']:
                print("🤖 Bot: Tạm biệt! Cảm ơn bạn đã sử dụng chatbot! 👋")
                print("Hẹn gặp lại! 😊")
                break
            
            # Kiểm tra lệnh help
            elif user_input.lower() in ['help', 'hướng dẫn', '?']:
                print("🤖 Bot:", bot.get_help())
                print()
                continue
            
            # Kiểm tra input rỗng
            elif not user_input:
                print("🤖 Bot: Bạn chưa nhập gì cả. Hãy hỏi tôi điều gì đó! 😄")
                print()
                continue
            
            # Xử lý tin nhắn
            result = bot.chat(user_input)
            print(f"🤖 Bot: {result['response']}")
            print()
            
        except KeyboardInterrupt:
            print("\n\n🤖 Bot: Đã nhận tín hiệu dừng. Tạm biệt! 👋")
            break
        except Exception as e:
            print(f"❌ Lỗi: {str(e)}")
            print("Vui lòng thử lại!")
            print()

if __name__ == "__main__":
    main()
