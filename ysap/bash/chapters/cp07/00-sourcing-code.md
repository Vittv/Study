# Sourcing code
## Commands
### `source`
If we make ourselves our own library under a `lib/` directory for example inside of our current root of our directory. We can execute other code, while requiring functions from a different file. We can `source` other code, from another file.

```bash
#!/usr/bin/env bash

source ./lib/greetings

greet dave
greet john
goodbye buddy
```

This would take the `greet` and `goodbye` functions of `./lib/greetings` and use the arguments `dave, john, buddy` we just gave it. So simply by running this script `./say-hi`, we'd get the proper result.

### `.`
The `.` command means the **same exact** thing *when used as the first character in a source statement*. So you can source things like `. ./lib/greetings` as well if preferred. `.` is also more portable for multiple shells, unlike `source`, so some devs prefer sourcing with `.` .

We can of course as usual do some scripting around this. Making conditionals to whether this `lib` we're sourcing even exists. Or we can add guardrails making it exit with an `exit 1` if it fails.

```bash
if ! ./lib/greetings; then
```

```bash
. ./lib/greetingz || exit 1
```

#### `-p`
We can use the `-p` flag for using predefined paths in `source`. An example will show it better:

```
libdirs=./lib
. -p "$libdirs" greetings || exit 1

```

### `if ! (return 2>/dev/null); then code fi`
You are able to test and add guardrails to the code your `sourcing` in the `sourcing` process itself.

```bash
if ! (return 2>/dev/null); then
  # we are being called directly
  greet dave
  goodbye john
fi
```

What is happening on the above code is:

1. We are making a `subshell` by wrapping our `if` argument in `()`.
  - The reason for that is so we can use the `return` statement. Otherwise `return` throws an error when outside of a `subshell`.

2. `2>/dev/null` is simply discarding the `exit code 2` (error code) if it ever does happen.

So, if the above code *can* be returned, it means it was sourced. If it *can't* then it wasn't. It is a clever way to check if your code can run before running it and getting errors.

In the example we have, we call the functions `greet()` and `goodbye()` directly, if we are unable to return. Directly as in, it is using the functions that already exist in that same file. So even if an error would be thrown, or something happened in the execution of such code, perhaps in a more complex codebase, it would still run it because we are directly calling them from within the script.
