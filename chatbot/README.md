# AI Portfolio Chatbot

Chatbot AI thông minh được tạo bằng Python và Google Gemini AI để trả lời các câu hỏi về thông tin cá nhân và kinh nghiệm nghề nghiệp của Lê Ngọc Dương.

## ✨ Tính năng

- 🤖 **AI thông minh**: Sử dụng Google Gemini AI để trả lời tự nhiên
- 🌐 **Web Interface**: Giao diện web đẹp mắt và responsive
- 💬 **Embedded Widget**: Component React để nhúng vào website
- 🔄 **Real-time Chat**: Trò chuyện thời gian thực
- 📱 **Mobile Friendly**: Tối ưu cho mobile
- 🎯 **Context Aware**: Hiểu ngữ cảnh và trả lời chính xác

## 🚀 Cài đặt nhanh

### 1. Chạy script setup (Windows)

```bash
setup.bat
```

### 2. Cấu hình API key

1. Lấy API key từ [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Mở file `.env`
3. Thay thế `your_gemini_api_key_here` bằng API key thực

### 3. Chạy ứng dụng

```bash
# Web interface
start_web.bat

# Terminal mode
start_gemini_terminal.bat
```

## 📋 Cài đặt thủ công

### Bước 1: Tạo virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### Bước 2: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### Bước 3: Cấu hình environment

```bash
cp .env.example .env
# Chỉnh sửa file .env và thêm GEMINI_API_KEY
```

### Bước 4: Chạy ứng dụng

```bash
# Web interface
python gemini_app.py

# Terminal mode
python run_gemini.py
```

## 🌐 Web Interface

Truy cập: `http://localhost:5000`

### Features:

- Giao diện chat hiện đại
- Typing indicators
- Status indicators
- Suggestions buttons
- Mobile responsive
- Real-time messaging

## 🔧 Nhúng vào React App

### 1. Copy component

```bash
# Copy thư mục EmbeddedChatbot vào src/components/
```

### 2. Import vào App.jsx

```jsx
import EmbeddedChatbot from "./components/EmbeddedChatbot/EmbeddedChatbot";

function App() {
  return (
    <div className="App">
      {/* Other components */}
      <EmbeddedChatbot />
    </div>
  );
}
```

### 3. Đảm bảo chatbot server đang chạy

```bash
python gemini_app.py
```

## 📡 API Endpoints

| Endpoint   | Method | Mô tả               |
| ---------- | ------ | ------------------- |
| `/`        | GET    | Giao diện web       |
| `/chat`    | POST   | Gửi tin nhắn        |
| `/health`  | GET    | Kiểm tra trạng thái |
| `/history` | GET    | Lịch sử chat        |
| `/clear`   | POST   | Xóa lịch sử         |

### Ví dụ API call:

```javascript
fetch("http://localhost:5000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    message: "Hãy giới thiệu về bản thân bạn",
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data.response));
```

## 💡 Ví dụ câu hỏi

### Thông tin cá nhân:

- "Hãy giới thiệu về bản thân bạn"
- "Bạn tên gì và làm nghề gì?"
- "Kể về background và kinh nghiệm của bạn"

### Kỹ năng & Công nghệ:

- "Bạn biết những kỹ năng lập trình gì?"
- "Công nghệ nào bạn thành thạo nhất?"
- "Bạn có kinh nghiệm với React không?"

### Dự án:

- "Những dự án nào bạn đã làm?"
- "Dự án nào bạn tự hào nhất?"
- "Kể về dự án web application của bạn"

### Liên hệ:

- "Làm thế nào để liên hệ với bạn?"
- "Bạn có đang tìm cơ hội làm việc không?"
- "Cách nào để hợp tác với bạn?"

## 🛠️ Cấu trúc project

```
chatbot/
├── gemini_chatbot.py      # Core AI chatbot logic
├── gemini_app.py          # Flask web server
├── data.py               # Dữ liệu portfolio
├── requirements.txt      # Dependencies
├── .env.example         # Template cấu hình
├── setup.bat           # Script setup Windows
├── start_web.bat       # Script chạy web
├── run_gemini.py       # Terminal mode
└── README.md          # Hướng dẫn này
```

## 🔒 Bảo mật

- API key được lưu trong file `.env` (không commit)
- CORS được cấu hình cho cross-origin requests
- Input validation và error handling
- Rate limiting (có thể thêm)

## 🐛 Troubleshooting

### Lỗi API key:

```
ValueError: GEMINI_API_KEY không được tìm thấy
```

**Giải pháp**: Kiểm tra file `.env` và API key

### Lỗi kết nối:

```
Failed to connect to AI
```

**Giải pháp**: Kiểm tra internet và API key hợp lệ

### Lỗi CORS:

```
CORS policy error
```

**Giải pháp**: Đảm bảo Flask server đang chạy trên localhost:5000

## 📝 Changelog

### v2.0 - AI Powered

- ✅ Tích hợp Google Gemini AI
- ✅ Web interface đẹp mắt
- ✅ Embedded React component
- ✅ Real-time chat
- ✅ Mobile responsive

### v1.0 - Basic

- ✅ Rule-based chatbot
- ✅ Basic web interface
- ✅ Terminal mode

## 🤝 Đóng góp

1. Fork project
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Liên hệ

Lê Ngọc Dương - [Portfolio Website](http://localhost:3000)

Project Link: [https://github.com/dducky203/my_portfolio](https://github.com/dducky203/my_portfolio)
