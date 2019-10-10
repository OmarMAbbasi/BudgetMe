import React, { Component } from "react";
import SliderOne from "../../../../styles/assets/Images/budget_sliders/Slider1.png";
import SliderTwo from "../../../../styles/assets/Images/budget_sliders/Slider2.png";
import SliderThree from "../../../../styles/assets/Images/budget_sliders/Slider3.png";
import SliderFour from "../../../../styles/assets/Images/budget_sliders/Slider4.png";
export default class Budget extends Component {
	render() {
		return (
			<div>
				<ul className="budget-sliders">
					<span className="budget-prompt">
						How Much Would You Like To Spend?
					</span>
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
