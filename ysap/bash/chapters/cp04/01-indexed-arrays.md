2026-02-08 - 17:38:15
tags: [#ysap]

# Indexed Arrays
In bash, you can make an array with `array=(foo bar baz)`. If you expand it like a variable and try `echo $array`, you will only get the first element of the array, instead of the entire array.

## Indexing the array
To properly index an array you need to wrap it in `{}`, *then* you can actually index it as usual with `echo "${array[0]}`", in this case, getting the first element of the array. In case you array only has 3 items for example, and you try to index its forth item, it will instead return an empty string, instead of throwing an error. Just like in other languages, inverting the order also works and you can do so by writing the index negatively as such `[-1]`. Which in this case would return the last value in the array.

It is also possible to use variables as indexes. If you had a variable `idx=2` and did `echo "${array[idx]}"` it would return index 2 from that array, so the third value in it. Indexing it with a `$` is also valid syntax `{array[$idx]}`.

## Indexing every single item
For this we can use `[*]` or `[@]`.
```
for item in "${array[@]}"; do
  echo "item is: $item"
done
```

The issue with using `*` is that it will actually return everything as a single item. To get a proper iteration returning every item on its own we can use the `[@]` instead.

> [!CAUTION] Caution
> Always make sure to quote `""` your indexed arrays. While it *can* sometimes work without them, its behavior might not be as predictable depending on the array's structure. To keep things safe and always get what you expect, quote them `""`.

## Array syntax
Typically `array=()` will already be interpreted by bash as an indexed array. But if you'd like to explicitly declare it as one you can do it with `declare -a array=()`.

### Copying over an array
To properly copy an array, you have to literally make a new one. We do this by using the same exact syntax as before to properly index an array, but we wrap it in `()`, since we are making a new one. So all we're doing is writing that same array once again, inside of another one, as such: `second-array=("${first-array[@]}")`.

### Pushing to an array
We can use the following syntax to push values into an array: `second-array+=(buddy guy joe)`, and it would append those items to the end of such array.

### Pretty printing values inside an array
To do this we can use our `declare` command from before but with the `-p` flag. If we declare an array `array=(foo bar baz)`, and do `declare -p array`, we get `declare -a array=([0]="foo" [1]="bar" [2]="baz")`. This syntax is valid, so we can also just declare an array and explicitly say which index is what.

### Getting array's length
By adding a `#` we can get an array's length. `echo "${#array[@]}"`. Contrary to doing `echo "${#array[0]}"`, which will only tell you the length of the string in `index [0]`.
