import RefAutoComplete from 'antd/lib/auto-complete'
import React, { Component, useState } from 'react'
import SearchResult from './SearchResult'

function SearchResultList(props) {

    const {searchList, title} = props
    let result = searchList[0]
    return (<div>
                <div className="searchHeader">
                <p id="searchResult">Search Results for "{title}"</p>
            </div>
                {searchList.map( result =>
                    <SearchResult
                        title={result.name.trim()} 
                        genre={result.genre} 
                        price={result.price} 
                        rating={result.rating}
                        foundTitle={"link" in result}
                    />
                )}
            </div>)
}
export default SearchResultList