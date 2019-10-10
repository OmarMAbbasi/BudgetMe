import React, { Component } from "react";
import NavButton from "../../../styles/assets/Images/nav_icons/NavigatorButton.png";

export default class NavMenu extends Component {
	constructor(props) {
		super(props);
		this.state = {
			popup: false
		};
		this.navFlip = this.navFlip.bind(this);
	}

	navFlip() {
		this.props.history.push("./loans");
		// console.log(this.state.popup);
		// console.log("flip");
		if (this.state.popup) {
			this.setState({ popup: false });
		} else {
			this.setState({ popup: true });
		}
	}

	render() {
		let navStatus = "nav-menu-hidden";
		if (this.state.popup) {
			navStatus = "nav-menu-show";
		}
		console.log(navStatus);
		return (
			<img
				style={{ zIndex: "2", height: "20vw", width: "20vw" }}
				onClick={this.navFlip}
				src={NavButton}
			></img>
		);
	}
}
