2026-02-06 - 15:09:04
tags: [#ysap]

# Finally Scripting
## Commands
### cp
This command copies a file, it expects two arguments, `filebeingcopied newfilebeingmade`. It can be used any file, so single, or even whole directories with nested children. In the case of the video, we are using it to use a script as a template. By copying it and making a new one, we get to already have a [shebang](../../../../../resources/shebang.md) in such script.

### bash -n
A syntax checker. It will syntax check a file for you, without executing it. If it returns no error messages to the terminal, it means the script is properly written.

### echo $?
This will check for exit codes. `#?` is a variable of the exit code of the last command that was run.

  - success - exit code: 0
  - failure - exit code: != 0

So yeah, basically anything other than 0 is a failure exit code. Which means the script is not properly working as intended. For instance, if we wrote `end`, rather than `done` at the end of our for loop in our `loop` script, we would've gotten:

```
bash -n loop
loop: line 6: syntax error: unexpected end of file from 'for' command on line 3

echo $?
2
```

Giving us an error code: 2, meaning the script did not execute successfully.
