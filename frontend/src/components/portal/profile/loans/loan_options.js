import React, { Component } from "react";

import MicroIcon from "../../../../styles/assets/Images/loan_icons/micro.png";
import PartnerIcon from "../../../../styles/assets/Images/loan_icons/partner.png";

export default class LoanOptions extends Component {
	constructor(props) {
		super(props);
		this.handleMicro = this.handleMicro.bind(this);
		this.handlePartner = this.handlePartner.bind(this);
	}

	handleMicro(e) {
		this.props.history.push("/profile/loans/micro");
	}
	handlePartner(e) {
		this.props.history.push("/profile/loans/partner");
	}

	render() {
		return (
			<ul>
				<li className="loan-network">
					<span className="micro-blurb">Micro Loans in your Circle</span>
					<div onClick={this.handleMicro} className="micro-icon">
						<img src={MicroIcon} />
					</div>
				</li>
				<li className="loan-partners">
					<span className="partner-blurb">Effortless Loans in Seconds</span>
					<div onClick={this.handlePartner} className="partner-icon">
						<img src={PartnerIcon} />
					</div>
				</li>
			</ul>
		);
	}
}
