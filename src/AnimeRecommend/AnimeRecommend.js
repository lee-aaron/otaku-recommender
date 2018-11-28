import React, { Component } from 'react';
import './AnimeRecommend.css';
import Background from '../img/404.jpg';

class AnimeRecommend extends Component {

  render() {
    return (
      <div className="anime-recommend">
        <img className="bg-img" src={Background} />
      </div>
    )
  }

}

export default AnimeRecommend;