import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";
import SettingsContainer from "./settings/settings_container";
import NavButton from "../../../styles/assets/Images/nav_icons/NavigatorButton.png";
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
				<div className="nav-button-wrapper">
					<Switch>
						<Route exact path="/profile/settings" />
						<Route
							path="/profile"
							component={() => {
								return (
									<img
										style={{ height: "20vw", width: "20vw" }}
										src={NavButton}
									></img>
								);
							}}
						/>
					</Switch>
				</div>
			</div>
		);
	}
}
