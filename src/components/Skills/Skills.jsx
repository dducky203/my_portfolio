import React from "react";
import { motion } from "framer-motion";
import {
  FaReact,
  FaJs,
  FaHtml5,
  FaCss3Alt,
  FaNodeJs,
  FaGitAlt,
} from "react-icons/fa";
import {
  SiTypescript,
  SiNextdotjs,
  SiTailwindcss,
  SiFigma,
} from "react-icons/si";
import { useLanguage } from "../../contexts/LanguageContext";
import { translations } from "../../data/translations";
import "./Skills.css";

const Skills = () => {
  const { language } = useLanguage();
  const t = translations[language];

  const skills = [
    { name: "React", icon: FaReact, level: 90 },
    { name: "JavaScript", icon: FaJs, level: 85 },
    { name: "TypeScript", icon: SiTypescript, level: 80 },
    { name: "Next.js", icon: SiNextdotjs, level: 75 },
    { name: "HTML5", icon: FaHtml5, level: 95 },
    { name: "CSS3", icon: FaCss3Alt, level: 90 },
    { name: "Tailwind CSS", icon: SiTailwindcss, level: 85 },
    { name: "Node.js", icon: FaNodeJs, level: 70 },
    { name: "Git", icon: FaGitAlt, level: 80 },
    { name: "Figma", icon: SiFigma, level: 75 },
  ];

  return (
    <section id="skills" className="skills section">
      <div className="container">
        <motion.h2
          className="section-title"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
        >
          {t.skills.title}
        </motion.h2>

        <div className="skills-grid">
          {skills.map((skill, index) => (
            <motion.div
              key={index}
              className="skill-card"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
              whileHover={{ y: -5 }}
            >
              <div className="skill-icon">
                <skill.icon />
              </div>
              <h3>{skill.name}</h3>
              <div className="skill-bar">
                <motion.div
                  className="skill-progress"
                  initial={{ width: 0 }}
                  whileInView={{ width: `${skill.level}%` }}
                  transition={{ duration: 1, delay: index * 0.1 + 0.5 }}
                  viewport={{ once: true }}
                />
              </div>
              <span className="skill-percentage">{skill.level}%</span>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Skills;
