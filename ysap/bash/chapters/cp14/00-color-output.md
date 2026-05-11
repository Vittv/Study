# Color Output
## ASCII
These color codes can be used in any language, so this isn't a bash specific thing. But, since it is very used in bash, it is worth learning, as such skill will also transfer into other languages.

The same way we can embolden something on a browser with `<b>This is bold</b>`, we can embolden things on the terminal using **ANSI Escape Sequences**. We can look into the [ASCII Table](https://ascii-code.com) for a full list of possible ASCII characters and Escape Sequences. There are 256 possibilities, because that's what a byte can fit.

For instance, we can print the character **a** in a new line, purely with hex code:

```bash
printf '%b' '\x61' '\x0a'
a

printf '%b' '\x61' '\x0a' | xxd
00000000: 610a
```

### Escaping
The escaping code we're looking for on the previously mentioned list is the `1b` ASCII, which is 033. Thus, also being able to be verified with the same command:

```bash
printf '%b' '\033' | xxd
00000000: 1b
```

Now, while you might find a lot of color code that starts with `\033`, we don't need to do that. `bash` has `\e` defined as its **escape character**, so anytime we need it, a simple `\e` can be used for any escaping purposes.

Here we can embolden something:

```bash
printf '\e[1mBold\n'
Bold
```

- `\e` -> Escapes what's to come
- `[1` -> Emboldens it
- `m`  -> Closes the escape
- `\n` -> Prints it on a new line

This will embolden everything going right indefinitely though. To properly close an embolden word, we need to do so with a reset of the initial escaping parameters. Since we made it bold, we need to make what comes after it *not* bold:

```bash
printf `\e[1mBold\e[0m\n`
```

- `\e` -> Escapes what's to come
- `[1` -> Emboldens it
- `[0` -> Resets the character
- `m`  -> Closes the escape
- `\n` -> Prints it on a new line

Finally:

### Coloring
#### Base 16 (ANSI colors)
Coloring the characters is the same concept, but using a color code instead. Not `rgb`, not `hex`, just the ASCII color code:

```bash
# Let's print some colors
# Foreground
printf `\e[30mBlack\e[0m\n`
printf `\e[31mRed\e[0m\n`
printf `\e[32mGreen\e[0m\n`
printf `\e[33mYellow\e[0m\n`
printf `\e[34mBlue\e[0m\n`
printf `\e[35mMagenta\e[0m\n`
printf `\e[36mCyan\e[0m\n`
printf `\e[37mWhite\e[0m\n`

Black
Red
Green
Yellow
Blue
Magenta
Cyan
White

# Background (change the 3 to 4)
printf `\e[40mBlack\e[0m\n`
printf `\e[41mRed\e[0m\n`
printf `\e[42mGreen\e[0m\n`
printf `\e[43mYellow\e[0m\n`
printf `\e[44mBlue\e[0m\n`
printf `\e[45mMagenta\e[0m\n`
printf `\e[46mCyan\e[0m\n`
printf `\e[47mWhite\e[0m\n`

# Bright Foreground (change the 4 to 9)
printf `\e[90mBlack\e[0m\n`
printf `\e[91mRed\e[0m\n`
printf `\e[92mGreen\e[0m\n`
printf `\e[93mYellow\e[0m\n`
printf `\e[94mBlue\e[0m\n`
printf `\e[95mMagenta\e[0m\n`
printf `\e[96mCyan\e[0m\n`
printf `\e[97mWhite\e[0m\n`

# Bright Background (change the 9 to 10)
printf `\e[100mBlack\e[0m\n`
printf `\e[101mRed\e[0m\n`
printf `\e[102mGreen\e[0m\n`
printf `\e[103mYellow\e[0m\n`
printf `\e[104mBlue\e[0m\n`
printf `\e[105mMagenta\e[0m\n`
printf `\e[106mCyan\e[0m\n`
printf `\e[107mWhite\e[0m\n`
```

> [!NOTE]
> Although we're using bash to declare it, what actually makes the colors show is your terminal emulator, not bash itself.

Now you might think: "How do I know which exact color values will these output on my terminal?". That will depend on your theme! Your terminal theme will simply define a hex value to be interpreted for each of these color codes. Which means Cyan in `Vague` theme, can look completely different in another theme like `Catppuccin` or `Gruvbox`, while the logic behind how each value is interpreted is part of your terminal emulator's source code.

### Switching color modes
#### 256 colors (8-bit)
We can also make use of different color modes. All it takes is declaring the mode, in this case it is **5** after the color code, then the color itself after the mode:

```bash
printf '\e[38;5;0mColor 0\n\e[0m'
```

- 38 -> no longer a color code, but a **select graphic rendition** (SGR) parameter that means "what follows is an extended foreground color specification."
- 5  -> the color mode (in this case, 8 bit - 256 colors)
- 0  -> the actual color, in this case, the first on the index would be Black

> [!TIP]
> As usual, all of this can be used in scripting with variables, arrays, loops etc.

#### True color (24-bit) Full RGB
For declaring a True color code, we put its color code **2** as well as its r, g, and b values:

```bash
# blueprint
\e[sgr;colormode;r;g;bm\e[0m\n
```

```bash
printf '\e[38;2;255;255;255m\e[0m\n'
```

> [!NOTE]
> Most, but **not all** terminal emulators will support this.

> [!TIP]
> We can consult this cheat sheet whenever we need to look at anything ANSI Escape Sequences related [ANSI gist](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)

### `tput`
`tput` is an easier way to handle such operations, though it is not a very portable tool, since it tends to have very different syntax across various operating systems. For instance, we can easily make something bold like this:

```bash
tput bold; echo hi;
hi
```

> [!TIP]
> You can learn more about `tput` with `man tput` or `help tput`.

### Conclusion
This is a deep rabbit hole, and coloring output and emboldening it doesn't even begin to scratch it. There is so much you can do with ANSI Escape Sequences, you can move the cursor, make lines, tables, entire [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface)'s are built out of this concept.
