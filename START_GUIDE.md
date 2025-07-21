# Portfolio với AI Chatbot

## Cách khởi động

### 🚀 Khởi động tự động (cả Web + Chatbot)

#### Từ NPM:

```bash
npm run start:all
```

#### Từ Windows Explorer:

- Double-click vào `start-all.bat`
- Hoặc chạy `start-all.ps1` trong PowerShell

### 🎯 Khởi động riêng biệt

#### Web Portfolio:

```bash
npm run dev
```

Truy cập: http://localhost:5173/

#### AI Chatbot:

```bash
npm run start:chatbot
```

Hoặc: Double-click vào `start-chatbot.bat`
Truy cập: http://localhost:5000/

## 📋 Yêu cầu

1. **Node.js** và **npm** đã được cài đặt
2. **Python** với virtual environment đã được setup trong thư mục `chatbot/`
3. **GEMINI_API_KEY** đã được cấu hình trong file `chatbot/.env`

## 🔧 Setup lần đầu

1. Cài đặt dependencies cho web:

```bash
npm install
```

2. Setup chatbot (trong thư mục chatbot):

```bash
cd chatbot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Tạo file `.env` trong thư mục `chatbot/` với nội dung:

```
GEMINI_API_KEY=your_api_key_here
```

## 🌐 Truy cập

- **Portfolio Website**: http://localhost:5173/
- **AI Chatbot**: http://localhost:5000/

## 💡 Lưu ý

- Script `start:all` sẽ tự động khởi động cả hai service cùng lúc
- Khi dừng một service, service kia cũng sẽ được dừng tự động
- Đảm bảo đã cấu hình GEMINI_API_KEY trước khi chạy chatbot
