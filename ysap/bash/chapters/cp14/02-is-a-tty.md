# Is a TTY
Commands like `ls` and `curl` detect if your output is a terminal. `isatty` is a builtin C library that checks if the `filedescriptor` is a terminal. This matters because things may change drastically if the output is a file or a terminal. There are different outputs and behaviors expected from each.

We can easily check it with bash like so:

```bash
[[ -t 1 ]]; echo $?
0
```

Let's make a script to make this check:

```bash
#!/usr/bin/env bash

if [[ -t 1 ]]; then
  echo stdout is a tty
else
  echo stdout is not a tty
```

From here we can use it and test it out:

```bash
./check-terminal
stdout is a tty

./check-terminal | cat
stdout is not a tty # because cat is a file, not a terminal

./check-terminal | less
stdout is not a tty # because less is a file, not a terminal
```

So if it doesn't directly output into a terminal, it is **not** a tty.

This is extremely useful for scripting since we can separate what happens to our code based on whether it is or not a tty!

> [!NOTE]
> If you ever write code like that, let the user override it. Give them the ability to force it one way or the other. Some commands like `ls` do that by default. This will make your tool more versatile and scriptable. So basically, don't make it always rely on the actual check, give it an option to make it think one or the other are matching. As a rule of thumb, both **allowing overrides** and **having sane defaults** makes for a great cli tool.
