# Date formatting
## Commands
### `date`
By default, the bash shell can use the `date` command to bring up the current date:

```bash
date
Wed May  6 02:51:26 PM -03 2026
```

#### Using arguments with `date`
We can make our own date format, and feed it to `date` as an argument as such:

```bash
datefmt='%Y/%m/%d %H:%M:%S'
date +"$datefmt"
2026/05/06 14:54:52
```

We could also declare it and use it like this:

```bash
printf 'the date is %(%Y/%m/%d %H:%M:%S)T\n'
the date is 2026/05/06 14:54:52
```

> [!TIP]
> It is advisable to **always** use dates in such format `%Y/%m/%d` for cli tools, since you can have people, servers, other software relying on it. Having an agnostic way to display the date, make the data consistent and the location of use not matter as much.

#### Epoch time
We can get a date's epoch time with the following command:

```bash
date +%s
1778090506

# alternatively:
printf '%(%s)T\n'
```

You are also able to know for how many seconds the current shell has been running:

```bash
echo $SECONDS
9

# it says 9 since I opened a bash shell just for this example
# typically I use fish shell

# we can also get epoch time that way
echo $EPOCHSECONDS
1778090506
```
