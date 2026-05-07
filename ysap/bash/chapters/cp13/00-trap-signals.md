# Trap Signals
Signals are provided by your operating system. The most common as `SIGTERM` and `SIGKILL`.

To get started with learning `trap`, we can use its help command:

```bash
help trap
```

In there we will find that `trap -l` will list all possible `SIG`'s we can trap.

```bash
trap -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

- `SIGINT` -> what is used when we press `ctrl-c`, it interrupts a process running on the shell. `ctrl+c` sends `SIGINT` to the entire **foreground process group**, not just a single process, so if you have a pipeline or parent+child processes running, they all receive it, not just the shell itself.

- `SIGWINCH` -> sent when your terminal is resized.

- `SIGKILL` -> sent to kill processes, typically what is used when you stop a process in `btop`, `htop`, or any sort of task manager.

## Trapping exit to ensure code execution
In this example we can see that because we are trapping bash's exit, the function written at the top **has** to execute before the code exits:

```bash
#!/usr/bin/env bash

cleanup() {
  echo cleanup function running
}

trap cleanup exit

echo script starting
echo ...
echo script done
```

This would output:

```bash
./script
script starting
...
script done
cleanup function running
```

This is interesting since as we can see, there was never a call at the end of the script to actually *run* such function. While the trap call was in the middle of the script, it still executed at the end of it, because it was the last thing to be done before exiting, since `exit` was trapped.

Even if we wrote a `exit 1` at the end of such script, it'd still be retained by the trap call, the output would be the exact same, but its `exit code` would be 1.

```bash
echo $?
1
```

Now if such `exit code` were written **inside** of the `cleanup()` function, its code would overwrite any other `exit code` written at the end of the script.

## $? vs stderr
- `$?` is machine-readable success/failure code which we call `exit code` (**0 -> success, 1 -> failure**).

- `stderr` is file descriptor 2, text output with a human-readable error message. People can sometimes be confused by the two, but they are completely different things.

This is why often we test something to run on the shell with for example: `command -v git > /dev/null 2>&1`. `> /dev/null` redirects `stdout` (fd 1) to `/dev/null`, discarting it. `2>&1` redirects `stderr` (fd 2) to wherever `stdout` is currently pointing, which is `/dev/null`. So both `stdout` and `stderr` get discarded. You don't care about the output at all, you only care about the `exit code`. If the command is found it exits 0, if not, 1.

Why not just `2> /dev/null`? Some programs print "command not found" to `stdout` instead of `stderr`, so redirecting both covers all cases.

The order also matters -> `2>&1 > /dev/null` does not do the same thing. That would redirect `stderr` to the original `stdout` (the terminal), then send `stdout` to `/dev/null`. You'd still see error messages. Always redirect `stdout` first, then point `stderr` at it.

In newer bash scripts you'll also see the shorthand:

```bash
command -v git &> /dev/null # redirects both stdout and stderr at once
```

Which is equivalent, but bash-specific.
