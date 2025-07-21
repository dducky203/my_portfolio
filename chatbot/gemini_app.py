from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from gemini_chatbot import GeminiPortfolioChatbot
import os

app = Flask(__name__)
CORS(app)

# Khởi tạo chatbot
try:
    bot = GeminiPortfolioChatbot()
    CHATBOT_READY = True
except Exception as e:
    print(f"Lỗi khởi tạo Gemini chatbot: {e}")
    CHATBOT_READY = False

# HTML template cho giao diện web
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Portfolio Chatbot - Lê Ngọc Dương</title>
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
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .header {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 30px;
            text-align: center;
            position: relative;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            pointer-events: none;
        }
        
        .header h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }
        
        .header p {
            opacity: 0.9;
            font-size: 1.1em;
            position: relative;
            z-index: 1;
        }
        
        .ai-badge {
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-top: 10px;
            position: relative;
            z-index: 1;
        }
        
        .chat-container {
            height: 500px;
            overflow-y: auto;
            padding: 20px;
            background: #f8f9fa;
            position: relative;
        }
        
        .message {
            margin-bottom: 20px;
            display: flex;
            align-items: flex-start;
            animation: fadeIn 0.3s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message.bot {
            justify-content: flex-start;
        }
        
        .avatar {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            margin: 0 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2em;
            flex-shrink: 0;
        }
        
        .user-avatar {
            background: #2196F3;
            color: white;
        }
        
        .bot-avatar {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        
        .message-content {
            max-width: 70%;
            padding: 15px 20px;
            border-radius: 20px;
            white-space: pre-wrap;
            line-height: 1.5;
            position: relative;
        }
        
        .message.user .message-content {
            background: #2196F3;
            color: white;
            border-bottom-right-radius: 5px;
            box-shadow: 0 2px 10px rgba(33, 150, 243, 0.3);
        }
        
        .message.bot .message-content {
            background: white;
            color: #333;
            border: 1px solid #e1e8ed;
            border-bottom-left-radius: 5px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .input-container {
            padding: 25px;
            border-top: 1px solid #e1e8ed;
            background: white;
        }
        
        .suggestions {
            margin-bottom: 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .suggestion-btn {
            padding: 10px 18px;
            background: linear-gradient(135deg, #f1f3f4, #e8eaf6);
            border: 1px solid #dadce0;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s ease;
            color: #5f6368;
        }
        
        .suggestion-btn:hover {
            background: linear-gradient(135deg, #e8f0fe, #c8e6c9);
            border-color: #667eea;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        }
        
        .input-group {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        
        #messageInput {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #e1e8ed;
            border-radius: 30px;
            font-size: 16px;
            outline: none;
            transition: all 0.3s ease;
            background: #fafafa;
        }
        
        #messageInput:focus {
            border-color: #667eea;
            background: white;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        #sendButton {
            padding: 15px 25px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            min-width: 100px;
        }
        
        #sendButton:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
        
        #sendButton:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        .typing-indicator {
            display: none;
            padding: 15px;
            font-style: italic;
            color: #666;
            text-align: center;
        }
        
        .typing-dots {
            display: inline-block;
        }
        
        .typing-dots span {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #667eea;
            margin: 0 2px;
            animation: typing 1.4s infinite;
        }
        
        .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
        .typing-dots span:nth-child(3) { animation-delay: 0.4s; }
        
        @keyframes typing {
            0%, 60%, 100% { transform: translateY(0); }
            30% { transform: translateY(-10px); }
        }
        
        .status-indicator {
            position: absolute;
            top: 20px;
            right: 20px;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .status-online {
            background: rgba(76, 175, 80, 0.2);
            color: #4CAF50;
        }
        
        .status-offline {
            background: rgba(244, 67, 54, 0.2);
            color: #F44336;
        }
        
        @media (max-width: 600px) {
            .container {
                margin: 10px;
                border-radius: 15px;
            }
            
            .header {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
            
            .chat-container {
                height: 400px;
                padding: 15px;
            }
            
            .message-content {
                max-width: 85%;
                padding: 12px 16px;
            }
            
            .input-container {
                padding: 20px;
            }
            
            .suggestions {
                margin-bottom: 15px;
            }
            
            .suggestion-btn {
                padding: 8px 15px;
                font-size: 13px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="status-indicator" id="statusIndicator">
                🟢 AI Online
            </div>
            <h1>🤖 AI Portfolio Chatbot</h1>
            <p>Powered by Google Gemini AI</p>
            <div class="ai-badge">Trò chuyện thông minh về Lê Ngọc Dương</div>
        </div>
        
        <div class="chat-container" id="chatContainer">
            <div class="message bot">
                <div class="avatar bot-avatar">🤖</div>
                <div class="message-content">
                    Xin chào! Tôi là AI assistant của Lê Ngọc Dương, được hỗ trợ bởi Google Gemini. Tôi có thể trả lời mọi câu hỏi về kinh nghiệm, kỹ năng, dự án và cách liên hệ với anh ấy. Hãy hỏi tôi bất cứ điều gì! ✨
                </div>
            </div>
        </div>
        
        <div class="input-container">
            <div class="suggestions">
                <button class="suggestion-btn" onclick="sendSuggestion('Hãy giới thiệu về bản thân bạn')">🙋‍♂️ Giới thiệu</button>
                <button class="suggestion-btn" onclick="sendSuggestion('Bạn có những kỹ năng lập trình gì?')">💻 Kỹ năng</button>
                <button class="suggestion-btn" onclick="sendSuggestion('Những dự án nào bạn tự hào nhất?')">🚀 Dự án</button>
                <button class="suggestion-btn" onclick="sendSuggestion('Làm thế nào để liên hệ với bạn?')">📞 Liên hệ</button>
                <button class="suggestion-btn" onclick="sendSuggestion('Bạn đang tìm kiếm cơ hội gì?')">🎯 Cơ hội</button>
            </div>
            
            <div class="input-group">
                <input type="text" id="messageInput" placeholder="Hỏi tôi về Lê Ngọc Dương..." onkeypress="handleKeyPress(event)">
                <button id="sendButton" onclick="sendMessage()">Gửi</button>
            </div>
            
            <div class="typing-indicator" id="typingIndicator">
                AI đang suy nghĩ <div class="typing-dots"><span></span><span></span><span></span></div>
            </div>
        </div>
    </div>

    <script>
        function addMessage(content, isUser = false, avatar = '') {
            const chatContainer = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
            
            const avatarDiv = document.createElement('div');
            avatarDiv.className = `avatar ${isUser ? 'user-avatar' : 'bot-avatar'}`;
            avatarDiv.textContent = isUser ? '👤' : '🤖';
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = content;
            
            if (isUser) {
                messageDiv.appendChild(contentDiv);
                messageDiv.appendChild(avatarDiv);
            } else {
                messageDiv.appendChild(avatarDiv);
                messageDiv.appendChild(contentDiv);
            }
            
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        function showTyping() {
            document.getElementById('typingIndicator').style.display = 'block';
            document.getElementById('chatContainer').scrollTop = document.getElementById('chatContainer').scrollHeight;
        }
        
        function hideTyping() {
            document.getElementById('typingIndicator').style.display = 'none';
        }
        
        function updateStatus(online) {
            const statusIndicator = document.getElementById('statusIndicator');
            if (online) {
                statusIndicator.className = 'status-indicator status-online';
                statusIndicator.textContent = '🟢 AI Online';
            } else {
                statusIndicator.className = 'status-indicator status-offline';
                statusIndicator.textContent = '🔴 AI Offline';
            }
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
                
                // Simulate AI thinking time
                setTimeout(() => {
                    hideTyping();
                    if (data.success) {
                        addMessage(data.response);
                        updateStatus(true);
                    } else {
                        addMessage('Xin lỗi, AI đang gặp vấn đề kỹ thuật. Vui lòng thử lại sau! 😅');
                        updateStatus(false);
                    }
                    sendButton.disabled = false;
                    input.focus();
                }, Math.random() * 1000 + 1000); // 1-2 seconds delay
                
            } catch (error) {
                hideTyping();
                addMessage('Không thể kết nối với AI. Vui lòng kiểm tra kết nối mạng! 🌐');
                updateStatus(false);
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
            updateStatus(true);
        });
        
        // Check connection periodically
        setInterval(async () => {
            try {
                const response = await fetch('/health');
                updateStatus(response.ok);
            } catch (error) {
                updateStatus(false);
            }
        }, 30000); // Check every 30 seconds
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    """Trang chủ với giao diện chat AI"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    """API endpoint để xử lý tin nhắn chat với Gemini"""
    if not CHATBOT_READY:
        return jsonify({
            'success': False,
            'response': 'Chatbot chưa sẵn sàng. Vui lòng kiểm tra cấu hình API key!',
            'error': 'Chatbot not initialized'
        }), 500
    
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        language = data.get('language', 'vi')  # Default to Vietnamese
        
        if not message:
            error_msg = 'Message cannot be empty' if language == 'en' else 'Tin nhắn không được để trống'
            return jsonify({'error': error_msg}), 400
        
        # Xử lý tin nhắn với Gemini chatbot
        result = bot.chat(message, language)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'response': 'Có lỗi xảy ra khi xử lý tin nhắn. Vui lòng thử lại!',
            'error': str(e)
        }), 500

@app.route('/history', methods=['GET'])
def get_history():
    """API endpoint để lấy lịch sử hội thoại"""
    if not CHATBOT_READY:
        return jsonify({'error': 'Chatbot not ready'}), 500
    
    return jsonify({'history': bot.get_conversation_history()})

@app.route('/clear', methods=['POST'])
def clear_history():
    """API endpoint để xóa lịch sử hội thoại"""
    if not CHATBOT_READY:
        return jsonify({'error': 'Chatbot not ready'}), 500
    
    result = bot.clear_history()
    return jsonify(result)

@app.route('/health', methods=['GET'])  
def health_check():
    """Health check endpoint"""
    status = 'healthy' if CHATBOT_READY else 'unhealthy'
    return jsonify({
        'status': status,
        'chatbot_ready': CHATBOT_READY,
        'message': 'AI Chatbot đang hoạt động tốt!' if CHATBOT_READY else 'AI Chatbot chưa sẵn sàng'
    })

if __name__ == '__main__':
    print("🚀 AI Portfolio Chatbot Server đang khởi động...")
    print("🤖 Powered by Google Gemini AI")
    print("🌐 Truy cập: http://localhost:5000")
    print("📡 API Chat: POST /chat")
    print("📊 API Health: GET /health")
    print()
    
    if not CHATBOT_READY:
        print("⚠️  CẢNH BÁO: Vui lòng cấu hình GEMINI_API_KEY trong file .env")
        print("📝 Hướng dẫn:")
        print("   1. Copy file .env.example thành .env")
        print("   2. Lấy API key từ https://makersuite.google.com/app/apikey")
        print("   3. Thay thế your_gemini_api_key_here bằng API key thực")
        print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
