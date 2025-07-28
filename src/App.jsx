import React from "react";
import { LanguageProvider } from "./contexts/LanguageContext";
import Header from "./components/Header/Header";
import Hero from "./components/Hero/Hero";
import About from "./components/About/About";
import Skills from "./components/Skills/Skills";
import Projects from "./components/Projects/Projects";
import Contact from "./components/Contact/Contact";
import Footer from "./components/Footer/Footer";
import EmbeddedChatbot from "./components/EmbeddedChatbot/EmbeddedChatbot";
import "./App.css";

function App() {
  return (
    <LanguageProvider>
      <div className="App">
        <Header />
        <Hero />
        <About />
        <Skills />
        <Projects />
        <Contact />
        <Footer />
        <EmbeddedChatbot />
      </div>
    </LanguageProvider>
  );
}

export default App;
