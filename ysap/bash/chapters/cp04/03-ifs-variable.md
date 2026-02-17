2026-02-10 - 14:32:19
tags: [#ysap]

# IFS Variable
A builtin to bash variable. Responsible for telling bash what character to have when we do `space` or `tab` and others.
```bash
array=(
  foo
  bar
  baz
)

# The * here is stringifying this
# Making it echo as a single line
# Rather than as a code block
echo "array is: ${array[*]}"

IFS=hello
echo "array is: ${array[*]}"

array is: foohbarhbaz
```

The first character of IFS is what will be printed between different items we print. In the case of the script, we get `h` between each word, because our first IFS value was `h`, from `hello`
