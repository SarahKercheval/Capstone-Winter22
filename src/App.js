import React, { Component, useState, UseEffect, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import NavBar from './components/NavBar';
import './index.css';
import SearchResult from './pages/SearchResult';
import Movies from './pages/Movies';
import 'bootstrap/dist/css/bootstrap.css';
import Genres from './pages/Genres';
import Faq from './pages/faq';

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
            <div className="App">
                <Router>
                    <NavBar />
                    <Routes>
                        <Route path="/home" element={<Home />} />
                        <Route path="/search-result" element={<SearchResult />} />
                        <Route path="/movies" element={<Movies />} />
                        <Route path="/genres" element={<Genres />} />
                        <Route path="/faq" element={<Faq />} />
                    </Routes>
                 </Router>
            </div>    
        )
}

export default App;
