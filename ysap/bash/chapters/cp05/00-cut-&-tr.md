# cut & tr
## Commands
### tr
We can use `tr` to replace a character by another one as such `cat simple.csv | tr , \'t'`. This specific example would make every `,` become a tab instead, which for a `.csv` file, it would format things a lot nicer, at least when you displayed them on the terminal.

### cut
`cut` can be used with some flags such as `-d` for delimiter and `-f` for field. If we run `cat simple.csv | cut -d , -f 1`, we could get the first field of such `.csv` file printed into the terminal. In the case of `simple.csv`, we'd get:
```
name
Alice
Bob
Charlie
Dana
```

While `cat simple.csv | cut -d -f 2` would return:
```
age
30
25
35
28
```

Finally `-f 3` at the end of the command would return:
```
city
New York
Chicago
Boston
San Francisco
```

#### `-f 1,2`
We can append more fields with a `,`.

#### `-f 1-3`
We can search for a field section 1 to 3 with a `-`.

Everything can be combined, since we're working on the shell, so the order doesn't really matter, and multiple things can work together.

> [!NOTE]
> The examples above are not a true `.csv` parsing, they're merely formatting text displayed into a terminal.
