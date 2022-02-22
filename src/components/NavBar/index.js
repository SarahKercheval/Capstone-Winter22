import React from "react";
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/nav'
import Container from 'react-bootstrap/Container'

const Navigation = () => {
    return (
        <>
            <Navbar bg="dark" variant="dark">
                <Container>
                    <Navbar.Brand href="/home">MoviesSearch</Navbar.Brand>
                    <Nav className="ms-auto">
                        <Nav.Link href='/home'>Home</Nav.Link>
                        <Nav.Link href='/movies'>Genres</Nav.Link>
                        <Nav.Link href="/search-result">FAQ</Nav.Link>
                    </Nav>
                </Container>
            </Navbar>
        </>
    );
};

export default Navigation;
