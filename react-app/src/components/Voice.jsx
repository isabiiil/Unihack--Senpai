import React from 'react';
import "./Voice.scss";

export default function Voice({ charName, charImg, voiceName, voiceImg }) {
  return (
    <div className="voice">
      <div className="names">
        <p>{charName}</p>
        <p>{voiceName}</p>
      </div>
      <div className="images">
        <img src={charImg} />
        <img src={voiceImg} />
      </div>
    </div>
  );
}