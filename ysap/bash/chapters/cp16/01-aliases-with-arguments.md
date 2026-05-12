# Aliases with Arguments
Appending arguments with aliases on the shell can be pretty unpredictable. It is better to instead write mini programs for interactive use in such shell session. We can write one as follows:

```bash
greet() { echo "hello $1 nice to meet you"; }
greet dave
hello dave nice to meet you
```

Alternatively we can:

```bash
alias foo='echo $1 $2'
foo

# no output because $1 and $2 are not set
# we can then use set -- to remove any arguments, then introduce our own
set -- a b c

# run foo again and it will use your arguments
foo
a b

# and if we echo each argument
echo $1
echo $2
echo $3
a
b
c
```
