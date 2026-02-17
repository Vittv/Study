2026-02-10 - 15:51:47
tags: [#ysap]

# Process Substitution
The syntax for this is similar as before, but changing the `$` for a `<`. Declared as such: `<(...)`.
```bash
words=$(grep d /usr/share/dict/words)

# grep -c d will also return the count

i=0
for word in "$words"; do
  echo "$word"
  ((i++))
done

echo "found $i words"
```

Alternatively we can also do this:
```bash
words=$(grep d /usr/share/dict/words)

i=0

while read -r word; do
  echo "$word"
  ((i++))

done <<< "$words"
```

## herestring
When using `<<<` you declare a herestring, which will pipe that data into the loop. The two above examples are not great, we are having to assign that entire variable into memory, making us iterate through 60150 lines of text. While this isn't a problem for such a small number, it could become very slow as this number grows to be infinitely bigger. A better way to write this script would be as such:
```bash
i=0

grep d /usr/share/dict/words | write read -r word; do
  echo "$word"
  ((i++))
done

echo "found $i words"
```

This script would work, partially, it would list all the words, but it would not return the correct number, instead returning zero. If we read the data from a process instead, we can get the actual value returned.
```bash
i=0

while read -r word; do
  echo "$word"
  ((i++))
done < <(grep d /usr/share/dict/words)

echo "found $i words"
```

So this is all *process substitution* is. It allows you to put a process in a file and pipe its output into the script. The same way, if you used it plainly in your shell, some commands won't work with it because it is being treated as a command. For example, if we `echo <(uname)` instead of getting our OS name, we will get the location of the process `/dev/fd/63`. Requiring us to instead `cat <(uname)` just as we would on any process. In sum, `<(grep d /usr/share/dict/words)` gets turn into a file in our script, and returns its output, even though it's originally a process.

### Error code
Because we are not declaring the `grep` statement into memory anymore, it will not return its error code anymore to us. So this behavior can be tricky if you're trying to debug the code, be mindful of that when using process substitution.
