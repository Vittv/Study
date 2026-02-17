2026-02-06 - 14:18:52
tags: [#ysap]

# Searching in Files
## Commands
### cat
Prints the contents of a file to the screen. `cat file.txt`. This can be useful for when you want to see what text is in a file, without having to open it yourself through a text editor.

### grep
Searches for the pattern you give it and returns any matching text from it. `grep pattern location/directory` If we do `grep dave /usr/share/dict/words`, instead of printing the entire words file, it will instead only print the words containing "dave" on them. So in some ways this is a better `cat` for a lot of situations.

`grep dave /usr/share/dict/words` would display:

```
cadaver
cadaveric
cadaverine
cadaverize
cadaverous
cadaverously
cadaverousness
daven
davenport
daver
daverdy
```

> [!NOTE] Note
> The above example is usually from a default file in macOS that other UNIX systems such as Linux might not have.

### ^
The caret typically means *match the beginning of the line*. So if we were to use grep with it from the example we had `grep '^dave' /usr/share/dict/words`, we would only output:

```
daven
davenport
daver
daverdy
```

Because we were giving our pattern `dave` a special character "^", we need to stop bash from interpreting special characters and treat the entire pattern as a string. Which is why we need to wrap the pattern in quotes as such `'^dave'`.

### $
The dollar sign means *match the end of the line*. Doing the same thing as `^` but matching the end instead. In which case `grep 'dave$' /usr/share/dict/words` would not return anything, since as we could see from the list above, none of those words end with `dave` specifically.

### >
When we earlier did `echo hello` we've learned that we can print hello to the screen with such command. But, by adding `>` to the end of it, and attaching a file, we can actually write our echo's message into a file as such: `echo hello > file.txt`. Now we will actually have "hello" inside of our `file.txt`. This is extremely useful and is one of the key features that make bash scripting so powerful.

> [!CAUTION] Caution
> This operation WILL overwrite content inside of a file.

### >>
This is a more sophisticated version of `>`. First, if we do `echo a >> file.txt`, if the file doesn't exist, it will automatically create it for us. If it does exist, instead of *overwriting*, it will instead *append* it to the end of the file. So our `echo hello > file.txt` file that currently has a "hello" inside of it, will now have:

```
hello
a
```

Now if you for example did `grep a file.txt` from that directory, you would get `a` as the output.

### grep flags
#### -A1
This will find the pattern given to grep *and* one line after it.

```
hello
a
b
c
d
```

`grep -A1 b file.txt` would return:

```
b
c
```

#### -B1
As you can probably guess, this is the same concept but for before the word, printing:

```
a
b
```

#### -C1
Finally we can use `-C1` which means context, we will get both options into one, displaying the text *before* and *after* our targeted pattern.

`grep -C1 b file.txt`

```
a
b
c
```

#### -i
`grep -i` can be used to make a case-insensitive search of the targeted pattern. If we had *DAVE* and *dave* in the same file, they would both return as output when running `grep -i dave file.txt`.

#### -o
`grep -o` will only print the parts that have matched the pattern.
If we run `'^d.' file.txt` we will get `da` because we only have the word dave that would match that, and the only part that matches it from the word is `da`. Same way if we combined this with the `-i` flag, `grep -o -i '^d.'` we would get `da DA` if we had both `dave` and `DAVE` in that file. The "." means any character.

These flags can be used in different orders and combined as well such as:

```
grep -oi
grep -io
grep -o -i
grep -i -o
```

### |
Referred to as "pipeline" this takes the output of a command and sends it into another one. So if we did `cat file.txt | grep dave`, it is as if we had done `grep dave file.txt`. This is a crucial part of automation on scripting as well.

These can also be chained as such, which may look confusing at first, but remember, all it is doing is sending its output to the field on the right.

`cat /usr/share/dict/words | grep -i dave | grep ly`

returns cadaverously

`cat /usr/share/dict/words | grep -i dave | grep i`

returns cadaveric cadaverine cadaverize
