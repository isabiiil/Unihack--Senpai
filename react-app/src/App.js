import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

// import { library } from '@fortawesome/fontawesome-svg-core'
// import { fas } from '@fortawesome/free-brands-svg-icons'
// import { faUserCircle, faEnvelope, faUnlockAlt } from '@fortawesome/free-solid-svg-icons'

import Register from "./pages/Register";
import Login from "./pages/Login";
import Navbar from "./components/Navbar";
import Profile from "./pages/Profile";
import Search from "./pages/Search";
import Swipe from "./pages/Swipe";
import './App.css';

// library.add(fas, faUserCircle, faEnvelope, faUnlockAlt);

export default function App() {
  return (
    <div className="App">
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/nav">Nav</Link>
              </li>
              <li>
                <Link to="/profile">Profile</Link>
              </li>
              <li>
                <Link to="/search">Search</Link>
              </li>
              <li>
                <Link to="/swipe">Swipe</Link>
              </li>
            </ul>
          </nav>

          {/* A <Switch> looks through its children <Route>s and
              renders the first one that matches the current URL. */}
          <Switch>
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/nav">
              <Navbar />
            </Route>
            <Route path="/profile">
              <Profile />
            </Route>
            <Route path="/search">
              <Search />
            </Route>
            <Route path="/swipe">
              <Swipe />
            </Route>
            <Route path="/">
              <Register />
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}