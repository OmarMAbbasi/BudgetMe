import React from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";

import configureStore from "./store/store";
import Root from "./root";

document.addEventListener("DOMContentLoaded", () => {
	const root = document.getElementById("root");
	const store = configureStore();

	ReactDOM.render(<Root store={store} />, root);
});

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
