# Regular expressions
## Scripting
Considering we want to perform the following task:

- We have files presented as such
  - name - date
  - name - date

- We need to convert them to
  - date - name
  - date - name

With a bit of regex and pattern recognition, we can do the following:

```bash
#!/usr/bin/env bash

regex='^.*\/(.*) - ([0-9]{4}-[0-9]{2}-[0-9]{2})\..*$'
for f in ./images/*; do
  if ! [[ $f =~ $regex ]]; then
    echo "$f didn't match pattern"
    continue
  fi

  name=${BASH_REMATCH[1]}
  date=${BASH_REMATCH[2]}
  echo "$date: $name"
done
```

From this:

```bash
fun family party - 2022-10-31.jpg
not fun enemy party - 2022-11-27.jpg
```

We get this:

```bash
./script
2022-10-31: fun family party
2022-11-27: not fun enemy party
```

> [!NOTE]
> The conclusion here is that sometimes using builtins for a job can be better, especially for performance. The script using regex runs 3x faster than a script using more external tools. This might not matter for 2 simple files, but start handling hundreds, thousands of files, and this 3x difference is really noticeable.
