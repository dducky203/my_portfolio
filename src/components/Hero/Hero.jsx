import { motion } from "framer-motion";
import { FaGithub, FaLinkedin, FaDownload, FaFacebook } from "react-icons/fa";
import { useLanguage } from "../../contexts/LanguageContext";
import { translations } from "../../data/translations";
import "./Hero.css";
import profileImage from "../../assets/avatar/avatar.jpg";
import linkCvVN from "../../assets/pdf/CV-InternWeb-LeNgocDuong.pdf";
import linkCvEng from "../../assets/pdf/CV_English-InternWeb-LeNgocDuong.pdf";

const Hero = () => {
  const { language } = useLanguage();
  const t = translations[language];

  const handleDownloadCV = () => {
    
    const link = document.createElement("a");
    link.href = language === "en" ? linkCvEng : linkCvVN; 
    link.download =
      language === "en" ? "CV-Eng-DuongLeNgoc.pdf" : "CV-VN-LeNgocDuong.pdf";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <section id="home" className="hero">
      <div className="container">
        <div className="hero-content">
          <motion.div
            className="hero-text"
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h3 className="hero-greeting">{t.hero.greeting}</h3>
            <h1 className="hero-name">{t.hero.name}</h1>
            <h2 className="hero-title">{t.hero.title}</h2>
            <p className="hero-description">{t.hero.description}</p>
            <div className="hero-buttons">
              <a href="#projects" className="btn btn-primary">
                {t.hero.viewWork}
              </a>
              <a href="#contact" className="btn btn-outline">
                {t.hero.getInTouch}
              </a>
              <button onClick={handleDownloadCV} className="btn btn-download">
                <FaDownload />
                {t.hero.downloadCV}
              </button>
            </div>
            <div className="hero-social">
              <a href="https://github.com/dducky203" className="social-link">
                <FaGithub />
              </a>
              <a
                href="https://www.linkedin.com/in/le-ngoc-duong-4b6bb326a"
                className="social-link"
              >
                <FaLinkedin />
              </a>
              <a
                href="https://www.facebook.com/ngocduong203"
                className="social-link"
              >
                <FaFacebook />
              </a>
            </div>
          </motion.div>

          <motion.div
            className="hero-image"
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            <div className="image-placeholder">
              <img src={profileImage} alt="Profile" />
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
