import React, { Component } from "react";
import { Route, NavLink } from "react-router-dom";

export default class Login extends Component {
	constructor(props) {
		super(props);
		this.state = {
			email: "",
			password: ""
		};
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleSubmit(e) {
		e.preventDefault();
		this.props.history.push("/portal");
	}

	update(field) {
		return e =>
			this.setState({
				[field]: e.currentTarget.value
			});
	}
	render() {
		return (
			<div>
				Login Form
				<form className="form-holder" onSubmit={this.handleSubmit}>
					<input
						type="email"
						value={this.state.email}
						onChange={this.update("email")}
					></input>
					<input
						type="password"
						value={this.state.password}
						onChange={this.update("password")}
					></input>
					<input type="submit" value="Login" className="submit-buttons"></input>
				</form>
				<NavLink to="/register">Register</NavLink>
			</div>
		);
	}
}
