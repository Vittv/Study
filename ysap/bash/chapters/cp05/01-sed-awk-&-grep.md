# `sed`, `awk`, & `grep`
## Commands
### `sed`
`sed` is a string editor that be very useful on the shell. To change a specific word of the output of a command, we can use it as such:
```
cat /etc/passwd | grep dave | cut -d : -f 1,7 | sed 's/dave/buddy'
```

1. What this is doing is, first we're `cat`ting the /etc/passwd file, which will just display its contents.

2. Then we're piping it to `grep` and grepping `dave`, returning us the first line in the file that contains `dave`.

3. Piping such output into a cut that will look for `-d` delimiter `:` on `-f` fields `1` and `7`.

4. Then piping that information into `sed` which will replace `dave` with `buddy` when we do `sed 's/dave/buddy`.

All of this would finally return `buddy:/bin/bash`

> [!CAUTION]
> `sed` might work differently on different versions of it, make sure to always check what version you have to know what is supported or not.

#### regex
`sed` also supports `regex` so if we were to instead run `sed 's/d..e/buddy` it would still find `dave`.

`regex` stands for Regular Expression. Unfortunately I already knew what this is. I say unfortunately because though it is extremely powerful, it can be very difficult to learn, or even to find enough reason to constantly practice it. More about `regex` can be found in [mdn regex documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions).

#### `-e`
You can use the expression flag to `sed` multiple things at once as such: `cat /etc/passwd | grep dave | cut -d : -f 1,7 | sed -e 's/d..e/buddy' -e 's/bash/fish/'` and it would return `buddy:/bin/fish`.

Again, none of this is real, we are not actually changing the user's shell to `fish`, we're simply altering the output.

### `awk`
`awk` is super powerful and has a huge rabbit hole of its own. It has its own language, so the moment we do `cat /etc/passwd | awk -F: '{ print $1 }'`, because we have the `''` after `awk` it indicates that we're giving it as an argument to `awk`. In that case it would print the first field of `/etc/passwd`.

To show a bit of its complexity, this can also be done with `awk`. Showcasing every user in the system and their respective shell permissions.

```bash
cat /etc/passwd/ | awk -F: '{ printf("%s has shell %s\n", $1, $7); }'

# would print:

root has shell /bin/bash
nobody has shell /bin/false
_dhcpcd has shell /sbin/nologin
_uuidd has shell /sbin/nologin
dave has shell /bin/bash
_nagios has shell /sbin/nologin
nagios has shell /bin/false
_mosquitto has shell /sbin/nologin
chrony has shell /sbin/nologin
```

#### conditionals
`awk` also accepts conditionals, for instance, if we ran the same cat command piping it to `awk -F: '$1 == "dave" { print $1, $7 }`, it would only print it if that first field indeed had `dave`.

Reminder that you can replace cat completely by a single `<` to read contents *from* a file. So if we wanted to easily get all the shells with a more simple command we could run `< /etc/passwd awk -F: '{ print $7 }'`.

Returning:
```bash
/bin/bash
/bin/false
/sbin/nologin
/sbin/nologin
/bin/bash
/sbin/nologin
/bin/false
/sbin/nologin
/sbin/nologin
```

#### `sort`
If we piped the previous command into a `sort`, it would return it sorted in alphabetical order.
```bash
/bin/bash
/bin/bash
/bin/false
/bin/false
/sbin/nologin
/sbin/nologin
/sbin/nologin
/sbin/nologin
/sbin/nologin
```

#### `uniq`
Which we can then pipe once **again** into `uniq`, getting only the unique matches of the operation.
```bash
/bin/bash
/bin/false
/sbin/nologin
```

##### `-c`
`uniq` can then use a flag `-c` to show the count of each unique match, how many time it would repeated without `uniq`.
```bash
2 /bin/bash
2 /bin/false
5 /sbin/nologin
```

### `wc`
Stands for word count and returns the amount of times a matched word returns from the command given. If we use it with a `-l` flag for lines, we get the same information as using `-c`.

If we ran `man ls | grep file | wc -l` it would return `70`, because the word "file" appears in 70 lines of the `ls` manpages. So for the `wc` command specifically:

- `-l` returns line count.
- `-w` returns word count.
- `-c` returns character count.

When running on its own, `wc` will return all three options. In the case of `man ls`, that would be `70 738 5153`.

> [!NOTE]
> `wc` does not work with unicode or emojis and what not. It merely counts bytes.
