import React, { Component } from 'react';
import './HomePage.css';
import Home from '../img/index.jpg';
import { Route } from 'react-router-dom';

class HomePage extends Component {

    render() {
        let welcome = "Welcome to Otaku Recommender!";

        const Button = () => (
            <Route render={({history}) => (
                <button
                    id="home_page"
                    type="button"
                    onClick={() => { history.push("/anime-recommend") }}>
                    Click here to get started!
                </button>
            )} />
        )

        return (
            <div>
                <img className="bg-img" src={Home} ></img>
                <div className="home_page_content">
                    <h1 className="info spacing">{welcome}</h1>
                    <Button />
                </div>
                <Route exact path="/anime-recommendation" />
            </div>
        )
    }
}

export default HomePage;