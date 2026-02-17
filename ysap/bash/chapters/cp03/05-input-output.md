2026-02-06 - 16:53:17
tags: [#ysap]

# Input/Output
## Commands
### read
When using the read command, we can make a script that allows us to send back to the user what they've typed. The script at first won't do anything, but will be waiting for your inputs, then send them back to you. This is similar to a prompt, but without any text.

```bash
# read has some weird behavior when using backslashes \
# because of that, it's better to use read -r
read -r zettelkasten
echo "you said $zettelkasten"

# which basically reads the string raw
# read only reads the first line
```

### <
Opposite from `>`, this command will instead bring the data *from* a file, rather than insert it *into* it. The big difference in using this command specifically, is that `bash` will be the one reading the data, rather than `cat` or `bat`.

`./read-input < /usr/share/dict/words`

## File Descriptors
Every time you read input from a file, such file has 3 file descriptors:

### stdin
This is file descriptor 0. Its code is 0, and it's important to know. This is the standard input, whatever you're writing at the moment and sending to the program.

### stdout
This is file descriptor 1. Code 1 is standard output, which is whatever the program sends back to the user.

### stderr
This is file descriptor 2. Code 2 is standard error, which is whatever error comes up as the program runs and/or the input/output is sent.

This matters because in a script as such:
```bash
if (($# == 0)); then
  echo "name required" >&2
  exit 1
fi
```
As we can see here, this is making it so, if no input is given, the string "name required" is *given* `>` to file descriptor 2 `standerror`. This would be specially useful for more complex scripts where you get actual non hardcoded error messages. Those could then be sent back to the user, by sending them to file descriptor 2, and printing such file descriptor to the terminal.

Typically programs will always send whatever you were looking for to `stdout` while error messages will go to `stderr`.

#### How it works
Say we did `cat /this-file-does-not-exist > file.txt`.

It would then output: `cat: /this-file-does-not-exist: No such file or directory`. But unlike what you might be thinking, `file.txt` did not get the output of this error. Because this error went to stdout, not stderror.

Now, because this operation was not successful, thus, nil. The file `file.txt` actually gets its content overwritten by nothing. So, now we have an empty file. This is to show that writing the wrong bash operations can have very destructive consequences. The act of overwritting content inside files is often referred to as `clobbering`.

### Going back on the script itself
```
if (($# == 0)); then
  echo "name required" >&2
  exit 1
fi
```
This script has an `exit 1`, because 1 is a code for failure, remember we always either return 0 for `true` and 1 for `false`. We must use `exit`, rather than `return`, because `return` is only allowed inside of functions. So just consider `exit` as a non-function `return`. The number at the end is optional, but definitely makes a script more polished.

When trying to match patterns after a letter, such as `d*` or `b*`, make sure to not quote them, or they will not be considered wildcards. So as a general recap to this whole part, this script:
```bash
hello() {
  local s=$1
  echo "hello $s!"
}

goodbye() {
  local s=$1
  echo "goodbye $s!"
}

if (($# == 0)); then
  echo "name required!" >&2 
  exit 1
fi

for name in "$@"; do
  if [[ $name == d* ]]; then
    hello "$name"
  elif [[ $name == b* ]]; then
    hello "$name"
  else
    goodbye "$name"
  fi
done
```
Uses two functions `hello()` and `goodbye()` that both take an input and save as variable. Then it verifies if there was an input at all, and if there wasn't, it prints an error message as `stderr`. Finally if there was input at all, it will prepend them `hello` in case the input starts with `d` or `b`, or prepend `goodbye` if not.
