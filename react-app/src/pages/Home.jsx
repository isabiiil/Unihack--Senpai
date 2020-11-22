import React from 'react';
import { Link } from "react-router-dom";
import "./Home.scss";

import Navbar from "./../components/Navbar";
import Avatar from "./../images/avatar2.png";

export default function Home() {
  return (
    <div className="home">
      <Navbar />
      <img className="main-img"src={Avatar} />
      <div className="featured-title">
        <p>Kimi ni Na wa.</p>
      </div>
      <div className="list">
        <img src={Avatar} />
        <img src={Avatar} />
        <img src={Avatar} />
        <img src={Avatar} />
        <img src={Avatar} />
      </div>
    </div>
  );
}