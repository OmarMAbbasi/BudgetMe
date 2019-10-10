import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";
import SettingsContainer from "./settings/settings_container";

export default class Profile extends Component {
	render() {
		return (
			<div className="main-app">
				Profile
				<Switch>
					<Route path="/profile/settings" component={SettingsContainer} />
				</Switch>
			</div>
		);
	}
}
