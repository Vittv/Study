# Pipe status
## Commands
### A bit of nuance for `$?`
The `$?` command only shows the `exit code` output of the *last* element in the pipeline. For instance if we had `echo hi | grep bye`, then `echo $?`, this would return `1`. Because although `echo hi` was successful, `grep bye`, the final pipeline, was not.

In a similar note, if we do the opposite where the final pipeline is successful instead: `cat /this-doesnt-exist | tf , `, our `echo $?` would return an `exit code` of 0. Because `tf` doesn't need an actual file to exist, in order to be successful. We can think of this as "if `this-doesnt-exist` existed, `tf` would have worked just fine".

### `echo "${PIPESTATUS[*]}"`
With such command, we can finally check the `pipestatus` of every single pipe in our command. This will return from the `PIPESTATUS` array, which in the previous case would be an output of `1 0` since it was a `failure`, then `success`.

The easiest way to see this in action is by piping:
```bash
true | false | true | false
echo "${PIPESTATUS[*]}"
0 1 0 1
```

Which returns `0 1 0 1` since `true` and `false` are commands made to specifically return `success` or `failure`.

### subshells
We can run commands in a `subshell` by wrapping them with `()`. For instance, if we were to `exit`, it would simply kick us out of our terminal. But if we instead run `(exit)`, nothing would happen.
```bash
(exit)
(exit 4)
(exit 4) | (exit 7) | (exit 100) | (exit 0)
echo $?
0
echo "${PIPESTATUS[*]}"
0
```

As we can see, it returns `exit code` 0 both times. That's because in the first case, it is returning the final `(exit 0)` which is successful. Then, because we ran `echo $?` to find out the last pipe's output `exit code`. We get a 0 as well, since `PIPESTATUS` only returns the last command's pipestatus. So if we were to use this in scripting, we'd have to be very deliberate about having such `PIPESTATUS` show up right after the command we were trying to debug. Otherwise, its pipestatus output would be completely lost, overwritten by a more recent command given to the shell.
