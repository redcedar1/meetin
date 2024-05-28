import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import Home from "./Home";
import About from "./pages/About"; // 수정된 경로
import Contact from "./pages/Contact"; // 수정된 경로
import "./App.css";

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <div class="mid">
          <Routes>
            <Route exact path="/" element={<Home />}></Route>
            <Route path="/about" element={<About />}></Route>
            <Route path="/contact" element={<Contact />}></Route>
          </Routes>
        </div>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
/*
<mid>
<Routes>
  <Route exact path="/" element={<Home />}></Route>
  <Route path="/about" element={<About />}></Route>
  <Route path="/contact" element={<Contact />}></Route>
</Routes>
</mid>
*/
