import React, { Component } from "react";
import { Route, NavLink } from "react-router-dom";

export default class Register extends Component {
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
		if (!this.currentUser) {
			this.props
				.register(user)
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
				Register Form
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
				<NavLink to="/login">Login</NavLink>
			</div>
		);
	}
}
