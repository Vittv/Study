# Bash arguments
## Commands
### `./` or `bash`
Both of these will behave the same way. The main difference is that with `bash` we can give it arguments to behave differently.

#### `-x`
Running `bash -x` will run the script in debug mode. It prints exactly what it is doing, line by line. For instance if we had the script:
```bash
#!/usr/bin/env bash

first_name='john'
last_name='eddy'

full_name="$first_name $last_name"

if [[ $first_name === 'dave' ]]; then
  echo "oh hey it's dave"
fi

echo "Hello $full_name!"
```

`bash -x 00-simple-script` would return:
```bash
+ first_name=john
+ last_name=eddy
+ [[ john == dave ]]
+ echo 'Hello john eddy!'
Hello john eddy!
```

If we simply change the `first_name` variable to `dave` we get this instead:
```bash
+ first_name=dave
+ last_name=eddy
+ [[ dave == dave ]]
+ echo 'oh hey it'\''s dave'
oh hey it's dave
+ echo 'Hello dave eddy!'
Hello dave eddy!
```

#### `set -x`
We can also declare it inside of the script, instead of having to use it interactively through the shell. Once we have `set -x` inside the script, it will always run it already in such debug mode, as long as it's there.

##### `set -x set -+`
Additionally, you can wrap a section with it, instead of making the whole script run like it, which makes debugging even better.
```bash
set -x

first_name='dave'
last_name='eddy'

set -+

# rest of the script
```

This would return the script's output, with only the wrapped section in debug mode.

#### `PS4` editing
Not PlayStation 4! `PS4` is simply the little `+` sign you see at the beginning of each debug output line. If we write `PS4='hello: ' bash -x 00-simple-script`, we would then get the same output as before, but with a `hello: ` prepended to each line:
```bash
hello: first_name=dave
hello: last_name=eddy
hello: [[ dave == dave ]]
hello: echo 'oh hey it'\''s dave'
oh hey it's dave
hello: echo 'Hello dave eddy!'
Hello dave eddy!
```

### `bash -n`
This will simply detect syntax errors in your code as its output, also returning the error code, which is useful. Similar to `-c` on `node.js`, this is a very important command since it allows you to debug before ever running the code. Thus, testing it without consequences.

If there are no syntax errors, it will instead print nothing and return 0 as its `exit code` since there were no errors. Otherwise, it would typically print the line with the error and return `2` as `exit code`.

> [!Tip]
> Reminder that we can use `echo $?` to get our previous command's `exit code`. More on this at [finally-scripting](../cp03/00-finally-scripting.md)

### `bash -u`
Considering the following code:
```bash
#!/usr/bin/env bash

foo=1
bar=2

echo "foo is $foo"
echo "bar is $bar"
echo "baz is $baz"
```

If we run it, we get:
```bash
foo is 1
bar is 2
baz is
```

We can use `bash -u` to check for what is undefined inside the code, without running it, which will also return an `exit code`, this time, `1`, meaning the operation will fail.
```bash
vitt@cat $ bash -u 02-undefined
foo is 1
bar is 2
02-undefined: line 8: baz :unbound variable

vitt@cat $ echo $?
1

```

> [!Attention]
> While most things can be combined in the shell, you can't run `bash -nu` as it will not behave as you expect. Because we're checking for things on runtime, this will not return what you expect. `bash -nu` on the previous code would return an `exit code` of `0` instead.

### Variables
Bash's variable scope are in the same namespace as your OS'. Meaning, if you run a script while giving it an environment variable, such as `baz=2 ./02-undefined` it will then run that script with such new value as their `baz` variable. This is very important to know, as it can make some operations extremely dangerous if not done carefully.

### `shellcheck`
This is a program that can be used to check for shell errors. It does the same as the commands above but all in one. It will fully check and return every problem in the script, displaying the line with the issue, as well as documentation to look into to fix the error.
