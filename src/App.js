import React, { Component } from 'react'
import SearchBar from './SearchBar'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/nav'
import Container from 'react-bootstrap/Container'
import 'bootstrap/dist/css/bootstrap.css';

class Home extends Component {
    render() {
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
}

export default Home
