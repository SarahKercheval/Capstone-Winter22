import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.css';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';
import moPic from '../images/S3.jpg';
import netflix from '../images/netflix.jpg';
import hulu from '../images/hulu.jpg';
import prime from '../images/prime video.png';

/*
const info = [
    { name: 'Star Wars: Revenge of The Sith'},
];
*/

const Movies = () => {
    return (
        <div className="Movies">
            <div id='mTitle'>
                <p id="Title">Star Wars Revenge of The Sith</p>
            </div>
            <div id="hori">
            <div id='mPicture'>
                <img src={moPic} alt="MoPic" />
            </div>
            <div id='synopsis'>
                Three years into the Clone Wars, the Jedi rescue Palpatine from Count Dooku.<br/> 
                As Obi-Wan pursues a new threat, Anakin acts as a double agent between the Jedi<br/>
                Council and Palpatine and is lured into a sinister plan to rule the galaxy.
                <br />
                <br />
                <table id="streaming">
                        <tr>
                            <td><img src={netflix} id="Netflix" /></td>
                            <td>$9.99</td>
                            <td><a href="">View</a></td>
                        </tr>
                            <td><img src={hulu} id="Netflix" /></td>
                            <td>$9.99</td>
                            <td><a href="">View</a></td>
                </table>
            </div>
            </div>
            <div id='information'>
                Name:<br />
                Rating:<br />
                Casts:<br/>
            </div>
        </div>
        )
}

export default Movies
