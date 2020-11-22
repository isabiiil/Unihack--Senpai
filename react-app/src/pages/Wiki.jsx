import React from 'react';
import './Wiki.scss';

import Navbar from './../components/Navbar';
import Voice from './../components/Voice';
import Avatar from "./../images/avatar2.png";

export default function Wiki() {
  return (
    <div className="wiki">
      <Navbar />
      <div className="content">
        <div className="banner">
          <img src={Avatar} />
          <div className="title">
            <h1>Shigatsu wa Kimi no Uso</h1>
          </div>
        </div>
        <div className="row1">
          <div className="info">
            <p>Type: TV
            Episodes: 22
            Status: Complete
            Aired: Oct 10, 2014 - Mar 20, 2015
            Producers: Aniplex, Dentsu, Kodansha, Fuji TV, Kyoraku Industrial Holdings
            Studios: A-1 Pictures
            Source: Manga
            Genres: Drama, Music, Romance, School, Shounen
            Duration: 22 min.
            Rating: PG-13 </p>
          </div>
          <div className="synopsis">
            <p>Music accompanies the path of the human metronome, the prodigious pianist Kousei Arima. But after the passing of his mother, Saki Arima, Kousei falls into a downward spiral, rendering him unable to hear the sound of his own piano.

            Two years later, Kousei still avoids the piano, leaving behind his admirers and rivals, and lives a colorless life alongside his friends Tsubaki Sawabe and Ryouta Watari. However, everything changes when he meets a beautiful violinist, Kaori Miyazono, who stirs up his world and sets him on a journey to face music again.

            Based on the manga series of the same name, Shigatsu wa Kimi no Uso approaches the story of Kousei's recovery as he discovers that music is more than playing each note perfectly, and a single melody can bring in the fresh spring air of April.</p>
            <p>*stars*</p>
            <p>ranking</p>
            <button>Add to List</button>
          </div>
        </div>
        <div className="row2">
          <div className="episode-image">
            <img src={Avatar} />
            <img src={Avatar} />
            <img src={Avatar} />
            <img src={Avatar} />
          </div>
          <div className="episode-title">
            <p>Episode 1</p>
            <p>Episode 2</p>
            <p>Episode 3</p>
            <p>Episode 4</p>
          </div>
        </div>
        <div className="row3">
          
        </div>
      </div>
    </div>
  );
}