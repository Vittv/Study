2026-02-10 - 15:10:10
tags: [#ysap]

# Command Substitution
Command substitution is a mechanism that allows you to execute a command and use its standard output in place of the command itself, either as arguments to another command or by assigning it to a variable

For instance:
```bash

current_date=$(date)
echo "Today's date is: $current_date"

echo "The current working directory is $(pwd)."

for file in $(ls); do
  echo "Processing file: $file"
done
```

Overall, all we're doing is assigning a variable to a pre-exisiting `bash` command. This is really similar to JavaScript's behavior. In the example that we do `echo "The current working directory is $(pwd)."`, if we hadn't had the `$()` we would have just printed the string `pwd` rather than evoking the command that displays our current path. The same way that in JS you would do it like so `The current working directory is ${pwd}`.
