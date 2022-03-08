import React, { Component } from 'react'
import SearchGenre from './SearchGenre'
import 'bootstrap/dist/css/bootstrap.css';
import action from '../images/action.png';
import adventure from '../images/adventure.png';
import drama from '../images/drama.png';
import horror from '../images/horror.png';
import romance from '../images/romance.png';
import scifi from '../images/sci-fi.png';

const Genres = () => {
        return (
            <div className="Genres">
                <div className="content">
                    <div id="genre1">
                        <img src={action} class='genrePic' />
                        <img src={adventure} class='genrePic' />
                        <img src={drama} class='genrePic' />
                    </div>
                    <div id="genre2">
                        <img src={horror} class='genrePic' />
                        <img src={romance} class='genrePic' />
                        <img src={scifi} class='genrePic' />
                    </div>
                    <div id="searchGenres">
                        <SearchGenre />
                    </div>
                </div>
            </div>
        )
}

export default Genres