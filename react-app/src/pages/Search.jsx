import React from 'react';
import "./Search.scss";

import SearchResult from "./../components/SearchResult"

export default function Search() {
  return (
    <div className="search">
      <div className="search-bar">
        <p>Shoujo Anime</p>
      </div>
      <SearchResult title="1" summary="yeet" />
      <SearchResult title="2" summary="yeet yeet" />
      <SearchResult title="3" summary="yeet yeet yeet" />
    </div>
  );
}