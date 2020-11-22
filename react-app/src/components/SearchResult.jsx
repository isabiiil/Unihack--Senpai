import React from 'react';
import './SearchResult.scss';

export default function SearchResult({ title, img, rating, summary }) {
  return (
    <div className="search">
      <img src={img}></img>
      <div className="text">
        <p><strong>Title: </strong>{title}</p>
        <p><strong>Overall Rating: </strong>{rating}</p>
        <p><strong>Summary: </strong>{summary}</p>
      </div>
    </div>
  );
}