import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";
import Portal from "./portal/portal";
import WelcomeContainer from "./welcome/welcome_container";

export default class Viewport extends Component {

	render() {
		return (
			<div>
				This Is The Viewport
				<Switch>
					<Route exact path="/portal" component={Portal} />
					<Route path="/" component={WelcomeContainer} />
				</Switch>
			</div>
		);
	}
}
