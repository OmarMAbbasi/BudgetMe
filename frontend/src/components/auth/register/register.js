import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class Register extends Component {
	render() {
		return (
			<div>
				Register Form
				<NavLink to="/login">Login</NavLink>
			</div>
		);
	}
}
