from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from chatbot import PortfolioChatbot
import os

app = Flask(__name__)
CORS(app)

# Khởi tạo chatbot
bot = PortfolioChatbot()

# HTML template cho giao diện web
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio Chatbot - Lê Ngọc Dương</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #2196F3, #21CBF3);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2em;
            margin-bottom: 10px;
        }
        
        .header p {
            opacity: 0.9;
            font-size: 1.1em;
        }
        
        .chat-container {
            height: 500px;
            overflow-y: auto;
            padding: 20px;
            background: #f8f9fa;
        }
        
        .message {
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message.bot {
            justify-content: flex-start;
        }
        
        .message-content {
            max-width: 70%;
            padding: 12px 18px;
            border-radius: 20px;
            white-space: pre-line;
        }
        
        .message.user .message-content {
            background: #2196F3;
            color: white;
            border-bottom-right-radius: 5px;
        }
        
        .message.bot .message-content {
            background: white;
            color: #333;
            border: 1px solid #e1e8ed;
            border-bottom-left-radius: 5px;
        }
        
        .input-container {
            padding: 20px;
            border-top: 1px solid #e1e8ed;
            background: white;
        }
        
        .input-group {
            display: flex;
            gap: 10px;
        }
        
        #messageInput {
            flex: 1;
            padding: 12px 18px;
            border: 2px solid #e1e8ed;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s;
        }
        
        #messageInput:focus {
            border-color: #2196F3;
        }
        
        #sendButton {
            padding: 12px 24px;
            background: #2196F3;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        
        #sendButton:hover {
            background: #1976D2;
        }
        
        #sendButton:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        
        .suggestions {
            margin-top: 15px;
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        
        .suggestion-btn {
            padding: 8px 16px;
            background: #f1f3f4;
            border: 1px solid #dadce0;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
        }
        
        .suggestion-btn:hover {
            background: #e8f0fe;
            border-color: #2196F3;
        }
        
        .typing-indicator {
            display: none;
            padding: 10px;
            font-style: italic;
            color: #666;
        }
        
        @media (max-width: 600px) {
            .container {
                margin: 10px;
                border-radius: 10px;
            }
            
            .header {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 1.5em;
            }
            
            .chat-container {
                height: 400px;
            }
            
            .message-content {
                max-width: 85%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Portfolio Chatbot</h1>
            <p>Tìm hiểu về Lê Ngọc Dương - Web Developer</p>
        </div>
        
        <div class="chat-container" id="chatContainer">
            <div class="message bot">
                <div class="message-content">
                    Xin chào! Tôi là chatbot của Lê Ngọc Dương. Tôi có thể trả lời các câu hỏi về kinh nghiệm, kỹ năng và dự án của anh ấy. Hãy hỏi tôi bất cứ điều gì! 😊
                </div>
            </div>
        </div>
        
        <div class="input-container">
            <div class="suggestions">
                <button class="suggestion-btn" onclick="sendSuggestion('Bạn tên gì?')">Giới thiệu</button>
                <button class="suggestion-btn" onclick="sendSuggestion('Bạn có những kỹ năng gì?')">Kỹ năng</button>
                <button class="suggestion-btn" onclick="sendSuggestion('Dự án nào bạn đã làm?')">Dự án</button>
                <button class="suggestion-btn" onclick="sendSuggestion('Làm sao để liên hệ?')">Liên hệ</button>
            </div>
            
            <div class="input-group">
                <input type="text" id="messageInput" placeholder="Nhập câu hỏi của bạn..." onkeypress="handleKeyPress(event)">
                <button id="sendButton" onclick="sendMessage()">Gửi</button>
            </div>
            
            <div class="typing-indicator" id="typingIndicator">
                Bot đang trả lời...
            </div>
        </div>
    </div>

    <script>
        function addMessage(content, isUser = false) {
            const chatContainer = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = content;
            
            messageDiv.appendChild(contentDiv);
            chatContainer.appendChild(messageDiv);
            
            // Scroll to bottom
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        function showTyping() {
            document.getElementById('typingIndicator').style.display = 'block';
        }
        
        function hideTyping() {
            document.getElementById('typingIndicator').style.display = 'none';
        }
        
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const sendButton = document.getElementById('sendButton');
            const message = input.value.trim();
            
            if (!message) return;
            
            // Add user message
            addMessage(message, true);
            
            // Clear input and disable button
            input.value = '';
            sendButton.disabled = true;
            showTyping();
            
            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message })
                });
                
                const data = await response.json();
                
                // Add bot response
                setTimeout(() => {
                    hideTyping();
                    addMessage(data.response);
                    sendButton.disabled = false;
                    input.focus();
                }, 1000);
                
            } catch (error) {
                hideTyping();
                addMessage('Xin lỗi, có lỗi xảy ra. Vui lòng thử lại!');
                sendButton.disabled = false;
            }
        }
        
        function sendSuggestion(text) {
            document.getElementById('messageInput').value = text;
            sendMessage();
        }
        
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        // Focus on input when page loads
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('messageInput').focus();
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    """Trang chủ với giao diện chat"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    """API endpoint để xử lý tin nhắn chat"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'Tin nhắn không được để trống'}), 400
        
        # Xử lý tin nhắn với chatbot
        result = bot.chat(message)
        
        return jsonify({
            'response': result['response'],
            'intent': result['intent'],
            'message_count': result['message_count']
        })
        
    except Exception as e:
        return jsonify({'error': f'Lỗi server: {str(e)}'}), 500

@app.route('/help', methods=['GET'])
def help_endpoint():
    """API endpoint để lấy hướng dẫn sử dụng"""
    return jsonify({'help': bot.get_help()})

@app.route('/health', methods=['GET'])  
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Chatbot đang hoạt động tốt!'})

if __name__ == '__main__':
    print("🚀 Portfolio Chatbot Server đang khởi động...")
    print("🌐 Truy cập: http://localhost:5000")
    print("📡 API Chat: POST /chat")
    print("❓ API Help: GET /help")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
