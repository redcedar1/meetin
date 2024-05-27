import React, { useEffect } from "react";

function Footer() {
  useEffect(() => {
    const footer = document.querySelector(".footer");
    const bottonBox = document.querySelector(".botton-box");
    bottonBox.style.width = (footer.offsetWidth / 100) * 35 + "px";
    bottonBox.style.height = footer.offsetHeight + "px";

    const botton = document.querySelectorAll(".botton");
    botton.forEach(function (botton) {
      botton.style.width = (footer.offsetHeight / 100) * 65 + "px";
      botton.style.height = (footer.offsetHeight / 100) * 65 + "px";
    });
  }, []);
  return (
    <div class="footer">
      <div class="botton-box">
        <div class="botton">
          <p>coffee</p>
        </div>
        <div class="botton">
          <p>meal</p>
        </div>
        <div class="botton">
          <p>club</p>
        </div>
      </div>
    </div>
  );
}

export default Footer;
