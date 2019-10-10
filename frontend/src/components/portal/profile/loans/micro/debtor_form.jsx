import React, { Component } from "react";

export default class DebtorForm extends Component {
	constructor(props) {
		super(props);
		this.state = {
			interest: "",
			amount: "",
			term: "",
			posted: false
		};
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	update(field) {
		return e =>
			this.setState({
				[field]: e.currentTarget.value
			});
	}

	handleSubmit(e) {
		e.preventDefault();
		this.setState({ posted: true });
	}

	render() {
		let buttonStyle = {
			width: "75vw",
			height: "8vh",
			display: "flex",
			justifyContent: "center",
			alignItems: "center",
			fontSize: "3vh",
			margin: "30px",
			color: "white",
			borderRadius: "3vw"
		};
		let buttonText;
		if (this.state.posted) {
			Object.assign(buttonStyle, { backgroundColor: "#35B085" });
			buttonText = "Successful";
		} else {
			Object.assign(buttonStyle, { backgroundColor: "#3B86FF" });
			buttonText = "Request A Loan";
		}
		return (
			<form onSubmit={this.handleSubmit} className="micro-request">
				<div className="micro-request-field-wrapper">
					<span>Loan Amount</span>
					<input
						className="micro-request-field"
						type="text"
						value={this.state.amount}
						onChange={this.update("amount")}
					></input>
				</div>
				<div className="micro-request-field-wrapper">
					<span>Interest Rate</span>
					<input
						className="micro-request-field"
						type="text"
						value={this.state.interest}
						onChange={this.update("interest")}
					></input>
				</div>
				<div className="micro-request-field-wrapper">
					<span>Term Length</span>
					<div className="term-length-wrapper">
						<input
							className="micro-request-field-mini"
							type="text"
							value={this.state.term}
							onChange={this.update("term")}
						></input>
						<span>Months</span>
					</div>
				</div>
				<button style={buttonStyle} onClick={this.handleSubmit}>
					{buttonText}
				</button>
			</form>
		);
	}
}
