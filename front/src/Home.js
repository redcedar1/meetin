import React, { useEffect } from "react";

function Home() {
  useEffect(() => {
    const mid = document.querySelector(".mid");
    const blackCircle = document.querySelector(".black-circle");
    const minDimension = Math.min(mid.offsetWidth, mid.offsetHeight);
    blackCircle.style.width = (minDimension / 100) * 70 + "px";
    blackCircle.style.height = (minDimension / 100) * 70 + "px";
  }, []);
  return (
    <div class="black-circle">
      <div>
        <h2>Welcome to our website!</h2>
        <p>This is a basic React website.</p>
      </div>
    </div>
  );
}

export default Home;
