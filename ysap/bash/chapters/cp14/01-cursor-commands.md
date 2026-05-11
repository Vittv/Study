# Cursor Commands
Here we can begin talking about how some of these TUI's are made. There are lots of libraries and frameworks made to build such TUI's, such as:


| Language | Library |
|---|---|
| Python | `Textual` |
| Python | `Rich` |
| Python | `curses` |
| Python | `Urwid` |
| Python | `Prompt Toolkit` |
| Rust | `Ratatui` |
| Rust | `Cursive` |
| Rust | `Crossterm` |
| Go | `Bubble Tea` |
| Go | `tview` |
| Go | `tcell` |
| Go | `gocui` |
| JavaScript / Node.js | `Blessed` |
| JavaScript / Node.js | `Ink` |
| JavaScript / Node.js | `cli-gui` |
| C / C++ | `ncurses` |
| C / C++ | `FTXUI` |
| C / C++ | `PDCurses` |
| Haskell | `Brick` |
| Haskell | `vty` |
| Java / Kotlin / JVM | `Lanterna` |
| Java / Kotlin / JVM | `JLine` |


## Commands
### `clear`
We can verify what well-known commands do under the hood:

```bash
clear | xxd
00000000: 1b5b 334a 1b5b 481b 5b32 4a .[3J. [H. [2J
``` 

Which means if you run the same output we got, you would also clear your terminal successfully.

### Script example: Jumping cursor
This code is self-explanatory:

```bash
#!/usr/bin/env bash

# save the cursor position
printf '\e7'

# jump somewhere
printf '\e[20;20H'

# print "hello world"
printf 'Hello World'

# restore cursor position
printf '\e8'
```
