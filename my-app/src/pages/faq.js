import React, { Component } from 'react'
import SearchBar from './SearchBar'
import 'bootstrap/dist/css/bootstrap.css';
import Collapsible from 'react-collapsible';

const faq = () => {
        return (
            <div className="faq">
                <div className="content">
                    <Collapsible trigger="Who are we?" class='cola'>
                        We are undergraduate students currently studying at Central Washington University.
                        This is our capstone project. Our supervisor is Razvan Andonie, team leader is Sarah Kercheval, 
                        and team members are Kahle Broadnax, Preston Fenimore, Ben Yokoyama, and Robin Purnama. 
                    </Collapsible>
                    <Collapsible trigger="What is Find That Show?" class='cola'>
                        Find That Show is our capstone project for Central Washington University Winter 2022. It's a show 
                        that allows users to quickly and easily find which streaming services shows are on. 
                    </Collapsible>
                    <Collapsible trigger="How can you get in contact with us?" class='cola'>
                        You can find our project on github at "https://github.com/SarahKercheval/Capstone-Winter22". Our
                        emails are accessible on there. 
                    </Collapsible>
                </div>
            </div>
        )
}

export default faq