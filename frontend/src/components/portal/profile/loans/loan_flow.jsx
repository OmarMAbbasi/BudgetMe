import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import LoanOptions from "./loan_options";
import MicroRequest from "./micro/micro_request";

export default class LoanFlow extends Component {
	render() {
		return (
			<Switch>
				<Route exact path="/profile/loans/micro" component={MicroRequest} />
				<Route exact path="/profile/loans/partner" />
				<Route path="/profile/loans" component={LoanOptions} />
			</Switch>
		);
	}
}
