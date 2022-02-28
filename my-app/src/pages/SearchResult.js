import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.css';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';
import starWars from '../images/S3.jpg';
import Netflix from '../images/netflix.jpg';
import Hulu from '../images/hulu.jpg';

/*
const searchData = [
    {picture:, name: "Star Wars Revenge of The Sith", }
]
*/

const SearchResult = () => {
        return (
            <div className="SearchResult">
                <div className="searchHeader">
                    <p id="searchResult">Search Results for "...."</p>
                </div>
                <div className="searchContent">
                    <MDBTable className='listMovies' borderless>
                        <MDBTableHead>
                            <tr>
                                <th scope='col'></th>
                                <th scope='col'></th>
                                <th scope='col'>Available On:</th>
                            </tr>
                        </MDBTableHead>
                        <MDBTableBody>
                            <tr>
                                <th scope='row'><img src={ starWars } id="StarWars"/></th>
                                <td>Name: StarWars:Revenge of The Sith<br />Genre:Action<br/>Synopsis:</td>
                                <td><img src={Netflix} id="Netflix" /><img src={Hulu} id="Netflix" /></td>
                            </tr>
                            <tr>
                                <th scope='row'><img src={starWars} id="StarWars" /></th>
                                <td>Name: StarWars:Revenge of The Sith<br />Genre:Action<br />Synopsis:</td>
                                <td><img src={Netflix} id="Netflix" /><img src={Hulu} id="Netflix" /></td>
                            </tr>
                        </MDBTableBody>
                    </MDBTable>
                </div>
            </div>
        )
}

export default SearchResult
