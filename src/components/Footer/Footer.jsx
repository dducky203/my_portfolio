
import { FaGithub, FaLinkedin, FaHeart, FaFacebook } from 'react-icons/fa'
import { useLanguage } from '../../contexts/LanguageContext'
import { translations } from '../../data/translations'
import './Footer.css'

const Footer = () => {
  const { language } = useLanguage()
  const t = translations[language]
  const currentYear = new Date().getFullYear()

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-text">
            <p>
              {t.footer.madeWith} <FaHeart className="heart-icon" /> {t.footer.by} 
            </p>
            <p>&copy; {currentYear} {t.footer.rights}</p>
          </div>
          
          <div className="footer-social">
            <a href="https://github.com/dducky203" className="social-link">
                <FaGithub />
              </a>
              <a href="https://www.linkedin.com/in/le-ngoc-duong-4b6bb326a" className="social-link">
                <FaLinkedin />
              </a>
              <a href="https://www.facebook.com/ngocduong203" className="social-link">
                <FaFacebook />
              </a>
            
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer
