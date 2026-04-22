# Braces and Globbing
## Commands
### `touch {arg1, arg2, ...}`
With the knowledge from our few previous lessons, we can now easily remake files if we deleted them. This isn't a real ressurection, such files won't have their contens anymore, but we can at least make new ones with the same names.

```bash
touch {foo,bar,baz}.{jpg,txt}

ls -l
bar.jpg
bar.txt
baz.jpg
baz.txt
foo.jpg
foo.txt
```

As we can see, we just made 6 new files with alternating file extensions with one simple command.

> [!CAUTION]
> Reminder that, even though you can verify if such files **exist** with `echo` and `printf` commands, you can still fool yourself by generating outputs from your command, rather than showing the reality of your current file system. Which is where `Glob` makes this more reliable. The moment you have a `*` in the command, you no longer can generate anything fake, it'll actually be there, or be modified.

#### Braces vs Globbing
For instance if we try such command in our current directory which **does not have** any .mov files:


```bash
printf '<%s>\n' files/*.mov
<>
```

It returns a null glob `<>`. But if we looked for files that actually existed, they would show up in the output:

```bash
printf '<%s>\n' files/*.{jpg,txt}
bar.jpg
bar.txt
baz.jpg
baz.txt
foo.jpg
foo.txt
```

In contrast, if we did this without a glob, we can get fake data, just strings being shown on the CLI, not actual files:

```bash
printf '<%s>\n' files/{foo,var,baz].{txt,jpg,mov}
bar.jpg
bar.txt
bar.mov
baz.jpg
baz.txt
baz.mov
foo.jpg
foo.txt
foo.mov
```

Here we just made 3 .mov files that don't actually existed, but do show up in the output.

TLDR: GLOBS **will look** at files, curly braces **will not**. 
