import React, { Component, useState, UseEffect, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import NavBar from './components/NavBar/Navigation';
import './index.css';
import Movies from './pages/Movies';
import 'bootstrap/dist/css/bootstrap.css';
import Genres from './pages/Genres';
import Faq from './pages/faq';

function App() {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("http://127.0.0.1:5000/home").then(
            res => res.json()
        ).then(
            data => {
                console.log('home fetch: ' + JSON.stringify(data))
                setData(data)
                console.log(data)
            }
        )
    }, [data])

        return (   
            <div className="App">
                <Router>
                    <NavBar />
                    <Routes>
                        <Route path="/home" element={<Home />} />
                        <Route path="/Capstone-Winter22" element={<Home />} />
                        <Route path="/movies" element={<Movies />} />
                        <Route path="/genres" element={<Genres />} />
                        <Route path="/" element={<Home />} />
                        <Route path="/faq" element={<Faq />} />
                    </Routes>
                 </Router>
            </div>    
        )
}

export default App;
