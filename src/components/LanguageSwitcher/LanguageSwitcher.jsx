import React from "react";
import { useLanguage } from "../../contexts/LanguageContext";
import "./LanguageSwitcher.css";

const LanguageSwitcher = () => {
  const { language, toggleLanguage } = useLanguage();

  return (
    <button className="language-switcher" onClick={toggleLanguage}>
      <span className={language === "en" ? "active" : ""}>EN</span>
      <span className="separator">|</span>
      <span className={language === "vi" ? "active" : ""}>VI</span>
    </button>
  );
};

export default LanguageSwitcher;
