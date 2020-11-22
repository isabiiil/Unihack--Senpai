import React from 'react';
import './Swipe.scss';

import Navbar from "./../components/Navbar";
import No from "./../images/no.png";
import Yes from "./../images/yes.png";
import Avatar from "./../images/avatar2.png";

export default function Swipe() {
  return(
    <div className="swipe">
      <Navbar />
      <div className="content">
        <h1>Swipe on animes that interest you</h1>
        <div className="main">
          <img src={No} className="icon" />
          <img src={Avatar} />
          <img src={Yes} className="icon" />
        </div>
      </div>
    </div>
  );
}