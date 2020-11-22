import React from 'react';
import { Link } from "react-router-dom";
// npm install --save-dev @iconify/react @iconify-icons/ic
import { Icon, InlineIcon } from '@iconify/react';
import roundArrowBack from '@iconify-icons/ic/round-arrow-back';

// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

// import Avatar1 from "./../images/avatar2.png"

import "./Login.scss";

export default function Login() {
  return (
    <div className="login">
      <p><Link to="/"><Icon class="icon" icon={roundArrowBack} /></Link></p>
      <h1>Welcome back to MyAnime</h1>
      {/* <img className="avatar" src={Avatar1} /> */}
      <form>
        {/* <FontAwesomeIcon icon="user-circle" /> */}
        <i class="fas fa-unlock-alt"></i>
        <input type="text" placeholder="username"></input>
        {/* <FontAwesomeIcon icon="unlock-alt" /> */}
        <input type="password" placeholder="password"></input>
        <input type="submit" className="submit" value="Log In"></input>
      </form>
      <p>Have an account? Log in here.</p>
    </div>
  );
}