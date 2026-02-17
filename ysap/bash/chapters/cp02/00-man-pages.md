2026-02-06 - 14:19:18
tags: [#ysap]

# Man Pages
## Commands
### man
Uses `less` to page through a command's documentation, if found in the database. Apparently this does not come on every system, because I didn't have it in mine until I installed. Very useful command to learn this the proper way about commands and their use cases.

#### man sections
`man` has sections, or indexes as you may call it on its manpages `man man`. This is nice but it becomes more useful when you find out that you can reference these sections from the terminal. So if you wanted to check a really specific part of the man manual, you could by running for example `man 1 cp`. That would page you the first chapter of man's man pages. You can also use it to reference commands such as `man printf`, which will show you the man printf documentation.

### help
For some commands you'll try using man for, the man page will actually tell you to use the command's official documentation on `help` because it's a bash builtin command. For example the command `man history` will do that. Help is bash's official version of man. The main difference aside from obviously the content coming from different databases is that help actually prints the content, it is not a pager, so in some ways it is worse to use if you have to scroll through a lot of text. It also won't have the searching features and others that man will for using a proper pager for its preview.

#### builtin commands
Because of being builtin, some commands can't even be found on the terminal through your typical `which`. So if it ever may seem like a command just doesn't have a path or is installed anywhere, there's a very high chance it is just a builtin command.

### type
For those cases you can always run `type history` or whatever command you want to know about. It will then output something like: `history is a shell builtin`. It can also show you aliases. On a lot of systems you might get an alias as an output when running `type ls`, such as `ls is aliased to 'ls -p --color=auto`.

If you ever want to know if a command is a builtin or if it's a program you can also run `type -a`. `type -a ls` will output:
```
ls is aliased to 'ls -p --color=auto'
ls is /bin/ls
```

### compgen -b
This lists every single builtin command from your shell. Not exactly an every day use case but definitely useful to have around and knowing what it does.
