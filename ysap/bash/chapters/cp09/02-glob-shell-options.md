# Glob Shell Options
## Commands
### `shopt | grep glob`
We can take a look at all the `glob` options we can use as such:

```bash
shopt | grep glob
dotglob                  off
extglob                  on
failglob                 off
globasciiranges          on
globskipdots             on
globstar                 off
nocaseglob               off
nullglob                 off
```

### `nullglob`
This should return an empty string as output. We are deliberately wrapping the string in `<>` so we can have a clear indication of where it starts and ends.

If we attempt to run it though:

```bash
printf '<%s>\n' empty/*
<empty/*>
```

We get the literal string `<empty/*>` which isn't ideal. This happened because it failed to get anything inside of a supposed existing `empty/` folder inside of our current directory.

This behavior can be polished if we toggle `nullglob` on. 

```bash
shopt -s nullglob
```

Now if we do the previous command:

```bash
printf '<%s>\n' empty/*
<>
```

It only returns the `<>` as expected. The main difference is that `nullglob` won't turn the result into a string if it fails.

> [!Note]
> Be careful with `nullglob` though. It's better to use it only when needed for testing things, as its behavior is not what you'd expect of your typical shell usage. For example if you try to `ls empty/*` in a directory with an actual `empty/` folder. IF `nullglob` were on, you'd just get a regular `ls` command output, rather than an error saying that there is no such file or directory inside of `empty/`.

### `dotglob`
Does exactly what it sounds like. Allows `globbing` to be done to hidden files as well. If we had a `.hidden-file` inside of `empty/`, we'd only be able to list it if we had `dotglob` on

```bash
ls empty/*
empty/.hidden-file
```

### `globstar`
This allows you to *recursively* `glob` through files in the shell.
