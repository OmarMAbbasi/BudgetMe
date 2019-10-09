import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class Login extends Component {
	render() {
		return (
			<div>
				Login Form
				<NavLink to="/register">Register</NavLink>
			</div>
		);
	}
}
