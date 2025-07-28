import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from data import PERSONAL_INFO, SKILLS, PROJECTS, STATS, CONTACT_INFO

# Load environment variables
load_dotenv()

class GeminiPortfolioChatbot:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY không được tìm thấy trong file .env")
        
        # Cấu hình Gemini API
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Context về thông tin cá nhân
        self.context = self._build_context()
        
        # Lịch sử hội thoại
        self.conversation_history = []
    
    def _build_context(self):
        """Xây dựng context về thông tin cá nhân"""
        context = f"""
Bạn là một chatbot thông minh đại diện cho {PERSONAL_INFO['name']} ({PERSONAL_INFO['english_name']}), một {PERSONAL_INFO['title']}.

THÔNG TIN CÁ NHÂN / PERSONAL INFORMATION:
- Tên / Name: {PERSONAL_INFO['name']} (English: {PERSONAL_INFO['english_name']})
- Nghề nghiệp / Profession: {PERSONAL_INFO['title']}
- Kinh nghiệm / Experience: {PERSONAL_INFO['experience_years']} years
- Vị trí / Location: {PERSONAL_INFO['location']}
- Mô tả (VI): {PERSONAL_INFO['description_vi']}
- Description (EN): {PERSONAL_INFO['description_en']}
- Đam mê (VI): {PERSONAL_INFO['passion_vi']}
- Passion (EN): {PERSONAL_INFO['passion_en']}
- Mục tiêu (VI): {PERSONAL_INFO['goal_vi']}
- Goal (EN): {PERSONAL_INFO['goal_en']}

KỸ NĂNG LẬP TRÌNH / PROGRAMMING SKILLS:
Frontend: {', '.join([f"{skill} ({level}%)" for skill, level in SKILLS['frontend'].items()])}
Backend: {', '.join([f"{skill} ({level}%)" for skill, level in SKILLS['backend'].items()])}
Tools: {', '.join([f"{skill} ({level}%)" for skill, level in SKILLS['tools'].items()])}
Chuyên môn / Specialties: {', '.join(SKILLS['specialties'])}

DỰ ÁN ĐÃ THỰC HIỆN / COMPLETED PROJECTS:
"""
        
        for i, project in enumerate(PROJECTS, 1):
            github_info = f"GitHub: {project.get('github_link', 'Đang cập nhật / In development')}"
            demo_info = f"Demo: {project.get('live_demo', 'Đang phát triển / In development')}"
            features_info = f"Tính năng / Features: {', '.join(project.get('features', []))}" if project.get('features') else ""
            
            context += f"""{i}. {project['title']}: 
   - Mô tả / Description: {project['description']}
   - Công nghệ / Technologies: {', '.join(project['technologies'])}
   - {github_info}
   - {demo_info}
   - {features_info}

"""
        
        context += f"""
THỐNG KÊ NGHỀ NGHIỆP:
- Dự án hoàn thành: {STATS['projects_completed']}
- Năm kinh nghiệm: {STATS['years_experience']}
- Khách hàng hài lòng: {STATS['happy_clients']}

THÔNG TIN LIÊN HỆ:
- Email: {CONTACT_INFO['email']}
- Số điện thoại: {CONTACT_INFO['phone']}
- Vị trí: {CONTACT_INFO['location']}
- GitHub: {CONTACT_INFO['github']}
- Phản hồi: {CONTACT_INFO['response_time']}
- Tình trạng: {CONTACT_INFO['availability']}
- CV: {CONTACT_INFO['cv']}

HƯỚNG DẪN TRẢ LỜI:
1. Luôn trả lời bằng tiếng Việt trừ khi được yêu cầu khác
2. Giữ giọng điệu thân thiện, chuyên nghiệp
3. Khi được hỏi về thông tin cá nhân, hãy trả lời như thể bạn chính là Lê Ngọc Dương
4. Sử dụng emoji phù hợp để làm câu trả lời sinh động
5. Nếu câu hỏi không liên quan đến thông tin portfolio, hãy lịch sự chuyển hướng về chủ đề nghề nghiệp
6. Luôn khuyến khích người dùng liên hệ nếu họ quan tâm đến hợp tác
7. Khi được hỏi về dự án, hãy bao gồm cả link GitHub và demo nếu có
8. Khi được hỏi về liên hệ, hãy cung cấp email và số điện thoại cụ thể
9. KHI CUNG CẤP LINKS: Hãy viết link đầy đủ có https:// để người dùng có thể click vào (ví dụ: GitHub: https://github.com/lnduong203/Home-Rentals)
10. Format links một cách rõ ràng và có thể click được trong giao diện chat
"""
        return context
    
    def chat(self, message, language="vi"):
        """Xử lý tin nhắn chat với Gemini"""
        try:
            # Tạo prompt với context và ngôn ngữ
            if language == "en":
                language_instruction = "Please respond in English. You are representing Duong Le Ngoc, answer as if you are him."
                prompt_template = f"{self.context}\n\n{language_instruction}\n\nUser question: {message}\n\nPlease answer this question based on the information above:"
            else:
                language_instruction = "Hãy trả lời bằng tiếng Việt. Bạn đang đại diện cho Lê Ngọc Dương, hãy trả lời như thể bạn chính là anh ấy."
                prompt_template = f"{self.context}\n\n{language_instruction}\n\nCâu hỏi của người dùng: {message}\n\nHãy trả lời câu hỏi này dựa trên thông tin trên:"
            
            # Gọi Gemini API
            response = self.model.generate_content(prompt_template)
            
            # Lưu vào lịch sử
            self.conversation_history.append({
                "user": message,
                "bot": response.text,
                "language": language,
                "timestamp": "now"
            })
            
            return {
                "response": response.text,
                "success": True,
                "language": language,
                "message_count": len(self.conversation_history)
            }
            
        except Exception as e:
            error_msg = (
                f"Sorry, I encountered a technical issue. Please try again! 😅\nError: {str(e)}" 
                if language == "en" 
                else f"Xin lỗi, tôi gặp chút vấn đề kỹ thuật. Vui lòng thử lại sau! 😅\nLỗi: {str(e)}"
            )
            return {
                "response": error_msg,
                "success": False,
                "language": language,
                "error": str(e)
            }
    
    def get_conversation_history(self):
        """Lấy lịch sử hội thoại"""
        return self.conversation_history
    
    def clear_history(self):
        """Xóa lịch sử hội thoại"""
        self.conversation_history = []
        return {"message": "Đã xóa lịch sử hội thoại"}

# Test chatbot
if __name__ == "__main__":
    try:
        bot = GeminiPortfolioChatbot()
        
        print("🤖 Gemini Portfolio Chatbot khởi động!")
        print("Gõ 'quit' để thoát\n")
        
        while True:
            user_input = input("Bạn: ")
            
            if user_input.lower() in ['quit', 'exit', 'thoát']:
                print("Bot: Tạm biệt! 👋")
                break
            
            result = bot.chat(user_input)
            print("Bot:", result['response'])
            print()
            
    except Exception as e:
        print(f"Lỗi khởi động: {e}")
        print("Vui lòng kiểm tra GEMINI_API_KEY trong file .env")
