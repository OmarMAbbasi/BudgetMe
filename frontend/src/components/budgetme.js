import React, { Component } from "react";
import { Switch } from "react-router-dom";
import Portal from "./portal/portal_container";
import Auth from "./auth/auth_container";

export default class BudgetMe extends Component {
	render() {
		return (
			<div>
				<Switch>
					<Portal exact path="/portal" />
					<Auth path="/" />
				</Switch>
			</div>
		);
	}
}
