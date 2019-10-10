import React, { Component } from "react";

export default class Info extends Component {
	constructor(props) {
		super(props);
		this.state = {
			name: "",
			age: "",
			income: ""
		};
	}

	update(field) {
		return e =>
			this.setState({
				[field]: e.currentTarget.value
			});
	}

	render() {
		return (
			<form className="basic-info" onSubmit={e => e.preventDefault()}>
				<div className="info-field-wrapper">
					<span className="info-field-prompt"> What is your Name ? </span>
					<input
						className="info-field-input"
						type="text"
						value={this.state.name}
						onChange={this.update("name")}
					></input>
				</div>
				<div className="info-field-wrapper">
					<span className="info-field-prompt"> What is your Age ? </span>
					<input
						className="info-field-input"
						type="number"
						value={this.state.age}
						onChange={this.update("age")}
					></input>
				</div>
				<div className="info-field-wrapper">
					<span className="info-field-prompt">
						{" "}
						What is your Monthly Income ?{" "}
					</span>
					<input
						className="info-field-input"
						type="number"
						value={this.state.income}
						onChange={this.update("income")}
					></input>
				</div>
			</form>
		);
	}
}
