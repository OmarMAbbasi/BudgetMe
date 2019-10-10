import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import LoanOptions from "./loan_options";

export default class LoanFlow extends Component {
	render() {
		return (
			<div>
				<Switch>
					<Route exact path="/profile/loans/micro" />
					<Route exact path="/profile/loans/partner" />
					<Route path="/profile/loans" component={LoanOptions} />
				</Switch>
			</div>
		);
	}
}
