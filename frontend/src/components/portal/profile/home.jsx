import React, { Component } from "react";
import PieChart from "../../../styles/assets/Images/pie_chart.png";
import SliderOne from "../../../styles/assets/Images/budget_sliders/Slider1.png";
import SliderTwo from "../../../styles/assets/Images/budget_sliders/Slider2.png";
import SliderThree from "../../../styles/assets/Images/budget_sliders/Slider3.png";
import SliderFour from "../../../styles/assets/Images/budget_sliders/Slider4.png";
import NavButton from "../../../styles/assets/Images/nav_icons/NavigatorButton.png";

export default class Home extends Component {
	render() {
		return (
			<div className="home-wrapper">
				<img src={PieChart} className="pie-chart"></img>
				<ul className="budget-status">
					<li>
						<img className="slider-image" src={SliderOne}></img>
					</li>
					<li>
						<img className="slider-image" src={SliderTwo}></img>
					</li>
					<li>
						<img className="slider-image" src={SliderThree}></img>
					</li>
					<li>
						<img className="slider-image" src={SliderFour}></img>
					</li>
				</ul>
			</div>
		);
	}
}
