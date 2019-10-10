import React from "react";
import { Provider } from "react-redux";
import { HashRouter } from "react-router-dom";
import App from "./App";
import "./styles/profile.css";
import "./styles/welcome.css";
import "./styles/setup.css";
import "./styles/css-reset.css";

const Root = ({ store }) => (
	<Provider store={store} className="root">
		<HashRouter>
			<App />
		</HashRouter>
	</Provider>
);

export default Root;
