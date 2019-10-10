import React, { Component } from 'react';
import SliderExpanded from '../../styles/assets/Images/Microloan/FundSomeoneExpanded.png';
import Slider2 from '../../styles/assets/Images/Microloan/FundSomeone2.png';
import Slider1 from "../../styles/assets/Images/Microloan/FundSomeone.png";
import classes from "./MicroLoan.module.css";
import NavigationBar from "../../styles/assets/Images/nav_icons/NavigatorButtonBlue.png";

export class MicroLoan extends Component {
    // Request Fund - 0 
    // Fund Someone - 1

    state = {
        toview: 0,
        seemore: 0,
    }


    render() {
        return (
            <div className={classes.Outer}>               
                <div className={classes.Loans}>
                    <img alt="0" src={Slider1}></img>
                    <img alt="1" src={Slider2}></img>
                </div>
            </div>
        )
    }
}

export default MicroLoan
