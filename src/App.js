import React, { Component, useState, UseEffect, useEffect } from 'react'
import SearchBar from './SearchBar'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/nav'
import Container from 'react-bootstrap/Container'
import 'bootstrap/dist/css/bootstrap.css';

//fetching from server.py flask 

function App() {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/home").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

    return (
        <div className="Home">
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="#home">MoviesSearch</Navbar.Brand>
                <Nav className="ms-auto">
                    <Nav.Link href="#home">Home</Nav.Link>
                    <Nav.Link href="#Genres">Genres</Nav.Link>
                    <Nav.Link href="#FAQ">FAQ</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
        <div className="content">
            <p id="Title">Find Movies/TV Shows</p>
            <SearchBar />
        </div>
    </div>
    )
}

export default App