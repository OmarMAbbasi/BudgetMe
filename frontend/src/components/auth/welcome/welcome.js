import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class Welcome extends Component {
	render() {
		return (
			<div>
				<div>Slideshow Here</div>
				<NavLink to="/login">Login</NavLink>
				<NavLink to="/register">Register</NavLink>
			</div>
		);
	}
}
