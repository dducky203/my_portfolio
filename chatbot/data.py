# Dữ liệu thông tin cá nhân và nghề nghiệp
PERSONAL_INFO = {
    "name": "Lê Ngọc Dương",
    "english_name": "Duong Le Ngoc", 
    "title": "Lập trình viên Backend / Backend Developer",
    "experience_years": "3 tháng",
    "location": "Việt Nam / Vietnam",
    "description_vi": "Tôi là một lập trình viên backend đam mê với 3 tháng kinh nghiệm thực chiến tạo ra các ứng dụng phía máy chủ mạnh mẽ và có thể mở rộng. Tôi cũng có khả năng phát triển frontend, cho phép tôi làm việc trên toàn bộ stack khi cần thiết.",
    "description_en": "I am a passionate backend developer with 3 months of hands-on experience creating robust and scalable server-side applications. I also have frontend development capabilities, allowing me to work across the full stack when needed.",
    "passion_vi": "Đam mê với kiến trúc hệ thống và hiệu suất ứng dụng",
    "passion_en": "Passionate about system architecture and application performance",
    "goal_vi": "Xây dựng những ứng dụng không chỉ hoạt động hoàn hảo mà còn mang lại hiệu suất và độ tin cậy tuyệt vời",
    "goal_en": "Building applications that not only work perfectly but also provide exceptional performance and reliability"
}

# Kỹ năng và công nghệ
SKILLS = {
    "backend": {
        "Node.js": 85,
        "Express.js": 80,
        "Python": 75,
        "MongoDB": 70,
        "PostgreSQL": 65,
        "REST API": 85
    },
    "frontend": {
        "React": 70,
        "JavaScript": 75,
        "HTML5": 80,
        "CSS3": 75,
        "TypeScript": 60
    },
    "tools": {
        "Git": 80,
        "Docker": 60,
        "Postman": 85,
        "VS Code": 90
    },
    "specialties": ["Backend Development", "API Development", "Database Design", "Full-stack Development"]
}

# Dự án đã thực hiện
PROJECTS = [
    {
        "title": "Website Thương Mại Điện Tử / Home Rental Website",
        "description": "Một nền tảng thương mại điện tử hiện đại được xây dựng bằng React, bao gồm danh mục sản phẩm, giỏ hàng và tích hợp thanh toán. Website cho thuê nhà với đầy đủ chức năng quản lý bất động sản.",
        "technologies": ["React", "Redux", "Node.js", "Express.js", "MongoDB"],
        "github_link": "https://github.com/lnduong203/Home-Rentals",
        "live_demo": "https://home-rentals-ten.vercel.app",
        "features": ["Quản lý bất động sản", "Hệ thống đặt phòng", "Xác thực người dùng", "Giao diện responsive"]
    },
    {
        "title": "Web Xem Phim - Clone Netflix / Movie App",
        "description": "Một ứng dụng clone Netflix với giao diện đẹp và chức năng phát video mượt mà. Cho phép người dùng duyệt và xem phim yêu thích với trải nghiệm tương tự Netflix.",
        "technologies": ["React", "TypeScript", "Material-UI", "Vercel"],
        "github_link": "https://github.com/lnduong203/MovieApp_CloneNETFLIX",
        "live_demo": "https://movie-app-clone-netflix.vercel.app",
        "features": ["Giao diện giống Netflix", "Tìm kiếm phim", "Phân loại theo thể loại", "Responsive design"]
    },
    {
        "title": "Bảng Điều Khiển Thời Tiết / Weather Dashboard",
        "description": "Một ứng dụng thời tiết responsive cung cấp điều kiện hiện tại và dự báo với hình ảnh trực quan đẹp mắt.",
        "technologies": ["React", "API Integration", "CSS3", "Chart.js"],
        "github_link": "Đang phát triển",
        "live_demo": "Đang phát triển",
        "features": ["Thời tiết hiện tại", "Dự báo 7 ngày", "Biểu đồ trực quan", "Tìm kiếm theo thành phố"]
    },
    {
        "title": "Website Portfolio",
        "description": "Một website portfolio cá nhân giới thiệu các dự án và kỹ năng với hoạt ảnh mượt mà và thiết kế responsive. Tích hợp chatbot AI thông minh.",
        "technologies": ["React", "Framer Motion", "CSS3", "Vite", "AI Chatbot"],
        "github_link": "https://github.com/dducky203/my_portfolio",
        "live_demo": "Portfolio hiện tại bạn đang xem",
        "features": ["Animations mượt mà", "Multi-language", "AI Chatbot", "Dark/Light mode"]
    }
]

# Thống kê nghề nghiệp
STATS = {
    "projects_completed": "5+",
    "years_experience": "3 tháng", 
    "happy_clients": "5+"
}

# Thông tin liên hệ
CONTACT_INFO = {
    "email": "ngocduongxk2003@gmail.com",
    "phone": "+84962498015", 
    "location": "Hà Nội, Việt Nam",
    "github": "https://github.com/dducky203",
    "portfolio": "Website portfolio hiện tại",
    "availability": "Luôn quan tâm đến những cơ hội mới và các dự án thú vị",
    "cv": "Có thể tải CV từ website portfolio",
    "preferred_contact": "Email hoặc số điện thoại",
    "response_time": "Thường phản hồi trong vòng 24h"
}

# Từ khóa và pattern để nhận diện câu hỏi
QUESTION_PATTERNS = {
    "name": ["tên", "tên gì", "tên là gì", "name", "who are you", "bạn là ai"],
    "experience": ["kinh nghiệm", "experience", "làm việc bao lâu", "years", "năm"],
    "skills": ["kỹ năng", "skills", "biết gì", "công nghệ", "technology", "tech stack"],
    "projects": ["dự án", "projects", "đã làm gì", "portfolio", "work"],
    "contact": ["liên hệ", "contact", "email", "phone", "số điện thoại"],
    "description": ["mô tả", "giới thiệu", "about", "description", "bạn là ai"],
    "stats": ["thống kê", "stats", "số liệu", "achievement"]
}

# Responses templates
RESPONSES = {
    "greeting": [
        "Xin chào! Tôi là chatbot của Lê Ngọc Dương. Tôi có thể trả lời các câu hỏi về kinh nghiệm backend, kỹ năng lập trình và dự án của anh ấy.",
        "Chào bạn! Tôi ở đây để giúp bạn tìm hiểu về Lê Ngọc Dương - một backend developer đam mê.",
        "Hello! Tôi có thể giúp bạn tìm hiểu về Dương - một backend developer với 3 tháng kinh nghiệm thực chiến."
    ],
    "unknown": [
        "Xin lỗi, tôi không hiểu câu hỏi của bạn. Bạn có thể hỏi về kinh nghiệm, kỹ năng, dự án hoặc thông tin liên hệ của Lê Ngọc Dương.",
        "Tôi chưa thể trả lời câu hỏi này. Hãy thử hỏi về kỹ năng lập trình, dự án đã thực hiện, hoặc cách liên hệ nhé!",
        "Hmm, tôi không chắc về điều đó. Bạn có thể hỏi tôi về kinh nghiệm làm việc, công nghệ sử dụng, hoặc các dự án của Dương không?"
    ]
}
