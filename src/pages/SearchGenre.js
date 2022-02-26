import React, { Component } from 'react'
import { FaSearch } from 'react-icons/fa'
import { Checkbox, Row, Col } from 'antd'

function onChange(checkedValues) {
    console.log('checked = ', checkedValues);
}

const options1 = ['Any', 'Netflix', 'Hulu', 'Amazon Prime'];
const options2 = ['Free', '< $2.99', '< $5.99h', 'Any amount'];
const options3 = ['English', 'Spanish', 'Chinese', 'Japanese'];
const options4 = ['Yes', 'No'];

const SearchGenre = () => (
    <div className="wrap">
        <div className="search">
            <form action="/" method="get">
                <input type="text" id="movies-search" placeholder="Search for Genres or SubGenres" name="s" />
                <button type="submit" className="searchBtn"><FaSearch id="searchIcon" /></button>
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
    </div>
);

export default SearchGenre
