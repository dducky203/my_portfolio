import React from "react";
import { motion } from "framer-motion";
import { useLanguage } from "../../contexts/LanguageContext";
import { translations } from "../../data/translations";
import "./About.css";

const About = () => {
  const { language } = useLanguage();
  const t = translations[language];

  return (
    <section id="about" className="about section">
      <div className="container">
        <motion.h2
          className="section-title"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
        >
          {t.about.title}
        </motion.h2>

        <div className="about-content">
          <motion.div
            className="about-text"
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            viewport={{ once: true }}
          >
            <h3>{t.about.subtitle}</h3>
            <p>{t.about.description1}</p>
            <p>{t.about.description2}</p>

            <div className="about-stats">
              <div className="stat">
                <h4>50+</h4>
                <p>{t.about.stats.projects}</p>
              </div>
              <div className="stat">
                <h4>3+</h4>
                <p>{t.about.stats.experience}</p>
              </div>
              <div className="stat">
                <h4>20+</h4>
                <p>{t.about.stats.clients}</p>
              </div>
            </div>
          </motion.div>

          <motion.div
            className="about-image"
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            viewport={{ once: true }}
          >
            <img
              src="https://via.placeholder.com/500x600?text=About+Me"
              alt="About Me"
            />
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default About;
