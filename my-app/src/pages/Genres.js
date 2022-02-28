import React, { Component } from 'react'
import SearchGenre from './SearchGenre'
import 'bootstrap/dist/css/bootstrap.css';
import whiteImg from '../images/white.jpg';

const Genres = () => {
        return (
            <div className="Genres">
                <div className="content">
                    <div id="genre1">
                        <img src={whiteImg} class='genrePic' />
                        <img src={whiteImg} class='genrePic' />
                        <img src={whiteImg} class='genrePic' />
                    </div>
                    <div id="genre2">
                        <img src={whiteImg} class='genrePic' />
                        <img src={whiteImg} class='genrePic' />
                        <img src={whiteImg} class='genrePic' />
                    </div>
                    <div id="searchGenres">
                        <SearchGenre />
                    </div>
                </div>
            </div>
        )
}

export default Genres