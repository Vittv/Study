# Understanding `printf`
## Why use `printf`?
While a simple `echo` can get the job done sometimes, for any relatively complex print task, the `printf` command will give you more features to perform such task. `printf` has its differences and might seem harder to use than `echo` at times. By default, it won't break into a new line, and it also only works while wrapping the argument a single string with quotes.

## Commands
### `%s` - format specifier
We can use format specifiers with `printf` and directly format a string in its own call:

```bash
printf 'my string is (%s)\n' "$s"
my string is (hello world)
```

> [!NOTE]
> Each `%s` is a new argument you can put in the function's call

#### Padding arguments
##### `%xs` (right-justified)
We can give `%s` a number and that will print such argument with `x` amount of characters:

```bash
printf '%5s %5s\n' hello world
hello world # nothing changes because they're both 5 character words

printf '%10s %10s\n' hello world
     hello     world # each word now takes 10 characters
```

This can be extremely useful for building tables from scratch through the command line.

##### `%-xs` (left-justified)
The `-` here will make it **left** justified:

```bash
printf '%-10s %-10s\n' hello world
hello     world     # each word now takes 10 characters
```

##### `%*s`
The `*` can be used to use an argument after the call:

```bash
printf '<%-*s>\n' 10 hello
<     hello> # the word takes 10 characters because it used 10 as an argument

printf '<%*s>\n'  10 hello
<hello     > # it can as usual be left-justified 
```

For scripting this is really good, since we can get such arguments from the user.

> [!TIP]
> A lot of this functionality is brought from `C`. So while bash itself didn't invent a lot of these things, it was still a choice to make it support various `C` features, making the shell more useful and familiar.

##### `%05d\n`
We can use the `d` parameter to print numbers, just like in `C`. With such, we can make use of the feature to pad numbers with 0, which can be extremely useful:

```bash
printf '%05d\n' 55
00055
```

This can really help in scripting, because it doesn't allow us to use non-numbers, and will return an error, which can be caught with our script as well:

```bash
printf '%05d\n' hello
bash: printf: hello: invalid number
00000

# if we echo the most recent exit code
echo $?
1
```

> [!CAUTION]
> **`printf` numeric literal prefixes**
>
> When using `printf '%d\n'`, the format of the numeric argument changes how it is interpreted:
>
> | Prefix | Base | Example | Output |
> |--------|------|---------|--------|
> | `0` | Octal (base 8) | `0123` | `83` |
> | `0x` / `0X` | Hex (base 16) | `0xff` | `255` |
> | *(none)* | Decimal (base 10) | `10` | `10` |
>
> A leading `0` silently switches to octal — `010` prints `8`, not `10`.
> An invalid octal literal (e.g. `08`) produces `0` and an error.

### `%q`
Quotes the argument in a way that can be reused as shell input.

This makes your argument safe to print, instead of running in the shell with unforeseen consequences:

```bash
printf '%q\n' 'foo$bar' # a $ is generally dangerous to the shell if misused
foo\$bar                # with %q bash will safely escape the character when printing
```

### `$b`
Expands backslash escape sequences in the corresponding argument.

You can give it raw hex codes, and it will interpret them:

```bash
printf '%b' '\xff'
?

# we get a ? character because it's an unprintable character
# however, if we pipe it into a hex viewer

printf '%b' '\xff' | xxd
00000000: ff
```

> [!NOTE]
> This means `bash` can write binary.

- Another example

```bash
printf 'hello world%b' '\x0a' | xxd
00000000: 6865 6c6c 6f20 776f 726c 640a

printf 'hello world%b' '\x0a'
hello world
```

As you can probably guess, `\x0a` is the same as `\n`.

### `-v`
The `-v` tag can be used to store a string in to a variable:

```bash
printf -v var 'hello %s' dave
echo $var
hello dave
```
