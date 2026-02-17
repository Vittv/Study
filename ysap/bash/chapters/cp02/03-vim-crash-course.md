2026-02-06 - 14:19:57
tags: [#ysap]

# vim Crash Course
## Modes
### NORMAL
The default, started by pressing `esc`, this is where we do most of our operations, such as deleting, editing, browsing, and copying (yanking)

- `y` yanks text (copy)
- `p` pastes text
- `yy` yanks a whole line
- `dd` deletes a whole line
- `x` deletes a character
- `u` undo the last command
- `.` repeats the last command given

> [!NOTE] Note
> When you delete text using visual mode selection + x or dd or any form of block of text deletion, such text is saved to your clipboard. This is a normal and expected behavior for vim, but it confuses new users quite a bit. Just have that in mind.

### VISUAL
Started by pressing `v`, Visual mode is probably one of the most important ones, from it, your cursor starts to highlight text, the same way a mouse would grab text if you held left-click on it. There is a lot that goes into it but for now we'll only be using this to copy and delete blocks of text.

### INSERT
Started by pressing `i`, this is the simplest mode, while in it, you can start typing and actually write text the document.

### COMMAND
Started by pressing `:`, this where we use all of our commands. Vim runs in a terminal, so it actually has direct access to your shell, so you can run anything you need from it. Thus, to do things like save and quit on the Vim application, you will have to use vim's commands in its own command line. All you need to know for now is that `:w` saves and `:q` quits. You can also combine these of course like so `wq`, writing and quitting at the same time. There are a lot more commands and possibilities that can be done through the command line on vim, but that would be a bit advanced for now, this is more than enough to start using vim as a daily driver text editor.
