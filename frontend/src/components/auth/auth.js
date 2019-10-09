import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";
import RegisterContainer from "./register/register_container";
import LoginContainer from "./login/login_container";
export default class BudgetMe extends Component {
	render() {
		return (
			<div>
				<Switch>
					<Route exact path="/register" component={RegisterContainer} />
					<Route exact path="/login" component={LoginContainer} />
				</Switch>
			</div>
		);
	}
}
