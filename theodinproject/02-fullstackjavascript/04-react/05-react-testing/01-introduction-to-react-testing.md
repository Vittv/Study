# Introduction To React Testing
For most of JS, we've used the [Jest](https://jestjs.io/) framework for testing. Since we're using [Vite](https://vitejs.dev/) for React, we can switch to [Vitest](https://vitest.dev/).

## UI testing
Since we were only testing the core logic rather than the UI before, our projects would get a little unstable on the frontend side of things. But as they grow more complex, testing the UI is more and more important, especially when working with a component-oriented library such as React.

## Setting up a React testing environment
We can follow along [Robin Wieruch's guide on setting up Vitest with RTL](https://www.robinwieruch.de/vitest-react-testing-library/) to get started.

> [!NOTE]
> Even if you set `globals: true` in `vite.config.js` like in the setup tutorial, ESLint will still yell at you, as it will not recognize these globals without some extra configuration in your `eslint.config.js` file. The most straightforward resolution would be to explicitly import the globals you’d need instead. You can omit `globals: true` from `vite.config.js` in this case.

Finally we'll need one more package before starting with testing:

```bash
npm install @testing-library/user-event --save-dev
```

From the packages we installed:

- `@testing-library/react` will give us access to useful functions like `render` which we’ll demonstrate later on.

- `@testing-library/jest-dom` includes some handy custom matchers (assertive functions) like `toBeInTheDocument` and more. (complete list on [jest-dom’s github](https://github.com/testing-library/jest-dom)). Jest already has a lot of matchers so this package is not compulsory to use.

- `@testing-library/user-event` provides the `userEvent` API that simulates user interactions with the webpage.

## Our first query
Let's try out first test:

```jsx
// App.jsx

const App = () => <h1>Our First Test</h1>;

export default App;
```

```jsx
// App.test.jsx

import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "./App";

describe("App component", () => {
  it("renders correct heading", () => {
    render(<App />);
    // using regex with the i flag allows simpler case-insensitive comparison
    expect(screen.getByRole("heading").textContent).toMatch(/our first test/i);
  });
});
```

We can then execute npm test `App.test.jsx` on the terminal and see the test pass. `getByRole` is just one of the many query methods we could've used. There are three types of queries: `getBy`, `queryBY` and `findBy`. We can read more about them in [the React Testing Library docs page about queries](https://testing-library.com/docs/queries/about/).

### Types of Queries Summary

| Type of Query | 0 Matches | 1 Match | >1 Matches | Retry |
|---|---|---|---|---|
| **Single Element** | | | | |
| `getBy...` | Throw error | Return element | Throw error | No |
| `queryBy...` | Return `null` | Return element | Throw error | No |
| `findBy...` | Throw error | Return element | Throw error | Yes |
| **Multiple Elements** | | | | |
| `getAllBy...` | Throw error | Return array | Return array | No |
| `queryAllBy...` | Return `[]` | Return array | Return array | No |
| `findAllBy...` | Throw error | Return array | Return array | Yes |


`ByRole` methods are favored methods for querying, especially when paired with the `name` option. For example, we could improve the specificity of the above query like so: `getByRole("heading", { name: "Our First Test" })`. Queries that are done through `ByRole` ensure that our UI is accessible to everyone no matter what mode they use to navigate the webpage (i.e. mouse or assistive technologies).

## Simulating user events
There are numerous ways a user can interact with a webpage. Even though live user feedback and interaction is irreplaceable, we can still build some confidence in our components through tests. Here’s a button which changes the heading of the App:

```jsx
// App.jsx

import { useState } from "react";

const App = () => {
  const [heading, setHeading] = useState("Magnificent Monkeys");

  const clickHandler = () => {
    setHeading("Radical Rhinos");
  };

  return (
    <>
      <button type="button" onClick={clickHandler}>
        Click Me
      </button>
      <h1>{heading}</h1>
    </>
  );
};

export default App;
```

Let’s test if the button works as intended. In this test suite, we’ll use a separate utility to query our UI elements. React Testing Library provides the `screen` object which has all the methods for querying. With `screen`, we don’t have to worry about keeping `render`’s destructuring up-to-date. Hence, it’s better to use `screen` to access queries rather than to destructure `render`.

```jsx
// App.test.jsx

import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import App from "./App";

describe("App component", () => {
  it("renders magnificent monkeys", () => {
    // since screen does not have the container property, we'll destructure render to obtain a container for this test
    const { container } = render(<App />);
    expect(container).toMatchSnapshot();
  });

  it("renders radical rhinos after button click", async () => {
    const user = userEvent.setup();

    render(<App />);
    const button = screen.getByRole("button", { name: "Click Me" });

    await user.click(button);

    expect(screen.getByRole("heading").textContent).toMatch(/radical rhinos/i);
  });
});
```

The tests speak for themselves. In the first test, we utilize snapshots to check whether all the nodes render as we expect them to. In the second test, we simulate a click event. Then we check if the heading changed. `toMatch` is one of the various assertions we could have made. Notice that the callback function for the second test is an `async` one, as we need this in order to `await user.click()`.

It’s also important to note that after every test, React Testing Library unmounts the rendered components. That’s why we render for each test. For a lot of tests for a component, a custom `setup` function could prove handy.

## What are snapshots?
Snapshot testing is just comparing our rendered component with an associated snapshot file. For example, the snapshot file which was automatically generated after we ran the *"renders magnificent monkeys"* test was:

```jsx
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports[`App component > renders magnificent monkeys 1`] = `
<div>
  <button
    type="button"
  >
    Click Me
  </button>
  <h1>
    Magnificent Monkeys
  </h1>
</div>
`;
```

It’s an HTML representation of the `App` component. And it will be compared against the `App` in future snapshot assertions. If the `App` changes even slightly, the test fails.

Snapshot tests are fast and easy to write. One assertion saves us from writing multiple lines of code. For example, with a `toMatchSnapshot`, we’re spared of asserting the existence of the button and the heading. They also don’t let unexpected changes creep into our code. Read all about what can be achieved with snapshots in the [Vitest snapshot docs](https://vitest.dev/guide/snapshot.html).

Snapshots might seem the best thing that has happened to us while testing thus far. But we are forced to wonder, what exactly are we testing? What’s being validated? If a snapshot passes, what does it convey about the correctness of the component?

Snapshot tests may cause false positives. Since we cannot ascertain the validity of the component from a snapshot test, a bug might go undetected. Over-reliance on snapshots can make developers more confident about their code than they should be.

The other issue with snapshots is false negatives. Even the most insignificant of changes compel the test to fail. Fixing punctuation? Snapshot will fail. Replacing an HTML tag to a more semantic one? Snapshot will fail. This might cause us to lose our confidence in the test suite altogether. Snapshots aren’t inherently bad; they do serve a purpose. But it’s beneficial to understand when to snapshot, and when not to snapshot.

### Resources
1. [Testing Implementation Details](https://kentcdodds.com/blog/testing-implementation-details)
2. [React Testing Library's cheatsheet](https://testing-library.com/docs/dom-testing-library/cheatsheet/)
3. [userEvent API docs](https://testing-library.com/docs/user-event/intro)
4. [Pros and Cons of Snapshot Tests](https://tsh.io/blog/pros-and-cons-of-jest-snapshot-tests/)
5. [Snapshot Testing: Benefits and Drawbacks](https://www.sitepen.com/blog/snapshot-testing-benefits-and-drawbacks)
