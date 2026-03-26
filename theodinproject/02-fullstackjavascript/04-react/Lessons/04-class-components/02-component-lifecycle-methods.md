# Component Lifecycle Methods
## `render()`
The render function is the most used lifecycle method. It is the only required lifecycle method in a class component. It runs on mount and update of a component. Render should be pure, meaning it doesn’t modify component state, returns the same thing each time it’s called (given the same inputs), and doesn’t directly interact with the browser.

## `componentDidMount()`
This method is run after the component is mounted (inserted in the DOM tree). You should make any calls to fetch data that is needed for the component here. It is also a good place to perform any operations that depend on the component being mounted in the DOM.

## `componentDidUpdate()`
This method is run after a component re-renders. Because of this, you have to be careful about what you update in this method, as if you’re updating state indiscriminately, a re-render is caused, and you’ll end up in an endless loop. You can avoid this issue by using conditional statements about the equality of previous and current props when updating state.

In this method you should be updating anything that needs to be changed in response to either the DOM changing, or any states that you might want to act on upon change. For example, you’d want to refetch user data if the user changes.

## `componentWillUnmount()`
This is the last lifecycle method, which is called before a component is unmounted and destroyed. In this method you should be performing cleanup actions, so that would be cancelling network requests, clearing timers, etc.

## How `useEffect()` combines the lifecycle methods
It’s useful to understand that the `useEffect` hook used in functional components is essentially a combination of `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`. Which method/methods it relates to varies based on its dependency array, and if it returns anything.

- An empty dependency array would be equivalent to componentDidMount.

- A dependency array with a value/values in it would be a combination of componentDidMount and componentDidUpdate, but only updating when dependencies change.

- No dependency array would be equivalent to componentDidMount and componentDidUpdate combined.

- A return function inside of a useEffect() hook would be equivalent to componentWillUnmount.

For instance:

```jsx
useEffect(() => {
  placeHolderFunction();
  return () => cleanupFunction();
}, [])
```

In this snippet, the `useEffect` contains the functionality of `componentDidMount`, and `componentWillUnmount` via the `return` function. This example doesn’t have the `componentDidUpdate` functionality because of an empty dependency array.

## Resources
[component lifecycle diagram](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)
[component documentation](https://react.dev/reference/react/Component)
