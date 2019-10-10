import React, { Component } from "react";
import { Route, NavLink } from "react-router-dom";

export default class Login extends Component {
	constructor(props) {
		super(props);
		this.state = {
			email: "",
			password: ""
		};
	}

	handleSubmit(e) {
		e.preventDefault();
		const user = Object.assign({}, this.state);
		if (!this.currentUser && this.currentUser.profileComplete) {
			this.props.login(user).then(() => this.props.history.push("/portal/"));
			return <Route to="/portal/" />;
		} else if (!this.currentUser && !this.currentUser.profileComplete) {
			this.props
				.login(user)
				.then(() => this.props.history.push("/register/profile"));
			return <Route to="/register/profile" />;
		} else {
			this.setState({ errors: "Not Logged In" });
		}
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
				<form onSubmit="">
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
				</form>
				<NavLink to="/register">Register</NavLink>
			</div>
		);
	}
}
