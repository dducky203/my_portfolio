import re
import random
from data import (
    PERSONAL_INFO, SKILLS, PROJECTS, STATS, CONTACT_INFO, 
    QUESTION_PATTERNS, RESPONSES
)

class PortfolioChatbot:
    def __init__(self):
        self.conversation_history = []
        
    def preprocess_message(self, message):
        """Tiền xử lý tin nhắn: chuyển về chữ thường, loại bỏ dấu câu"""
        message = message.lower().strip()
        # Loại bỏ dấu câu
        message = re.sub(r'[^\w\s]', '', message)
        return message
    
    def detect_intent(self, message):
        """Nhận diện ý định của câu hỏi"""
        processed_message = self.preprocess_message(message)
        
        # Kiểm tra các pattern
        for intent, patterns in QUESTION_PATTERNS.items():
            for pattern in patterns:
                if pattern.lower() in processed_message:
                    return intent
        
        # Kiểm tra greeting
        greetings = ["xin chào", "chào", "hello", "hi", "hey"]
        if any(greeting in processed_message for greeting in greetings):
            return "greeting"
            
        return "unknown"
    
    def generate_response(self, intent, message=""):
        """Tạo phản hồi dựa trên ý định"""
        
        if intent == "greeting":
            return random.choice(RESPONSES["greeting"])
        
        elif intent == "name":
            return f"Tôi đại diện cho {PERSONAL_INFO['name']} (tên tiếng Anh: {PERSONAL_INFO['english_name']}). Anh ấy là một {PERSONAL_INFO['title']}."
        
        elif intent == "experience":
            return f"{PERSONAL_INFO['name']} có {PERSONAL_INFO['experience_years']} năm kinh nghiệm trong lĩnh vực phát triển web. {PERSONAL_INFO['description']}"
        
        elif intent == "skills":
            skills_text = f"{PERSONAL_INFO['name']} có các kỹ năng sau:\n\n"
            skills_text += "🎨 **Frontend:**\n"
            for skill, level in SKILLS['frontend'].items():
                skills_text += f"• {skill}: {level}%\n"
            
            skills_text += "\n💻 **Backend:**\n"
            for skill, level in SKILLS['backend'].items():
                skills_text += f"• {skill}: {level}%\n"
                
            skills_text += "\n🛠️ **Tools & Others:**\n"
            for skill, level in SKILLS['tools'].items():
                skills_text += f"• {skill}: {level}%\n"
                
            skills_text += f"\n✨ **Chuyên môn:** {', '.join(SKILLS['specialties'])}"
            return skills_text
        
        elif intent == "projects":
            projects_text = f"{PERSONAL_INFO['name']} đã thực hiện các dự án sau:\n\n"
            for i, project in enumerate(PROJECTS, 1):
                projects_text += f"**{i}. {project['title']}**\n"
                projects_text += f"📝 {project['description']}\n"
                projects_text += f"🔧 Công nghệ: {', '.join(project['technologies'])}\n\n"
            return projects_text
        
        elif intent == "contact":
            contact_text = f"Thông tin liên hệ với {PERSONAL_INFO['name']}:\n\n"
            contact_text += f"📧 Email: {CONTACT_INFO['email']}\n"
            contact_text += f"📞 Phone: {CONTACT_INFO.get('phone', 'N/A')}\n"
            contact_text += f"📍 Vị trí: {CONTACT_INFO['location']}\n"
            # Thêm mạng xã hội nếu có
            if CONTACT_INFO.get('linkedin'):
                contact_text += f"🔗 LinkedIn: {CONTACT_INFO['linkedin']}\n"
            if CONTACT_INFO.get('facebook'):
                contact_text += f"📘 Facebook: {CONTACT_INFO['facebook']}\n"
            contact_text += f"🐙 GitHub: {CONTACT_INFO.get('github', 'N/A')}\n"
            contact_text += f"💼 {CONTACT_INFO['availability']}\n"
            contact_text += f"📄 CV: {CONTACT_INFO['cv']}"
            return contact_text
        
        elif intent == "description":
            desc_text = f"Về {PERSONAL_INFO['name']}:\n\n"
            desc_text += f"👨‍💻 {PERSONAL_INFO['description']}\n\n"
            desc_text += f"🎯 Mục tiêu: {PERSONAL_INFO['goal']}\n\n"
            desc_text += f"❤️ {PERSONAL_INFO['passion']}"
            return desc_text
        
        elif intent == "stats":
            stats_text = f"Thống kê nghề nghiệp của {PERSONAL_INFO['name']}:\n\n"
            stats_text += f"🚀 Dự án hoàn thành: {STATS['projects_completed']}\n"
            stats_text += f"⏰ Năm kinh nghiệm: {STATS['years_experience']}\n"
            stats_text += f"😊 Khách hàng hài lòng: {STATS['happy_clients']}"
            return stats_text
        
        else:
            return random.choice(RESPONSES["unknown"])
    
    def chat(self, message):
        """Xử lý tin nhắn chat chính"""
        # Lưu lịch sử hội thoại
        self.conversation_history.append({"user": message, "timestamp": "now"})
        
        # Nhận diện ý định
        intent = self.detect_intent(message)
        
        # Tạo phản hồi
        response = self.generate_response(intent, message)
        
        # Lưu phản hồi vào lịch sử
        self.conversation_history.append({"bot": response, "timestamp": "now"})
        
        return {
            "response": response,
            "intent": intent,
            "message_count": len(self.conversation_history)
        }
    
    def get_help(self):
        """Trả về hướng dẫn sử dụng"""
        help_text = """
🤖 **Hướng dẫn sử dụng Chatbot**

Tôi có thể trả lời các câu hỏi về Lê Ngọc Dương:

📋 **Các chủ đề có thể hỏi:**
• Thông tin cá nhân (tên, giới thiệu)
• Kinh nghiệm làm việc  
• Kỹ năng lập trình
• Dự án đã thực hiện
• Thông tin liên hệ
• Thống kê nghề nghiệp

💬 **Ví dụ câu hỏi:**
• "Bạn tên gì?"
• "Bạn có bao nhiêu năm kinh nghiệm?"
• "Bạn biết những kỹ năng gì?"
• "Dự án nào bạn đã làm?"
• "Làm sao để liên hệ?"

Hãy thử hỏi tôi nhé! 😊
        """
        return help_text

# Test chatbot
if __name__ == "__main__":
    bot = PortfolioChatbot()
    
    print("🤖 Portfolio Chatbot khởi động!")
    print("Gõ 'quit' để thoát, 'help' để xem hướng dẫn\n")
    
    while True:
        user_input = input("Bạn: ")
        
        if user_input.lower() in ['quit', 'exit', 'thoát']:
            print("Bot: Tạm biệt! Hẹn gặp lại! 👋")
            break
        elif user_input.lower() in ['help', 'hướng dẫn']:
            print("Bot:", bot.get_help())
        else:
            result = bot.chat(user_input)
            print("Bot:", result['response'])
            print()
