import React, { Component } from 'react'
import SearchBar from './SearchBar'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/nav'
import Container from 'react-bootstrap/Container'
import 'bootstrap/dist/css/bootstrap.css';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    useParams,
} from "react-router-dom";

const Home = () => {
        return (
            <div className="Home">
                <div className="content">
                    <p id="Title">Find Movies/TV Shows</p>
                    {/* <SearchBar /> */}
                </div>
            </div>
        )
}

export default Home