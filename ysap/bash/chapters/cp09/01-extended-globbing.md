# Extended Globbing
## Commands
### `shopt`
This is a builtin command in bash which allows you to toggle more specific features of the bash shell. You can use `help shopt` for more information and available commands.

We need this in this case to toggle on the `extended globbing` feature by running `shopt extglob`. To toggle it more verbosely, we can use the `-s` and `-u` flags.

- `-s` for "set"
- `-u` for "unset"

```bash
shopt extglob
extglob       on

shopt -s extglob
shopt extglob
extglob       on

shopt -u extglob
shopt extglob
extglob       off
```

### `+H / -H`
If we ever get a problem on bash, like an error we have no idea about typically saying something about `event not found`. For the purposes for having clarity for testing, we can toggle it off with `shopt +H` and on with `shopt -H`. This has to do with *history expansion*, which is the part of the shell responsible for allowing the user to re-use, modify, and re-execute portions of previous command lines.

### Negating glob
We can make use of the `!()` syntax in order to negate an argument from a search. For instance:

```bash
ls -l files/!(*.txt)
```

Means we are looking for everything in files that *doesn't* end on `.txt`.

```bash
ls -l files/!(*.txt)
files/bar.jpg
files/baz.jpg
files/foo.jpg
```

### Matching multiple specific arguments
We can do so with `+(arg1|arg2)`, with the `+` meaning it has to match one or multiple times.

```bash
ls -l files/+(foo|bar).txt
files/bar.txt
files/foo.txt
```

#### `regex` similarities
These three are practically the same in regex comparatively:


|`bash`|`regex`|
|---|---|
|+(thing)|/(thing)+/|
|?(thing)|/(thing)?/|
|*(thing)|/(thing)*/|


- `+` => one or many times
- `?` => zero or one times
- `*` => zero or many times

### `ls -l files/@(foo).*`
Unlike the previous commands, the `@` makes the matching extremely strict. It will only match `foo` in this case, and only `foo`. So if we had a `foofoo.txt` file, it would still not show up as output, even though it has `foo` on its name. `foo.txt` on other hand would.
