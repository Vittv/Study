# Special Strings
## Commands
There are three ways we can use strings:

### `no quotes`
This is fine if you don't plan on using expansion of variables.

```bash
echo hello
hello
```

### `''`
Single quotes should be used for when you **don't want** expansion of variables. Anything inside it becomes a true string:

```bash
echo 'hello'
hello

# attemping to expand variable
echo 'hello $USER'
hello $USER

# does not expand it
# instead shows the literal $USER string
# rather than your username
```

### `""`
Double quotes **do** expand variables:

```bash
echo "hello $USER"
hello vitt
```

### Examples
We can do some interesting things with this:

#### Different ways we can pad text
##### Tabbing

```bash
echo $'foo\tbar'
foo    bar
```

##### Line-breaking

```bash
echo $'foo\nbar'
foo
bar
```

###### Vertical tabbing

```bash
echo $'foo\vbar\vbaz'
foo
    bar
        baz
```

> [!TIP]
> All of these examples can be stored in variables. So if you stored for example `\n` in a variable called `newline` you could use it like `echo $'first{newline}second` and it would drop the second word on a new line.
