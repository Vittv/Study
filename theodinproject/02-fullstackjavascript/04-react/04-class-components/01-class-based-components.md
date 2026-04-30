# Class based components
## Historical React component patterns
Back in the day, React codebases were very class based. Since functional components were called state-less as there was no way to manage state in them. So if we ever deal with legacy React code, we will probably see a lot of classes.

## Building a class component
Usually we want to make more components instead of having a single component responsible for most of the app. But here we can make one long functional component just to visualize how they're made.

```jsx
import { useState } from "react";

const FunctionalInput = ({ name }) => {
  const [todos, setTodos] = useState(["Just some demo tasks", "As an example"]);
  const [inputVal, setInputVal] = useState("");

  const handleInputChange = (e) => {
    setInputVal(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setTodos((prevTodos) => [...prevTodos, inputVal]);
    setInputVal("");
  };

  return (
    <section>
      <h3>{name}</h3>
      <form onSubmit={handleSubmit}>
        <label htmlFor="task-entry">Enter a task: </label>
        <input
          type="text"
          id="task-entry"
          name="task-entry"
          value={inputVal}
          onChange={handleInputChange}
        />
        <button type="submit">Submit</button>
      </form>
      <h4>All the tasks!</h4>
      <ul>
        {todos.map((todo) => (
          <li key={todo}>{todo}</li>
        ))}
      </ul>
    </section>
  );
};

export default FunctionalInput;

```

### The start of a class-based component
Now we can make it into a class-based component. Which should start with a class, which will need certain properties to qualify as a React component. React provides us with all those properties on a class called `Component`.

```jsx
import { Component } from "react";

class ClassInput extends Components {
  // Some code goes here
}

export default ClassInput;
```

### The use of a constructor and props
Classes are usually incomplete without a constructor. Since the whole point of a class is to define a structure that can be used to make more methods.

The props passed into this component are passed to the class’s `constructor`. This, along with the `super` method, allows you to use the props in the context of this, which, in this case, refers to the component. We can check more about `super` in its [mdn page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super).

If a component doesn't have any props, it's okay to leave the constructor and super with no arguments.

```jsx
import { Component } from "react";

class ClassInput extends Component {
  constructor(props) {
    super(props);
  }
  // Some more code goes here
}

export default ClassInput;
```

### How you can render JSX
Now we have to find a way to render the JSX.

We can do so with a `render` method, also using the declared props in the constructor as well.

```jsx
import { Component } from "react";

class ClassInput extends Component {
  constructor(props) {
    super(props);
  }
  // Some more code goes here

  render() {
    return (
      <section>
        <h3>{this.props.name}</h3>
       {/* The input field to enter Todos */}
        <form>
          <label htmlFor="task-entry">Enter a task: </label>
          <input type="text" id="task-entry" name="task-entry" />
          <button type="submit">Submit</button>
        </form>
        <h4>All the tasks!</h4>
        {/* The list of all the Todos, displayed */}
        <ul></ul>
      </section>
    );
  }
}

export default ClassInput;
```

The main difference as we can see here is that hte props get provided by `this`, unlike the functional component we saw initially.

### How to use state and manage context
From the following code block we can see that the state gets initialized as a part of the constructor.

```jsx
import { Component } from "react";

class ClassInput extends Component {
  constructor(props) {
    super(props);

    this.state = {
      todos: [],
      inputVal: "",
    };
  }
  // Some more code goes here

  render() {
    return (
      <section>
        <h3>{this.props.name}</h3>
        <form>
          <label htmlFor="task-entry">Enter a task: </label>
          <input type="text" id="task-entry" name="task-entry" />
          <button type="submit">Submit</button>
        </form>
        <h4>All the tasks!</h4>
        <ul></ul>
      </section>
    );
  }
}

export default ClassInput;
```

The pre-defined `setState` method can be used to set it again, since state must not be mutated, so a new state must be set, every time.

Finally we can finish it with functionality. Everything is similar except, whenever a method is declared, you must `bind` the `this` of the method to that of the class in order to work with it, as by default, the methods in a class are not bound to it. This is usually done inside the constructor and not at runtime (in the render method). Though if you use arrow function syntax, `this` is automatically bound to the class instance, and you can skip binding it in the constructor.

```jsx
import { Component } from "react";

class ClassInput extends Component {
  constructor(props) {
    super(props);

    this.state = {
      todos: [],
      inputVal: "",
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleInputChange(e) {
    this.setState((state) => ({
      ...state,
      inputVal: e.target.value,
    }));
  }

  handleSubmit(e) {
    e.preventDefault();
    this.setState((state) => ({
      todos: state.todos.concat(state.inputVal),
      inputVal: "",
    }));
  }

  render() {
    return (
      <section>
        <h3>{this.props.name}</h3>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="task-entry">Enter a task: </label>
          <input
            type="text"
            id="task-entry"
            name="task-entry"
            value={this.state.inputVal}
            onChange={this.handleInputChange}
          />
          <button type="submit">Submit</button>
        </form>
        <h4>All the tasks!</h4>
        <ul>
          {this.state.todos.map((todo) => (
            <li key={todo}>{todo}</li>
          ))}
        </ul>
      </section>
    );
  }
}

export default ClassInput;
```
