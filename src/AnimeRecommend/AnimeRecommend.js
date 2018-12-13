import React, { Component } from 'react';
import './AnimeRecommend.css';
import Background from '../img/404.jpg';
import axios from 'axios';

class AnimeRecommend extends Component {

  constructor() {
    super();

    this.state = {
      username: ''
    };

    this.sendQuery = this.sendQuery.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    this.setState({
      username: e.target.value
    });
  }

  sendQuery(e) {
    e.preventDefault();

    let port = process.env.PORT || 5000;
    axios.get("http://localhost:" + port + "/recommend", {
      params: {
        username: this.state.username
      }
    })
      .then(res => {
        console.log(res);
      })
      .catch(error => {
        console.error(error);
      });

  }

  render() {
    return (
      <div className="anime-recommend">
        <img className="bg-img" src={Background} alt="" />
        <div className="anime-recommend-content">
          <form onSubmit={this.sendQuery}>
            <label className="username" htmlFor="username">Enter Username</label>
            <input className="form-control mr-sm-2" placeholder="Bob" type="text" required autoComplete="off" onChange={this.handleChange} /><br />
            <button className="btn btn-success" type="submit">Recommend Me!</button>
          </form>
        </div>
      </div>
    )
  }

}

export default AnimeRecommend;