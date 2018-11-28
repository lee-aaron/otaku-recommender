import React, { Component } from 'react';
import './App.css';
import './bootstrap.css';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import HomePage from './Home/HomePage';
import AnimeRecommend from './AnimeRecommend/AnimeRecommend';

function make_link(path, text) {
  return (
    <div className="nav-item" key={path}>
      <Link className="nav-link" to={path}>{text}</Link>
    </div>
  )
}

class App extends Component {
  render() {
    let navItems = [
      ["/", "Home"],
      ["/donate", "Donate"],
      ["/about", "About"],
      ["/contact", "Contact"]
    ].map((item) => make_link.apply(null, item));
    let name = "Otaku Recommender";
    return (
      <Router>
        <div className="App">
          <nav className="navbar navbar-expand bg-light">
            <Link className="navbar-brand" to='/' >
              <div>{name}</div>
            </Link>
            <div className="navbar-collapse">
              <div className="navbar-nav ml-auto">
                { navItems }
              </div>
            </div>
          </nav>
          <Route exact path="/" component={ HomePage } />
          <Route exact path="/donate" />
          <Route exact path="/about" />
          <Route exact path="/contact" />
          <Route exact path="/anime-recommend" component={AnimeRecommend} />
        </div>
      </Router>
    );
  }
}

export default App;
