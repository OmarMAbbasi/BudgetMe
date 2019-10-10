import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class Welcome extends Component {
	render() {
		return (
			<div>
				<div className="welcome-box">
					<div className="welcome-header">
						<div className="splash-welcome">Welcome to</div>
						<div className="splash-budget">BudgetMe</div>
					</div>
					<div
						style={{
							display: "flex",
							height: "20vh",
							flexDirection: "column",
							justifyContent: "space-around",
							alignItems: "center"
						}}
					>
						<NavLink className="welcome-buttons" to="/login">
							Login
						</NavLink>
						<NavLink className="welcome-buttons" to="/register">
							Register
						</NavLink>
					</div>
				</div>
			</div>
		);
	}
}
