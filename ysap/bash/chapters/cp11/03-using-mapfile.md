# Using `mapfile`
## Example
Let's say we have some data:

```bash
cat data.txt
you what's up everyone
my name's dave
and you suck at programming
```

A basic way to read this in to an array would be:

```bash
#!/usr/bin/env bash
array=()

# read file into array
while read -r line; do
  array+=("$line")
done < data.txt

#print array
printf '<%s>\n "${array[@]}"'
```

## `mapfile` on scripts
Now, with `mapfile`, we can turn this into a much simpler script, but it wouldn't achieve the same result:

```bash
#!/usr/bin/env bash

mapfile array < data.txt

# print array
printf '<%s>\n "${array[@]}"'
```

That script wouldn't format it properly, because `mapfile` doesn't trim new lines by default. This can easily be fixed by including the `-t` flag on it:

```bash
#!/usr/bin/env bash

mapfile -t array < data.txt

# print array
printf '<%s>\n "${array[@]}"'
```

We can also give it a number of lines to read:

```bash
#!/usr/bin/env bash

mapfile -t -n 2 array < data.txt

# print array
printf '<%s>\n "${array[@]}"'
```

### `mapfile` callbacks
`mapfile` can accept callbacks:

```bash
#!/usr/bin/env bash

my_func() {
  local line=$1
  echo "(mapfile) called with line $line"
}

mapfile -t -C my_func -c 1 foo < data.txt

#print array
printf '<%s>\n "${foo[@]}"'
```

- `C` is the `callback` flag, but such flag expects a `quantum` value to define how many lines will be read between each call to `callback`

- `c` is the `quantum` flag we use to determine such number of lines

Would output:

```bash
./mapfile-callback
(mapfile) called with line: 0
(mapfile) called with line: 1
(mapfile) called with line: 2
<you what's up everyone>
<my name's dave>
<and you suck at programming>
```

> [!TIP]
> `mapfile` and `readarray` are the **same exact program**, so both can be called interchangeably on the shell. The same way `.` and `source` do the same exact thing, it's the **same program**, just different ways to call it.
