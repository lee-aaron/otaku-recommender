import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';

class App extends Component {
  render() {
    let name = "Otaku Recommender";
    return (
      <Router>
        <div className="App">
          <nav className="search-bar navbar navbar-expand-md navbar-light fixed-top">
            <Link className="navbar-brand" to="/">
              <div>{name}</div>
            </Link>
          </nav>
        </div>
      </Router>
    );
  }
}

export default App;
