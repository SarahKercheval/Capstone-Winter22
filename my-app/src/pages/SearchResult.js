import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.css';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';
import starWars from '../images/S3.jpg';
import Netflix from '../images/netflix.jpg';
import Hulu from '../images/hulu.jpg';


const SearchResult = (props) => {
    const { title, genre, price, rating, foundTitle } = props

    return (
        <div className="SearchResult">
            <div className="searchHeader">
                <p id="searchResult">Search Results for "{title}"</p>
            </div>
            { foundTitle &&
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
                                {/* <th scope='row'><img src={ starWars } id="StarWars"/></th> */}
                                <td>Name: {title}<br />Genre: {genre}<br/>Price: {price}<br />Genre: {genre}</td>
                                <td><img src={Netflix} id="Netflix" /><img src={Hulu} id="Netflix" /></td>
                            </tr>
                            <tr>
                                {/* <th scope='row'><img src={starWars} id="StarWars" /></th> */}
                                <td>Name: {title}<br />Genre: {genre}<br />Price: {price}<br />Genre: {genre}</td>
                                <td><img src={Netflix} id="Netflix" /><img src={Hulu} id="Netflix" /></td>
                            </tr>
                        </MDBTableBody>
                    </MDBTable>
                </div>
            }
            { !foundTitle &&
                <div className='listMovies'>
                    Nothing found
                </div>
            }
        </div>
    )
}

export default SearchResult
