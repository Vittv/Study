# Basic Globbing
## Commands
### `ls`
This will list the files inside of a directory. If not argument is given, it will list the ones in the current directory.

```bash
ls files/
bar.jpg bar.txt baz.jpg baz.txt foo.jpg foo.txt
```

#### `ls -l`
Lists the files as a list (each file on top of each other taking an entire line per output), instead of side by side.

```bash
ls -l files/
bar.jpg
bar.txt
baz.jpg
baz.txt
foo.jpg
foo.txt
```

### `echo files/*`
`*` here means everything inside `files/` will get sent as output while having `files/` still part of such output:

```bash
echo files/*

files/bar.jpg files/bar.txt files/baz.jpg files/baz.txt files/foo.jpg files/foo.txt
```

#### `ls -l files/*`
This does the same as the previous command, but outputs a list since it has the `-l` flag. Similarly to other commands, we can append `.jpg` or `.txt` to the end of `*`, and that will output only files in those specific file extensions.

```bash
ls -l files/*.txt
bar.txt
baz.txt
foo.txt

ls -l files/*.jpg
bar.jpg
baz.jpg
foo.jpg
```

Alternatively, you can also use `files/bar.*` which will output any bar named files regardless of their file extension.

```bash
ls -l files/bar.*
bar.txt
bar.jpg
```

#### `ls -l files/ba?.txt`
Here, the `?` in the end of the `ba` argument means that this output will have to be anything that starts with `ba`, but it *has* to have something after `ba`. In this case we get `bar` and `baz`

We can also use patterns for more in-depth searches just like in regex. Like so:

```bash
ls -l files/ba[abcrz].*
```

In this case, we are still long for `ba`, but also looking for abcrz after `ba`. Which will return `bar` and `baz`.

```bash
ls -l files/ba[abcrz].*
files/bar.jpg
files/bar.txt
files/baz.jpg
files/baz.txt
```
