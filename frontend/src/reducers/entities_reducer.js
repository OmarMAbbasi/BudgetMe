import { combineReducers } from "redux";

import usersReducer from "./users_reducer";
import datasetsReducer from "./datasets_reducer";

const entitiesReducer = combineReducers({
	users: usersReducer,
	datasets: datasetsReducer
});

export default entitiesReducer;