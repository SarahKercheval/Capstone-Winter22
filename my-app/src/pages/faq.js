import React, { Component } from 'react'
import SearchBar from './SearchBar'
import 'bootstrap/dist/css/bootstrap.css';
import Collapsible from 'react-collapsible';

const faq = () => {
        return (
            <div className="faq">
                <div className="content">
                    <Collapsible trigger="Q1" class='cola'>
                        Answer here
                    </Collapsible>
                    <Collapsible trigger="Q2" class='cola'>
                        Answer here
                    </Collapsible>
                </div>
            </div>
        )
}

export default faq