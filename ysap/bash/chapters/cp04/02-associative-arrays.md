2026-02-10 - 14:32:01
tags: [#ysap]

# Associative Arrays
These in bash are basically objects in JavaScript. They consist of arrays with more arrays and properties inside them. Anything with key -> value. To declare it we need to use `declare -A arr`.

> [!NOTE] Feature Detection
> If you'd like to use more modern features as such on very old systems, you might want to check if it works first. Instead of doing *version detection*, you should do *feature detection*, as it's a more practical way of seeing if it works. You can do so by simply following the command you'd like to test with an `echo $?` and that should return the proper stdcode.

```bash
if ! declare -A arr; then
  echo "uh oh, I couldn't make an associative array" >&2
  exit 1
fi
```

## Using associative arrays
```bash
declare -A arr

arr[foo]=1
arr[bar]=2
arr[baz]=3

echo "${arr[foo]}"
echo "${arr[bar]}"
echo "${arr[baz]}"
echo "${arr[baz]}"

# Indexing its values
echo "${arr[*]}"

# Indexing its keys
echo "${!arr[*]}"

for key in "${!array[@]}"; do
  value=${arr[$key]}
  echo "got $key=$value"
done
```
