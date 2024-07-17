// Define ADD, addMessage(), messageReducer(), and store here:
const ADD = "ADD";
const addMessage = message => {
  return {
    type: ADD,
    message
  };
};

const messageReducer = (previousState = [], action) => {
  switch (action.type) {
    case ADD:
      return [...previousState, action.message];
      break;

    default:
      return previousState;
  }
};

const store = Redux.createStore(messageReducer);