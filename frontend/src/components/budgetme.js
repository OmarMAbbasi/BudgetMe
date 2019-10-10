import React, { Component } from "react";
import { Switch } from "react-router-dom";
import Profile from "./portal/profile/profile_container";
import Auth from "./auth/auth_container";

export default class BudgetMe extends Component {
	render() {
		return (
			<Switch>
				<Profile path="/profile" />
				<Auth path="/" />
			</Switch>
		);
	}
}
