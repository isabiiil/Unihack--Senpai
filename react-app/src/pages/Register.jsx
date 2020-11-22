import React from 'react';
import { Link } from "react-router-dom";
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import Avatar1 from "./../images/avatar2.png"

import "./Register.scss";

export default function Register() {
  return (
    <div className="register">
      <h1>Join the MyAnime Community</h1>
      <p>Choose avatar</p>
      <form>
        <div className="avatars">
          <label><input type="radio"></input><img className="avatar" src={Avatar1} /></label>
          <label><input type="radio"></input><img className="avatar" src={Avatar1} /></label>
          <label><input type="radio"></input><img className="avatar" src={Avatar1} /></label>
        </div>
        {/* <FontAwesomeIcon icon="user-circle" /> */}
        <i class="fas fa-unlock-alt"></i>
        <input type="text" placeholder="username"></input>
        {/* <FontAwesomeIcon icon="envelope" /> */}
        <input type="email" placeholder="email"></input>
        {/* <FontAwesomeIcon icon="unlock-alt" /> */}
        <input type="password" placeholder="password"></input>
        <input type="submit" className="submit" value="Create Account"></input>
      </form>
      <p>Have an account? <Link to="/login">Log in here.</Link></p>
    </div>
  );
}