import React from "react";
import "./App.css";
import "./stylesheets/welcome.css";
import "./stylesheets/css-reset.css";

import BudgetMe from "./components/budgetme";

function App() {
	return (
		<div style={{ width: "100vw" }} className="App">
			<BudgetMe />
		</div>
	);
}

export default App;
