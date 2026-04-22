# Numeric Brace Expansion
## Commands
### `echo {n1..n2}`
This works exactly as you think it should, it will print all the numbers in between `n1` and `n2`:

```bash
echo {1,2}
1 2

echo {1..2}
1 2

echo {1..20}
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
```

#### inverted

```bash
echo {10..1}
10 9 8 7 6 5 4 3 2 1
```

#### skipping
In this case we'd be skipping 5 numbers per call

```bash
echo {1..100..5}
1 6 11 16 21 26 31 36 41 46 51 56 61 66 71 76 81 86 91 96
```

### `seq arg1 arg2`
We can also use `seq` as a sequence command, in this case, putting each number in a new line:

```bash
seq 1 10
1
2
3
4
5
6
7
8
9
10
```

It also assumes defaults, if you only give it one argument, such as 5, it will assume you wanted 1 to 5:

```bash
seq 5
1
2
3
4
5
```

### `echo` x `seq`
The main difference here is the order of arguments. To achieve going from 1 to 50, skipping 10 numbers, we would declare such command with opposite argument placement:

#### `echo`

```bash
echo {1..50..10}
1 11 21 31 41
```

#### `seq`

```bash
seq 1 10 50
1 11 21 31 41
```

### Using multiple arguments
We can write a script to showcase how this can be done with more than sequence number arguments and it will still work:

```bash
#!/usr/bin/env bash

for i in foo {1..10} bar {1..4} baz; do
  echo "$i"
done
```

Which would then output:

```bash
foo
1
2
3
4
5
6
7
8
9
10
bar
1
2
3
4
baz
```

This shows that while you *can* use `seq`, you don't necessarily need to. You can achieve the same results with some basic scripting.

> [!CAUTION]
> If you try to do this with a variable though, it will not work.

To exemplify this:

```bash
#!/usr/bin/env bash

max=4
for i in {1..$max}; do
  echo "$i"
done
```

This would **not** work. Instead, we can make a traditional for loop and get the desired output:

```bash
#!/usr/bin/env bash

max=4
for ((i = 0; i <= max; i++)); do
  echo "$i"
done
```

This would work just fine, and not depend on any external program or command aside from bash builtins.

- For skipping by 2 or any other number, we can easily do so by changing the incrementation argument: `i++` -> `i+=2`.
