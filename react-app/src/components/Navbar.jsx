import React from 'react';
import "./Navbar.scss";

export default function Navbar() {
  return (
    <div className="navbar">
      <h3>MyAnime</h3>
      <div className="right">
        <p>Home</p>
        <p>Recommendations</p>
        <form className="searchbar">
          <input type="text" placeholder="Search for an anime"></input>
          <input type="submit" value="submit"></input>
        </form>
      </div>
    </div>
  );
}