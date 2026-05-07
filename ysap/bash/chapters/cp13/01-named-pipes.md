# Named Pipes
A **named pipe** (also called a FIFO - First In, First Out) is a special file that lets processes communicate by writing and reading from a shared pipe. Unlike anonymous pipes (`|`), named pipes persist and can be used by unrelated processes.

You can create one with:

```bash
mkfifo mypipe
```

Then we can add hello into it:

```bash
echo hello > pipe
```

This is hard to showcase without 2 shell sessions, since once we run the previous command, the shell will just hang while the process is running. In which case, we'd need something like `tmux` for another shell session.

From there we can:

```bash
cat pipe
hello
```

Once this return happens, our original shell session stops hanging, and the process finishes successfully. This is why pipes can be so useful, they will block the shell until something else communicates with them.

## Scripting
We can make a script to showcase how this would work in a more practical fashion:

```bash
#!/usr/bin/env bash

while read -r line; do
  echo "[read line] $line"
done < pipe
```

If we run this on **session 1**:

```bash
# session 1
./basic-reader
|
```

It will hang and wait.

On session 2 we can:

```bash
# session 2
echo hello > pipe
```

Which will print `hello` on **session 1**.

```bash
# session 1
hello
```

Alternatively, we can also make the script read forever:

```bash
#!/usr/bin/env bash

while true; do
  while read -r line ; do
    echo "[read line] $line"
  done < pipe
done
```

Running this will hang in **session 1** and await for commands, while we can infinitely feed it commands from **session 2**:

```bash
# session 1
./forever-reader
|

# hanging awaiting commands
# printing commands from session 2 on session 1
[read line] hello
[read line] hello
[read line] hello
[read line] hello
[read line] hello
[read line] hello
[read line] hello
[read line] hello
[read line] Linux

# session 2
# inputting the commands
# we can also use commands instead of simple strings
echo hello > pipe
echo hello > pipe
echo hello > pipe
echo hello > pipe
echo hello > pipe
echo hello > pipe
echo hello > pipe
echo hello > pipe
uname > pipe
```

### Multiple clients writing to a shared pipe

```bash
#!/usr/bin/env bash

exec {fd}<>pipe

client() {
  local name=$1

  while true; do
    sleep 3
    echo "[client $name] hello" >&$fd
  done
}

client foo &
client bar &
client baz &

while read -r -u "$fd" line; do
  echo "[read line] $line"
done
```

#### What's going on
- **`exec {fd}<>pipe`** -> opens the file `pipe` for both reading and writing (`<>`), and assigns it a dynamic file descriptor number stored in `$fd`. This is the shared communication channel.

- **`client()`** -> a function that takes a name, loops forever, sleeps 3 seconds, then writes a hello message into the pipe using `>&$fd` (redirect `stdout` to the file descriptor).

- **`client foo &`, `client bar &`, `client baz &`** -> spawns three client instances as background processes, all writing into the same pipe concurrently.

- **`while read -r -u "$fd" line`** -> reads from the pipe one line at a time using `-u $fd` (read from that file descriptor). As each client writes a line, the main loop picks it up and prints it.

### Why this works
The pipe serialises the writes, even though three processes are writing concurrently, the reader sees them one line at a time. This is a simple fan-in pattern: many writers, one reader.
