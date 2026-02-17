2026-02-06 - 15:09:19
tags: [#ysap]

# User Input
## Commands
### read
The `read` command is how you read data from the shell, to be used somewhere else. By using the flag `-p` and writing it as such `read -p` you turn it into an actual prompt, where the user's answer will be the one to give you the desired data.

Even though you can use this for scripts. Your scripts can still bypass this prompting behavior by having data pipelined into them. So when it comes to our `hello` script prompting us for our name. If I simply run `echo vitt | ./hello` it would return `hello vitt`.

### yes
This command spams `y` on your shell. This is typically used to confirm any user prompts that require a `[y/n]` reply. A common way to use this for long installation scripts for example, is to have it `yes | ./installationscript` that way, it will answer yes to every single question in there. This can of course be a dangerous operation, but if you're the one making the script to make it easier for others, there would be no reason to fear such operation as long as you know what you script does. This is probably not the best way to do this, but it is the first way we've learned about so far.

### $1
When assigning a variable to this, it means the script will run using the first argument given by the user. For example, `./hello vitt` would return `hello vitt`, because `vitt` was the first argument given.

### $@
When using this in a loop, of course always quoted, it will put all user arguments into an array and return it into the script. That way you can have as many as needed and the script will run them all. For example: `./loop one two three` would return:

```
thing is one
thing is two
thing is three
```
