import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export default class Welcome extends Component {
	render() {
		return (
			<div>
				<div style={{ width: "100vw" }}>
					<div style={{ height: "33%" }}>Slideshow Here</div>
					<div
						style={{
							display: "flex",
							height: "66%",
							flexDirection: "column",
							justifyContent: "space-between",
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
