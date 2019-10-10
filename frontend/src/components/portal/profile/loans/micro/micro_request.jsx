import React, { Component } from "react";

export default class MicroRequest extends Component {
	constructor(props) {
		super(props);
		this.state = {
			debtorClass: true,
			lenderClass: false
		};
		this.swapToDebtor = this.swapToDebtor.bind(this);
		this.swapToLender = this.swapToLender.bind(this);
	}

	swapToDebtor() {
		if (this.state.lenderClass) {
			this.setState({
				debtorClass: true,
				lenderClass: false
			});
		}
	}

	swapToLender() {
		if (this.state.debtorClass) {
			this.setState({
				debtorClass: false,
				lenderClass: true
			});
		}
	}

	render() {
		let debtorClass = "micro-switch-active";
		let lenderClass = "micro-switch-inactive";
		if (this.state.lenderClass) {
			lenderClass = "micro-switch-active";
			debtorClass = "micro-switch-inactive";
		}
		return (
			<div className="micro-request-form-wrapper">
				<div className="role-switch">
					<span onClick={this.swapToDebtor} className={debtorClass}>
						Request Loan
					</span>
					<span onClick={this.swapToLender} className={lenderClass}>
						Fund A Loan
					</span>
				</div>
			</div>
		);
	}
}
