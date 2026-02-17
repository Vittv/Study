2026-02-06 - 16:04:34
tags: [#ysap]

# Conditionals
## Commands
### test
Every conditional flag in bash is actually an alias to `test -flag`. So when you have for example `-f` inside of an if statement's condition, you are actually running `test-f`.

To learn more about each conditional flag you can use, the `help test` can help, by showing every possible flag we can have. Some of the common ones are:

- -e FILE    true if file exists
- -a FILE    true if file exists
- -s FILE    true if file exists and is not empty
- -f FILE    true is file exists and is a regular file

- -b FILE    true if file is block special
- -c FILE    true if file is character special

- -d FILE    true if file is a directory

- -h FILE    true if file is a symbolic link

- -z STRING  true if string is empty
- -n STRING  true if string is not empty

### true and false
Both of these commands exist on the shell. `true` returns 0, `false` returns 1, when we run `echo $?` after each of them.

### running code on the terminal
Everything can be run from the terminal, you can throw in whole blocks like `[[ -f file.txt ]]` and it will run it. This alone won't do anything, but if you proceed to `echo $?` it should return 0 if that file does exist, and 1 if it does not.

### conditional best practices
It is generally recommended to use `[[]]` for conditions in bash. While if statements can be written without those at all or with only single brackets `[]`, they will behave better with double brackets. Consider not doing it if you're writing an actual POSIX script. But for the most part, `[[]]` will parse things better.
