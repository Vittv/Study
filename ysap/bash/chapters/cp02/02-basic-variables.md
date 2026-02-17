2026-02-06 - 14:19:45
tags: [#ysap]

# Basic Variables
## Commands
### pwd
- pwd - shows your current path
- echo $PWD - same but referencing the variable

### whoami $USER
- whoami - shows current user
- echo $USER - same but referencing the variable

### $SHELL
- echo $SHELL - shows what bash you are running specifically

### $HOSTNAME
- echo $HOSTNAME - shows your hostname

### $MACHTYPE
- echo $MACHTYPE - shows your current OS

### Making new variables
You can make your variables from the terminal too. If we do `name=vitt` we can then `echo $name` and its output will be `vitt`. This will only last on the current bash session though. To make this permanent, you will need to add it as variable in your `~/.bashrc`. Make sure to always quote your expansions such as `"$name"` as it will make bash behave more properly. As an example of why this matters, if we declare variable `$somevariable=I am              a variable` if we `echo $somevariable` we would not output it with the proper spacing. If we had done `echo "$somevariable"` instead, we would get proper spacing.

#### unset
You can use `unset variablename` to unset the variable. Which is not the same as doing `variable= `, because in this case the variable still exists for that session, while unsetting it gets rid of it.

### uname
This prints your system's name. If run with `uname - a` you can get a lot of information such as:

- system name
- hostname
- kernel
- date
- time
- architecture

As you would expect, this can also be declared as a variable as such `thing=$(uname -a)` which then by doing `echo $thing` we would get the same exact output.

> [!NOTE] Note
> Try to default declaring variables as $() rather than using "``" to make your scripts more POSIX-compliant.
