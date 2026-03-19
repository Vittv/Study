# Array Expansion
## Commands
### `printf`
This will be talked about more later, but the `printf` command makes printing a lot more convenient on the shell.
```bash
arr=(foo bar baz)
printf "%s\n" hello how are you
hello
how
are
you
```

```bash
printf "%s\n" "${arr[@]}"
foo
bar
baz
```

As usual, we can chain commands to do as we prefer. Everything from the previous note would work here.

```bash
# replacing every a with o
printf "%s\n" "${arr[@]//a/o}"
foo
bor
boz
```

```bash
# starting from the first character, getting only the first 2 words
printf "%s\n" "${arr[@]:0:2}"
foo
bar
```

Very simple note since everything from `parameter-expansion` applies here.
