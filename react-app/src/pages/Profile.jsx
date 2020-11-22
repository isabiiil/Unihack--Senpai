import React from 'react';

import Navbar from "./../components/Navbar";
import Avatar from "./../images/avatar2.png";
import "./Profile.scss";

export default function Profile() {
  return(
    <div className="profile">
      <Navbar />
      <div className="content">
        <div className="col1">
          <img className="prof" src={Avatar} />
          <div className="header">
            <p>AnimeLover99</p>
          </div>
          <div className="bio">
            <p>I started watching anime in 2016 after I picked up reading manga. Fairytail is a classic that I have both read and watched in its entirety. I am a sucker for romance and anything we pretty art. I am also get very emotional, so any anime that pulls at my heartstrings has a special place in my kokoro.</p>
            <button>Edit Profile</button>
          </div>
        </div>
        <div className="col2">
          <div className="header">
            <p>Recommended For You</p>
          </div>
          <div className="col-container">
            <img src={Avatar} />
            <img src={Avatar} />
            <button>Refresh</button>
          </div>
        </div>
        <div className="col3">
          <div className="header">
            <p>Lifetime Hours</p>
          </div>
          <div className="col-container">
            <img src={Avatar} />
            <div className="col-text">
              <p>You have watched 3500 hours of anime.</p>
              <p>You have reached WEEB status.</p>
              <p>Watch 5200 more hours to reach LEGENDARY status.</p>
            </div>
          </div>
        </div>
        <div className="col4">
          <div className="header">
            <p>Latest Watched</p>
          </div>
          <div className="col-container">
            <img src={Avatar} />
            <img src={Avatar} />
            <button>Add More</button>
          </div>
        </div>
      </div>
    </div>
  );
}