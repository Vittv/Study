# Parameter Expansion
## Commands
### `${}`
There are quite a few things we can do inside of `{}`.

If we define a variable `s="dave eddy"`. We can grab information from it as such:

- Length
  ```bash
  echo "${#s}"
  9
  ```

- Capitalize first letter
  ```bash
  echo "${s^}"
  Dave eddy
  ```

- Capitalize the entire string
  ```bash
  echo "${s^^}"
  DAVE EDDY
  ```

- Capitalize a specific letter (in this case, `d`)
  ```bash
  echo "${s^^d}"
  Dave eDDy
  ```

If we try and run `echo "${s^^da}"` though, it won't work, we need to specialize a pattern.

Instead, we can make it work with:

```bash
echo "${s^^[da]}"
DAve eDDy
```

All of this can be applied to lowercasing as well, using `,` instead of `^`.

### Defining default parameter values in `bash`
We can make use of `${:-}` to add default values into parameters. The way it works is it will look for if there was a value defined at all, and if not, it will be replaced with whatever comes after `:-`.

```bash
#!/usr/bin/env bash

# parameter-expansion

name=${1:-Steve}

echo "hello $name!"

echo "done"
```

If we run `./parameter-expansion` without an argument, we get

```bash
hello Steve!
done
```

This is good for installation scripts for example, since we can use the current user's name as a way to approach them by using the `$USER` variable.

```bash
name=${1:-$USER}
```

```bash
hello vitt!
done
```

### `{?}`
We can also make use of `?`. The `?` here means required. So if we declared it as simple as `name=${1?}`. It would not run our script until we gave it an argument.

You may as well add strings after the ?. By default, the `?` alone would return `parameter not set` and refuse to run the script. But if we write `{?"You must supply a name"}`, it would instead print that rather than the `parameter not set` message.

### Substitutions with `/x/y`
We can easily substitute characters with `//`.

```bash
path="/home/dave/foo.txt"
echo "$path"

/home/dave/foo.txt

echo "${path/a/o}"
/home/dove/foo.txt
```

`/a/o` - `a` is picked, `o` is what it is changed into, just like many other substitution commands.

> [!Important]
> This only works once, for the first substitution match it finds

#### Substitute all matches
In order to substitute all matches we can simply double our `//` at the beginning where we write the matched character.

```bash
echo "${path//o/a}"
/hame/dave/faa.txt

# otherwise this happens

echo "${path/o/a}"
/hame/dave/foo.txt
```

### `#`
The `#` can be used inside any command `{}` to start from the left and delete to the right.

### `%`
The `%` is the exact opposite, it will go from right deleting to the left.

> [!Note]
> This is obviously not a real deletion, it's just a deletion from the string that is about to get printed into the shell. It is not file manipulation, unless you involve into actual file manipulation commands like `rm`, `cp`, `>`, `<`, `>>`, `<<` and so on.

### Substrings
We can make substrings as such:

```bash
s="dave eddy"
echo "${s:0}"
dave eddy

echo "${s:1}"
ave eddy
```

This feels like we're just making a new string, starting on the index given by the argument.

We can append this even further, defining a number of characters to be returned, with yet another `:` like so:

```bash
echo "${s:0:4}"
dave
```

In that case it only prints `dave` since it is starting from `0` and only priting the first `4` characters.

> [!Caution]
> You might think that using `echo "${s:-1}` would work as intended, which would start from the last character on the string. It won't, as we've learned before, `:-` means to give the command a default parameter. So if `s` was never defined, it'd get rid of our entire string and replace it with a `1`. To treat `-1` as an actual number in this scenario, we need to simply space it as such `echo"${s: -1}`. 

Applying this to scripting, we can iterate over all characters in a string.

```bash
#!/usr/bin/env bash

s="dave eddy"
len=${#s}

for ((i = 0; i < len; i++)); do
  c=${s:i:1}
  echo "$c"
done
```

Which would return:

```bash
d
a
v
e

e
d
d
y
```
