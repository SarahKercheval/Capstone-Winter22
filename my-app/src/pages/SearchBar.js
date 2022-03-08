import React, { Component, useState } from 'react'
import { FaSearch } from 'react-icons/fa'
import { Checkbox, Row, Col } from 'antd'
import SearchResult from './SearchResult';

function onChange(checkedValues) {
    console.log('checked = ', checkedValues);
}

const options1 = ['Any', 'Netflix', 'Hulu', 'Amazon Prime'];
const options2 = ['Free', '< $2.99', '< $5.99', 'Any amount'];
const options3 = ['English', 'Spanish', 'Chinese', 'Japanese'];
const options4 = ['Yes', 'No'];

const SearchBar = () => {
    const [movieTitle, setMovieTitle] = useState('')
    const [searchResult, setSearchResult] = useState({"name": ""})

    const onSubmitClick = (e) => {
        console.log('about to request movie: ' + movieTitle)
        fetch('http://127.0.0.1:5000/search-result/' + movieTitle, {
            "method": "POST",
            "headers": {
                "Access-Control-Allow-Origin": true
            }
        }).then(response => {
            if (response.ok) {
                response.json().then(body => {
                    console.log('fetch result: ' + JSON.stringify(body))
                    setSearchResult(body)
                })
            } else {
                setSearchResult({"name": movieTitle})
            }
        })
    }

    return(
        <div className="wrap">
            <div className="search">
                <form 
                    action="/" 
                    method="get"
                    onSubmit={(event) => {
                        event.preventDefault()
                    }}>
                    <input 
                        type="text" 
                        id="movies-search" 
                        placeholder="Search for TV or Movies" 
                        name="s"
                        onChange={(event) => {
                            setMovieTitle(event.target.value)
                        }}
                        />
                    <button type="submit" className="searchBtn"><FaSearch id="searchIcon"
                        onClick={onSubmitClick} /></button>
                </form>
            </div >
            <div className="filters">
                <label>Filters:</label>
                <br />
                <Checkbox.Group onChange={onChange}>
                    <label>Streaming Services:</label>
                    <Checkbox.Group options={options1} onChange={onChange} />
                    <br />
                    <label>Price:</label>
                    <Checkbox.Group options={options2} onChange={onChange} />
                    <br />
                    <label>Language:</label>
                    <Checkbox.Group options={options3} onChange={onChange} />
                    <br />
                    <label>Subtitle:</label>
                    <Checkbox.Group options={options4} onChange={onChange} />
                </Checkbox.Group>
            </div>
            { !!searchResult.name &&
                <div>
                    <SearchResult 
                        title={searchResult.name} 
                        genre={searchResult.genre} 
                        price={searchResult.price} 
                        rating={searchResult.rating}
                        foundTitle={"link" in searchResult} />
                </div>
            }
        </div>
    );
}

export default SearchBar
