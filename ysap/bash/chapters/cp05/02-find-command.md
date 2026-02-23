# `find` command
## Commands
### `find .`
This will look for all files in such directory recursively, by default. Which means it will also show you files inside of such directories and so on.

### `find . -type f`
`find` works with your usual `bash` flags, in this case, it would return only regular files.


### `find . -type d`
The usual, but only looking for directories specifically.

> [!Important]
> Make sure to always wrap name arguments with quotes `""`. Otherwise you're telling `bash` to read them, not `find`. 

### `-exec`
This can be appended into a `find` command to execute something related to the files found by `find`.

#### Example
If we run
```bash
find /usr/share -type f -name "*.txt" -exec echo hi i found a file {} yay ";"
```

It would return something like
```bash
hi i found a file /usr/share/vim91/doc/filetype.txt yay
hi i found a file /usr/share/vim91/doc/farsi.txt yay
hi i found a file /usr/share/vim91/doc/editing.txt yay
hi i found a file /usr/share/vim91/doc/digraph.txt yay
hi i found a file /usr/share/vim91/doc/diff.txt yay
hi i found a file /usr/share/vim91/doc/debugger.txt yay
hi i found a file /usr/share/vim91/doc/debug.txt yay
hi i found a file /usr/share/vim91/doc/channel.txt yay
hi i found a file /usr/share/vim91/doc/builtin.txt yay
hi i found a file /usr/share/vim91/doc/autocmd.txt yay
```

That command is:

1. looking into `/usr/share`
2. only for regular files `-type f`
3. only for files that end in `.txt`
4. `-exec`uting `echo hi i found a file {} yay ";"`
5. returning the output in `{}`
6. ending the operation `";"`

> [!Caution]
> Unlike most `bash` operations, `find` needs its flags and arguments to be in the right order, it can't just have its subsequent commands in whatever order you'd like. For more information on find you can always `man find` to check its manpage.
