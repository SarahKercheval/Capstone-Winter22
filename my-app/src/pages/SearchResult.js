import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';
import Netflix from '../images/netflix.jpg';
import Hulu from '../images/hulu.jpg';
import Paramount from '../images/paramount.png'


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
                                <td>Name: {title}<br />Genre: {genre}<br/>Price: {price}</td>
                                <td>
                                    <img src={Netflix} id="Netflix" alt="Netflix"/>
                                    <img src={Hulu} id="Netflix" alt="Netflix"/>
                                    <img src={Paramount} id="Netflix" alt="Paramount"/>
                                </td>
                            </tr>
                            <tr>
                                <td>Name: {title}<br />Genre: {genre}<br />Price: {price}</td>
                                <td>
                                    <img src={Netflix} id="Netflix" alt="Netflix"/>
                                    <img src={Hulu} id="Netflix" alt="Hulu"/>
                                    <img src={Paramount} id="Netflix" alt="Paramount"/>
                                </td>
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
