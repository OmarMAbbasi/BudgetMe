import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";
import SettingsContainer from "./settings/settings_container";
import Home from "./home";
export default class Profile extends Component {
	render() {
		return (
			<div className="main-app">
				<Switch>
					<Route path="/profile/settings" component={SettingsContainer} />
					<Route path="/profile/loans" />
					<Route path="/profile" component={Home} />>
				</Switch>
			</div>
		);
	}
}
