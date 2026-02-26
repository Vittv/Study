# Timing commands
## Commands
### `time`
This returns how long it took to run a command in the shell.
```bash
time echo hi
hi

real 0m0.000s
user 0m0.000s
sys  0m0.000s
```

Which doesn't show much since it is a relatively simple operation. But if we instead time something like `ls`:
```bash
time ls
done/

real 0m0.005s
user 0m0.001s
sys  0m0.004s
```

#### `real`
This is the one we want to focus on the most. The real time it took to run a command in the shell.

#### `user`
This is how much `bash` is processing.

#### `sys`
How much `bash` is waiting for the kernel to process something like reading a file, system calls basically.

> [!Tip]
> When using `HTOP` for example. When we check our `CPU` usage, we can see `green` and `red` lines (or whatever color the terminal is currently themed in). The first color represents `userspace` `CPU usage`, while the second one represents `system` `CPU usage`.

### `time` in `userspace` vs `root`
Very simple, but basically, if we did `time sudo whoami`, we'd get `root` returned, with a proper time shown. If instead we do `sudo time whoami` we get 0ms time, because `time` is an external program, therefore, since we're running it from `root`, time can't get out of our shell and up into our root to check for it, so it will return the `/bin/time` output instead of the `time` builtin bash `keyword`.
