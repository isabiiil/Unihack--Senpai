import React from 'react';
import "./Search.scss";
import Navbar from "./../components/Navbar";
// npm install --save-dev @iconify/react @iconify-icons/gg
import { Icon, InlineIcon } from '@iconify/react';
import searchIcon from '@iconify-icons/gg/search';

import SearchResult from "./../components/SearchResult"

export default function Search() {
  return (
    <div className="search">
            <Navbar />
      <div className="search-bar">
        <p>Shoujo Anime <Icon className="icon" icon={searchIcon} /></p>
      </div>
      <SearchResult title="1" summary="yeet" />
      <SearchResult title="2" summary="yeet yeet" />
      <SearchResult title="3" summary="yeet yeet yeet" />
    </div>
  );
}