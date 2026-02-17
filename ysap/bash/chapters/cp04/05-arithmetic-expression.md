2026-02-10 - 15:28:32
tags: [#ysap]

# Arithmetic Expression
We can declare arithmetic expressions in bash by simply wrapping them around another set of parenthesis as such `thing=$(( 2 + 2 ))`. Also, while inside this math mode, you don't need to refer to variables with a `$`, it will understand that you are using a variable already.

This is valid syntax:
```bash
a=2
b=3

echo $(( a + b ))

> 5
```

## Using words instead of numbers
If you try to do the same operation from above, instead with words, it will return a 0. Anything that bash can't parse as numbers will result in 0. Which can cause a lot of bugs. For example if taking numbers from a user input, you will need to check that what they're giving you is a valid number, before proceeding with the script.

## Common gotcha
When things return 0 in bash, they are considered a failure, even if that's the supposed outcome. For instance, if we run `10 % 2`, because this operation results in 0, bash will treat it as a failure, even though it has a correct output.

## Treating values like numbers
Consider the following script:
```bash
a=06
echo "$a"
echo $(( a ))
```

The former would return `06`, while the latter would return `6`. Because, once again, when we wrap things in double parenthesis with the `$`, we go into math mode. Thus, treating everything as math would in a proper way.

### Octal
But if we tried to make `a=08`, it wouldn't work and because it would consider the number to be too high. When bash gets number starting with 0, it considers them a `base8` number. Meaning for example that `8` would actually need to be declared as `010`. You can also force a base into the script:

```bash
a=010
echo "$a"
echo $(( 10#$a ))
```

The `#` is what forces the base to be base 10, thus returning 10 in this case, and because we are using that, we are also required to declare the variable more explicitly by having the `$` before it. If `a` were `08` instead on that example, it would return 8, as intended.
