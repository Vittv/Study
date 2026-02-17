2026-02-06 - 14:18:23
tags: [#ysap]

# Basic File Manipulation
## Commands
### mv
There is no `rename` command in the CLI. Instead what we do is we `move` a file. Moving usually implies moving it from a location to another, such as, moving from one directory to another. But the same logic applies to names. If you move a file with a name to another file with another name, you will be renaming that file to the new name. `mv myfilename.txt ourfilename.txt` will change the file name into the latter. Always doing `old new`.

> [!NOTE]
> Typically, most CLI commands that are responsible for changing things as manipulating files, expects 2 arguments. Old first, new second. So always first tell it what file to change, and then what to change it to.

> [!CAUTION]
> If you're not careful, you can actually replace files with this command. So make sure when you're moving, you are actually naming it something that no other file is named as.

So just to be clear. Be mindful when using `mv`. It **WILL** overwrite your file if you're not careful. Unlike a file manager where it would usually tell you that you are about to overwrite a file or sometimes it will even rename it into, say, `filename(1).txt`, this will not be the case on any CLI. It will just overwrite it with no confirmation.

`mv` and `rm` are incredibly powerful, which is a better way to describe it rather than saying they're "dangerous". Everything about the CLI is supposed to be fast and intuitive. It expects you to know what you're doing because it's mostly not an environment made for users. It's a scripting environment, so **everything** is treated as code and immediate. It can be scary at first to use since there is a general lack of guardrails, but it's this same lack what makes you able to do really complex chains of commands that can save you a lot of time in the long run.

### rm
Picking `rm` back up to introduce some additional information. Let's say you had `lesson1.txt lesson2.txt lesson3.txt`. You can remove all of them with a simple `rm lesson*`.

> [!NOTE]
> "*", called "glob" typically means "all". Once again, it can be a very powerful tool, use it carefully. What the command rm lesson* does is it will match ANYTHING that comes AFTER lesson, thus deleting them.

#### Interactive Mode
To avoid scenarios where you would delete things on accident, you can use an *interactive* flag `-i`. `rm -i` will not remove things until you confirm it with a `yes/y/Y`. `remove lesson-1.txt?`

#### Command history
You can go back or forth a command you did before using up and down arrow keys. Up will go back a command, Down will go forward. This is very useful so if you're doing really repetitive tasks, you don't need to actually write out a lot of these commands over and over again.

#### alias
Briefly, an alias is when you name a command or a sequence of commands into a single name. In our case here, this is being brought up because if we wanted the rm command to be safer by default, we could easily achieve so by doing `alias rm='rm -i'`. Which is basically saying, when we run `rm`, make it actually run `rm -i`. To confirm that something is an alias, you can run `alias rm` for example. It will return `alias rm='rm -i`. If no alias is found, it returns `bash: alias: command: not found`

### clear
Also available as `ctrl+l`, this command simply clears the terminal. Useful for when things get too busy and you'd like to work on a clean slate.

### history
Prints the command history mentioned a few paragraphs back. Typically showing the number of commands used in total on that shell (as of this writing we currently have run 500 commands in our history, wow). This persists through logging in and out and `poweroff` and `reboot` as well.
