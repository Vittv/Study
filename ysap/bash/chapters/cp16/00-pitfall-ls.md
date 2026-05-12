# Pitfall: `ls`
First, let's look into what's actually in this directory:

```bash
ls files
a   b   c   d       e
```

Looks like we have `a`, `b`, `c`, and `d    e` inside this directory.

From here, we can showcase a common pitfall on the use of `ls` with two scripts:

## bad
```bash
for f in $(ls files); do
  echo "file is $f"
done

```

The `bad` script will output a file that doesn't exist, `e`:

```bash
./bad
file is a
file is b
file is c
file is d
file is e
```

This happens because the `whitespace` after `d` makes `e` get treated as another argument for the operation.

Because the `$()` sequence wasn't properly escaped.

## good
```bash
for f in ./files/*; do
  echo "file is $f"
done
```

In this case, the script properly shows all files listed:

```bash
./good
file is ./files/a
file is ./files/b
file is ./files/c
file is ./files/d     e
```
