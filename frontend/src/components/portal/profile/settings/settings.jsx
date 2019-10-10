import React, { Component } from "react";
import { Switch, Route, NavLink } from "react-router-dom";

import Budget from "./budget";
import Info from "./info";

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
			currentView: <span>toEULA</span>,
			nextButton: this.finishRegistration
		});
	};

	finishRegistration = () => {
		this.props.history.push("/profile");
	};

	render() {
		return (
			<div>
				{this.state.currentView}
				<button onClick={this.state.nextButton}>Next Button</button>
			</div>
		);
	}
}
