import React, { Component, useState } from 'react'
import { FaSearch } from 'react-icons/fa'
import { Checkbox, Row, Col } from 'antd'
import SearchResult from './SearchResult';
import SearchResultList from './SearchResultList'

function onChange(checkedValues) {
    console.log('checked = ', checkedValues);
}

const options1 = ['Any', 'Netflix', 'Hulu', 'Paramount'];
const options2 = ['Free', '< $2.99', '< $5.99', 'Any amount'];

const SearchBar = () => {
    const [movieTitle, setMovieTitle] = useState('')
    const [searchResult, setSearchResult] = useState([{"name": ""}])

    const onSubmitClick = (e) => {
        console.log('about to request movie: ' + movieTitle.trim())
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
            // setSearchResult({
            //     ...searchResult,
            //     "name": movieTitle
            // })
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
                </Checkbox.Group>
            </div>
            { !!searchResult &&
                <div id="SearchResultList">
                    <SearchResultList
                        searchList={searchResult}
                        title={movieTitle.trim()}
                    />
                </div>
            }   

        </div>
    );
}

export default SearchBar
