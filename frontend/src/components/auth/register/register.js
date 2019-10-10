import React, { Component } from "react";
import { Route, NavLink } from "react-router-dom";

export default class Register extends Component {
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
		this.props.history.push("/profile/settings");
	}

	update(field) {
		return e =>
			this.setState({
				[field]: e.currentTarget.value
			});
	}

	render() {
		return (
			<div className="welcome-box">
				<div className="welcome-header">
					<div className="splash-welcome">Welcome to</div>
					<div className="splash-budget">BudgetMe</div>
				</div>
				<form className="form-holder" onSubmit={this.handleSubmit}>
					<div className="form-fields">
						<input
							className="auth-field"
							type="email"
							value={this.state.email}
							placeholder="Username"
							onChange={this.update("email")}
						></input>
						<input
							className="auth-field"
							type="password"
							value={this.state.password}
							placeholder="Password"
							onChange={this.update("password")}
						></input>
					</div>
					<input
						type="submit"
						value="Register"
						className="welcome-buttons"
					></input>
				</form>
				<div className="oauth-splash" />
				<div className="registration-pitch">
					<span className="pitch-question">Already have an account? </span>
					<NavLink to="/login" className="pitch-answer">
						Login
					</NavLink>
				</div>
			</div>
		);
	}
}
