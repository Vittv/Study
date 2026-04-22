# Brace Expansion
## Commands
### `{}`
If we try and do `echo {hello,world}`, `hello` and `world` are turned into two arguments, which makes the `echo` print:

```bash
echo {hello,world}
hello world
```

So it ignores the "," or rather, it recognizes each word as arguments *because* of the comma if anything.

We can make it literal by quoting them, in that case we'd print the literal curly braces:

```bash
echo "{hello,world,foo,bar,baz}"
{hello,world,foo,bar,baz}
```

#### script example

```bash
#!/usr/bin/env bash

filename='my-file'
echo "$filename".{txt,jpg,mov}
```

On the above script, because we left the file extensions out of the quote, we'd get the following output:

```bash
./curly-brace-expansion
my-file.txt my-file.jpg my-file.mov
```

> [!NOTE]
> Unlike `Glob`, `echo` doesn't care if these are actual files, it treats them all as strings.

#### array example
We can achieve a more readable output by using an array:

```bash
#!/usr/bin/env bash

filename='my-file'
arr=( "$filename."{txt,jpg,mov} )

for item in "${arr[@]}"; do
  echo "$item"
done
```

And get the following output:

```bash
./curly-brace-expansion
my-file.txt
my-file.jpg
my-file.mov
```
