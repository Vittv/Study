# Return vs Output
## Commands
### `return`
The `return` statement can be used to give a variable a value it expects, as such in the example below:

```bash
my func() {
  echo "YSAP"
  return 25
}

var=$(my-func)
code=$?

echo "output=$var, code=$code"
```

> [!IMPORTANT]
> `return` statements can only return `8bit` integers, so be careful when using it, as you might get unexpected results if not done carefully. What happens is for example if your `error code` gets higher the more it happens in your script, if such code gets to a number divisible by 256, it will return 0, instead of 256.

### File descriptors and `stdout/stderr`
If we run the script:

```bash
my func() {
  echo "this goes to stdout" >&1
  echo "this goes to stderr" >&2
  return 0
}

var=$(my-func 2>/dev/null)
code=$?

echo "output=$var, code=$code"
```

This would return `output=this goes to stdout, code 0`. Because we are throwing away the `stderr` by running `my-func 2>/dev/null`. `UNIX` systems have a file in the root `/dev/null` that works as a trash. Since this file will always keep itself empty, as we've learned before, by using `>` we write our output into another file. So by doing `2>/dev/null` we are essentially throwing the output into the void.

> [!Attention]
> This is **NOT** the same as your system's trash. The trash directory is located under `~/.local/share/Trash/` in most `UNIX`/`UNIX`-like systems.
