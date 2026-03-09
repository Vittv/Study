# Curlies vs Parens
## Commands
### `()`
When writing functions, it is *usually* advised that we declare them with the `local` keyword. Otherwise they will be declared globally, thus being able to be changed globally by other elements. Which makes our code very unpredictable and unreliable.

There is another way to make things safer too, by utilizing `()` to wrap your function, instead of the typical `{}`. The reason for that is because `()` is actually wrapping your function in its own `subshell`, so it will no longer affect the global scope.

#### `subshell`
A `subshell` is simply a temporary shell that is used for the instance of an event. If you run code that is run in one, it will run each thing line by line, but when it gets to the `subshell` part, it will run it in its own `subshell`, basically isolating that action from the rest of the code and your entire shell.
