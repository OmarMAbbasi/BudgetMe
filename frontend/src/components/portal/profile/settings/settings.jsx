import React, { Component } from "react";
import { Switch, Route, NavLink } from "react-router-dom";
import Budget from "./budget";
import Info from "./info";
import EULAAgreement from "../eula";
import nextButton from "../../../../styles/assets/Images/nav_icons/NextButton.png";
export default class Settings extends Component {
	constructor(props) {
		super(props);
		this.toBudget = this.toBudget.bind(this);
		this.toEULA = this.toEULA.bind(this);
		this.finishRegistration = this.finishRegistration.bind(this);
		this.state = {
			currentView: <Info />,
			nextButton: this.toBudget
		};
	}

	toBudget = () => {
		this.setState({ currentView: <Budget />, nextButton: this.toEULA });
	};

	toEULA = () => {
		this.setState({
			currentView: <EULAAgreement />,
			nextButton: this.finishRegistration
		});
	};

	finishRegistration = () => {
		
		this.props.history.push("/profile");
	};

	render() {
		return (
			<div className="setup-flow">
				{this.state.currentView}
				<div className="next-button-wrapper" onClick={this.state.nextButton}>
					<img
						style={{ height: "20vw", width: "20vw;" }}
						src={nextButton}
					></img>
				</div>
			</div>
		);
	}
}
