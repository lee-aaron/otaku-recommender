import React, { Component } from 'react';
import './HomePage.css';
import { Route } from 'react-router-dom';

class HomePage extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        let welcome = "Welcome to Otaku Recommender!";
        return (
            <div>
                <h1 className="info">{welcome}</h1>
                <Route exact path="/anime-recommendation" />
            </div>
        )
    }
}

export default HomePage;