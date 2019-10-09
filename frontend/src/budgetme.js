import React, { Component } from "react";
import Dropdown from "./header/dropdown";
import Viewport from "./components/viewport/viewport";

export default class BudgetMe extends Component {
	render() {
		return (
			<div>
				<Dropdown />
				<Viewport exact path="/" />
			</div>
		);
	}
}
