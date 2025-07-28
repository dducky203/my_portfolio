# 🤖 HƯỚNG DẪN CÀI ĐẶT VÀ SỬ DỤNG AI CHATBOT

## 📋 Tổng quan

Bạn vừa có một chatbot AI thông minh sử dụng Google Gemini AI để trả lời các câu hỏi về portfolio của Lê Ngọc Dương. Chatbot có thể:

✅ Trả lời thông minh và tự nhiên  
✅ Hiểu ngữ cảnh câu hỏi  
✅ Nhúng vào website React  
✅ Giao diện web đẹp mắt  
✅ Responsive trên mobile

## 🚀 CÁCH 1: CÀI ĐẶT NHANH (KHUYẾN NGHỊ)

### Bước 1: Chạy setup

```bash
cd d:\Portfolio\chatbot
setup.bat
```

### Bước 2: Lấy API key

1. Truy cập: https://makersuite.google.com/app/apikey
2. Đăng nhập Google account
3. Tạo API key mới
4. Copy API key

### Bước 3: Cấu hình

1. Mở file `.env` trong thư mục chatbot
2. Thay thế `your_gemini_api_key_here` bằng API key vừa copy
3. Lưu file

### Bước 4: Chạy chatbot

```bash
# Giao diện web (khuyến nghị)
start_web.bat

# Hoặc chế độ terminal
start_gemini_terminal.bat
```

## 🌐 CÁCH 2: NHÚNG VÀO WEBSITE PORTFOLIO

### Đã được tích hợp sẵn!

Chatbot đã được thêm vào `src/App.jsx` và sẽ xuất hiện ở góc dưới bên phải website.

### Để chạy cả website + chatbot:

1. **Chạy chatbot server:**

```bash
cd d:\Portfolio\chatbot
start_web.bat
```

2. **Chạy website portfolio:**

```bash
cd d:\Portfolio
npm run dev
```

3. **Truy cập:**

- Website: http://localhost:5173 (với chatbot nhúng)
- Chatbot riêng: http://localhost:5000

## 🔧 CÁCH 3: CÀI ĐẶT THỦ CÔNG

```bash
# 1. Tạo virtual environment
cd d:\Portfolio\chatbot
python -m venv venv
venv\Scripts\activate

# 2. Cài đặt packages
pip install -r requirements.txt

# 3. Tạo file .env
copy .env.example .env
# Chỉnh sửa .env và thêm GEMINI_API_KEY

# 4. Chạy
python gemini_app.py
```

## 💬 CÁCH SỬ DỤNG

### Ví dụ câu hỏi hay:

- "Hãy giới thiệu về bản thân bạn"
- "Bạn có những kỹ năng lập trình gì?"
- "Kể về dự án mà bạn tự hào nhất"
- "Làm thế nào để liên hệ với bạn?"
- "Bạn có kinh nghiệm với React không?"
- "Dự án Netflix clone của bạn như thế nào?"

### Features:

🎯 AI hiểu ngữ cảnh và trả lời chi tiết  
🌟 Giao diện đẹp mắt, hiện đại  
📱 Responsive trên mọi thiết bị  
⚡ Trả lời nhanh và chính xác  
🔄 Real-time messaging

## 🛠️ TROUBLESHOOTING

### ❌ Lỗi "GEMINI_API_KEY not found"

**Giải pháp:** Kiểm tra file `.env` và đảm bảo đã thêm API key

### ❌ Lỗi "Failed to connect"

**Giải pháp:** Kiểm tra kết nối internet và API key hợp lệ

### ❌ Chatbot không xuất hiện trên website

**Giải pháp:** Đảm bảo chatbot server đang chạy trên port 5000

### ❌ CORS error

**Giải pháp:** Chạy website từ localhost, không mở file HTML trực tiếp

## 📞 HỖ TRỢ

Nếu gặp vấn đề, hãy:

1. Kiểm tra lại các bước cài đặt
2. Đảm bảo API key hợp lệ
3. Kiểm tra kết nối internet
4. Xem log lỗi trong terminal

## 🎉 HOÀN THÀNH!

Giờ bạn đã có:
✅ Chatbot AI thông minh  
✅ Giao diện web đẹp mắt  
✅ Widget nhúng vào portfolio  
✅ Trải nghiệm người dùng tuyệt vời

Chúc bạn thành công! 🚀
