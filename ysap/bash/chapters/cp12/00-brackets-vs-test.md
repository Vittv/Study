# Brackets vs. `test`
## Commands
### `test`
Test is both builtin to bash, and also is installed on your system.

```bash
type -a test
test is a shell builtin
test is /bin/test
```

### `[`
The same as `test`, only difference is it requires a closing bracket.

```bash
type -a '['
[ is a shell builtin
[ is /bin/[
```

We can verify this by running `file /bin/[`:

```bash
file /bin/[
/bin/[: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamical
ly linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=78feb2bb
52c210964d728a377553e85997f90cfb, for GNU/Linux 4.4.0, stripped
```

### `[[`
Although these are shell builtins and also programs installed on your system, `[[` in bash is a keyword. We can verify it by running:

```bash
type -a '[['
[[ is a shell keyword
```

> [!TIP]
> `[[` generally seems to be the safest option for most use cases. It is not a command, but a keyword, which gives it special parsing rules the shell handles before execution.

#### Why it wins
##### No word splitting or globbing on variables

```bash
file="my file.txt"
[ -f $file ]    # breaks! splits into: [ -f my file.txt ]
[[ -f $file ]]  # fine - no splitting inside [[
```

##### No quoting required (though still good practice)

```bash
[ "$a" = "$b" ]   # must quote to avoid errors if empty
[[ $a = $b ]]     # safe unquoted
```

##### Pattern matching with `=` and `!=`

```bash
[[ $name = J* ]]        # glob match - is $name a J name?
[[ $file != *.txt ]]    # does not end in .txt?
```

`[ ]` Treats these as literal strings, not patterns.

##### Regex matching with `=~`

```bash
[[ $email =~ ^[a-z]+@[a-z]+\.[a-z]+$ ]]
```

`[ ]` has no regex support at all.

##### `&&` and `||` work correctly inside `[[ ]]`

```bash
[[ $a -gt 0 && $b -gt 0 ]]   # fine
[ $a -gt 0 && $b -gt 0 ]     # syntax error - && is a shell operator, not a test operator
[ $a -gt 0 -a $b -gt 0 ]     # old style, deprecated
```

##### No accidental command execution with `<` and `>`

```bash
[ $a < $b ]    # tries to redirect stdin from file named $b
[[ $a < $b ]]  # lexicographic comparison, as intended
```

When to still use `[` or `test`: when writing POSIX `sh` scripts that need to run on systems without bash (BusyBox, `/bin/dash`, Alpine, etc). `[[` is bash/zsh/ksh only. If your **shebang** is `#!/bin/sh`, stick to `[`.

In short, `[[` does what you *meant* to write, while `[` does what you *literally* wrote, which often isn't the same thing.
