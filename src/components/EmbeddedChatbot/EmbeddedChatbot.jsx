import React, { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { useLanguage } from "../../contexts/LanguageContext";
import "./EmbeddedChatbot.css";

const EmbeddedChatbot = () => {
  const { language } = useLanguage();
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    {
      id: 1,
      text:
        language === "en"
          ? "Hello! I'm Duong Le Ngoc's AI assistant. I can answer questions about his experience, skills, and projects. Ask me anything! ✨"
          : "Xin chào! Tôi là AI assistant của Lê Ngọc Dương. Tôi có thể trả lời các câu hỏi về kinh nghiệm, kỹ năng và dự án của anh ấy. Hãy hỏi tôi bất cứ điều gì! ✨",
      isBot: true,
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [isOnline, setIsOnline] = useState(true);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  // Use deployed API URL or fallback to localhost for development
  const API_BASE_URL = import.meta.env.VITE_CHATBOT_API_URL || "http://localhost:5000";

  // Log API URL for debugging (remove in production)
  console.log('Chatbot API URL:', API_BASE_URL);

  
  // Update welcome message when language changes
  useEffect(() => {
    setMessages((prevMessages) => [
      {
        id: 1,
        text:
          language === "en"
            ? "Hello! I'm Duong Le Ngoc's AI assistant. I can answer questions about his experience, skills, and projects. Ask me anything! ✨"
            : "Xin chào! Tôi là AI assistant của Lê Ngọc Dương. Tôi có thể trả lời các câu hỏi về kinh nghiệm, kỹ năng và dự án của anh ấy. Hãy hỏi tôi bất cứ điều gì! ✨",
        isBot: true,
        timestamp: new Date(),
      },
      ...prevMessages.slice(1), // Keep other messages
    ]);
  }, [language]);

  // Function để convert links thành thẻ a có thể click
  const convertLinksToClickable = (text) => {
    // Regex để tìm URLs
    const urlRegex = /(https?:\/\/[^\s]+)/g;

    // Thay thế URLs bằng thẻ a
    const textWithLinks = text.replace(urlRegex, (url) => {
      return `<a href="${url}" target="_blank" rel="noopener noreferrer" class="chat-link">${url}</a>`;
    });

    // Thay thế line breaks bằng <br>
    return textWithLinks.replace(/\n/g, "<br>");
  };

  // Function để render message content với HTML
  const renderMessageContent = (text) => {
    const htmlContent = convertLinksToClickable(text);
    return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />;
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (isOpen && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isOpen]);

  // Kiểm tra trạng thái server
  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/health`);
        setIsOnline(response.ok);
      } catch (error) {
        setIsOnline(false);
      }
    };

    checkHealth();
    const interval = setInterval(checkHealth, 30000);
    return () => clearInterval(interval);
  }, []);

  const sendMessage = async (messageText = inputValue) => {
    if (!messageText.trim()) return;

    const userMessage = {
      id: Date.now(),
      text: messageText,
      isBot: false,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInputValue("");
    setIsTyping(true);

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: messageText,
          language: language,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      setTimeout(() => {
        const botMessage = {
          id: Date.now() + 1,
          text: data.success
            ? data.response
            : data.error && data.error.includes('quota')
            ? language === "en"
              ? "I'm temporarily unavailable due to API quota limits. Please try again later! 🤖"
              : "Tôi tạm thời không khả dụng do giới hạn quota API. Vui lòng thử lại sau! 🤖"
            : language === "en"
            ? "Sorry, I encountered a technical issue. Please try again! 😅"
            : "Xin lỗi, tôi gặp chút vấn đề kỹ thuật. Vui lòng thử lại sau! 😅",
          isBot: true,
          timestamp: new Date(),
        };

        setMessages((prev) => [...prev, botMessage]);
        setIsTyping(false);
        setIsOnline(data.success || response.ok);
      }, 1000 + Math.random() * 1000);
    } catch (error) {
      setTimeout(() => {
        const errorMessage = {
          id: Date.now() + 1,
          text:
            language === "en"
              ? "Cannot connect to AI. Please check your network connection! 🌐"
              : "Không thể kết nối với AI. Vui lòng kiểm tra kết nối mạng! 🌐",
          isBot: true,
          timestamp: new Date(),
        };

        setMessages((prev) => [...prev, errorMessage]);
        setIsTyping(false);
        setIsOnline(false);
      }, 1000);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const suggestionQuestions =
    language === "en"
      ? [
          "Tell me about yourself",
          "What are your skills?",
          "Which project are you most proud of?",
          "How can I contact you?",
        ]
      : [
          "Hãy giới thiệu về bản thân",
          "Bạn có những kỹ năng gì?",
          "Dự án nào bạn tự hào nhất?",
          "Làm sao để liên hệ với bạn?",
        ];

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="embedded-chatbot">
      {/* Chat Toggle Button */}
      <motion.button
        className={`chat-toggle ${isOpen ? "active" : ""}`}
        onClick={toggleChat}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        animate={isOpen ? { rotate: 180 } : { rotate: 0 }}
      >
        <span className="toggle-icon">{isOpen ? "✕" : "💬"}</span>
        {!isOpen && (
          <motion.div
            className="chat-notification"
            animate={{ scale: [1, 1.2, 1] }}
            transition={{ repeat: Infinity, duration: 2 }}
          >
            <span className="notification-dot"></span>
          </motion.div>
        )}
      </motion.button>

      {/* Chat Window */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            className="chat-window"
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 20, scale: 0.95 }}
            transition={{ duration: 0.3 }}
          >
            {/* Header */}
            <div className="chat-header">
              <div className="header-info">
                <div className="avatar">🤖</div>
                <div className="info">
                  <h4>AI Assistant</h4>
                  <span className={`status ${isOnline ? "online" : "offline"}`}>
                    {isOnline
                      ? language === "en"
                        ? "🟢 Online"
                        : "🟢 Trực tuyến"
                      : language === "en"
                      ? "🔴 Offline"
                      : "🔴 Ngoại tuyến"}
                  </span>
                </div>
              </div>
              <button className="minimize-btn" onClick={toggleChat}>
                <span>−</span>
              </button>
            </div>

            {/* Messages */}
            <div className="chat-messages">
              {messages.map((message) => (
                <motion.div
                  key={message.id}
                  className={`message ${message.isBot ? "bot" : "user"}`}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.3 }}
                >
                  {message.isBot && <div className="message-avatar">🤖</div>}
                  <div className="message-content">
                    {renderMessageContent(message.text)}
                    <span className="message-time">
                      {message.timestamp.toLocaleTimeString("vi-VN", {
                        hour: "2-digit",
                        minute: "2-digit",
                      })}
                    </span>
                  </div>
                  {!message.isBot && <div className="message-avatar">👤</div>}
                </motion.div>
              ))}

              {/* Typing Indicator */}
              {isTyping && (
                <motion.div
                  className="message bot typing"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  <div className="message-avatar">🤖</div>
                  <div className="message-content">
                    <div className="typing-indicator">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                </motion.div>
              )}

              <div ref={messagesEndRef} />
            </div>

            {/* Suggestions */}
            {messages.length === 1 && (
              <div className="suggestions">
                {suggestionQuestions.map((question, index) => (
                  <motion.button
                    key={index}
                    className="suggestion-btn"
                    onClick={() => sendMessage(question)}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.1 }}
                  >
                    {question}
                  </motion.button>
                ))}
              </div>
            )}

            {/* Input */}
            <div className="chat-input">
              <div className="input-wrapper">
                <input
                  ref={inputRef}
                  type="text"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  onKeyPress={handleKeyPress}
                  placeholder={
                    language === "en"
                      ? "Ask about Duong Le Ngoc..."
                      : "Hỏi về Lê Ngọc Dương..."
                  }
                  disabled={isTyping || !isOnline}
                />
                <button
                  onClick={() => sendMessage()}
                  disabled={!inputValue.trim() || isTyping || !isOnline}
                  className="send-btn"
                >
                  <span>➤</span>
                </button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default EmbeddedChatbot;
