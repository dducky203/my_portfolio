import React from "react";
import { motion } from "framer-motion";
import { FaGithub, FaExternalLinkAlt } from "react-icons/fa";
import { useLanguage } from "../../contexts/LanguageContext";
import { translations } from "../../data/translations";
import "./Projects.css";
import movieAppImage from "../../assets/projectImg/movie-app.png";
import homeImg from "../../assets/projectImg/home.png";

const Projects = () => {
  const { language } = useLanguage();
  const t = translations[language];

  const projects = [
    {
      title: t.projects.items[0].title,
      description: t.projects.items[0].description,
      image: homeImg,
      technologies: ["React", "Redux", "Node.js", "Express.js", "MongoDB" ],
      githubLink: "https://github.com/lnduong203/Home-Rentals",
      liveLink: "https://home-rentals-ten.vercel.app",
      // dashBoardLink: "https://home-rentals-admin.vercel.app",
    },
    {
      title: t.projects.items[1].title,
      description: t.projects.items[1].description,
      image: movieAppImage,
      technologies: ["React", "TypeScript", "Vercel", "Material-UI"],
      githubLink: "https://github.com/lnduong203/MovieApp_CloneNETFLIX",
      liveLink: "https://movie-app-clone-netflix.vercel.app",
    },
    {
      title: t.projects.items[2].title,
      description: t.projects.items[2].description,
      image: "https://via.placeholder.com/400x250?text=Weather+Dashboard",
      technologies: ["React", "API Integration", "CSS3", "Chart.js"],
      githubLink: "#",
      liveLink: "#",
    },
    {
      title: t.projects.items[3].title,
      description: t.projects.items[3].description,
      image: "https://via.placeholder.com/400x250?text=Portfolio+Website",
      technologies: ["React", "Framer Motion", "CSS3", "Vite"],
      githubLink: "#",
      liveLink: "#",
    },
  ];

  return (
    <section id="projects" className="projects section">
      <div className="container">
        <motion.h2
          className="section-title"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          viewport={{ once: true }}
        >
          {t.projects.title}
        </motion.h2>

        <div className="projects-grid">
          {projects.map((project, index) => (
            <motion.div
              key={index}
              className="project-card"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.2 }}
              viewport={{ once: true }}
              whileHover={{ y: -10 }}
            >
              <div className="project-image">
                <img src={project.image} alt={project.title} />
                <div className="project-overlay">
                  <div className="project-links">
                    <a href={project.githubLink} title="GitHub Repository" className="project-link">
                      <FaGithub />
                    </a>
                    <a href={project.liveLink} title="Live Demo" className="project-link">
                      <FaExternalLinkAlt />
                    </a>
                    {project.dashBoardLink && (
                      <a href={project.dashBoardLink} title="Dashboard" className="project-link">
                        <FaExternalLinkAlt />
                      </a>
                    )}
                  </div>
                </div>
              </div>

              <div className="project-content">
                <h3>{project.title}</h3>
                <p>{project.description}</p>
                <div className="project-technologies">
                  {project.technologies.map((tech, techIndex) => (
                    <span key={techIndex} className="tech-tag">
                      {tech}
                    </span>
                  ))}
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Projects;
