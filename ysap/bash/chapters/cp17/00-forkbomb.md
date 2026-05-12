# Forkbomb
What if one day we found a `bomb.txt` in our files and we `cat` it:

```bash
cat bomb.txt
# DON'T RUN THIS

:(){ :|:& };:
```

Whoever wrote that would be write to warn you, do not run this.

That is a `forkbomb`. If you run this, it has a chance of locking up your machine. Let's understand what it does, by framing it into something more proper:

```bash
#!/usr/bin/env bash

# this is a function, so we should frame it as one
:() {
  : | : & 
}

:

# we remove the ; because it's a shell only necessity
# it separates the : from the rest so it can be read as a command AFTER the function

# now, let's frame this in a really obvious way
# : is null in bash, and it can be overwritten

my-func() {
  my-func | my-func &
}

my-func
```

So to put it simply:

1. We call `my-func()`
2. It calls itself
3. Then pipes itself into itself
4. Finally it runs in the background with the `&`
5. The final `my-func` is simply what calls the function to start in the first place

So in the original version, that final `:` is the trigger for it all.

## Why is this dangerous?
It's an infinite function. With the use of recursion, we are actively calling the same function over and over exponentially. On a system without proper guard-rails, this will consume all your CPU power and eventually shut the system down, or at least lock it up.

This diagram better shows what happens:

```

                     -> func -> ...
                    /
         -> func ->
        /           \
       /             -> func -> ...
func ->              -> func -> ...
       \            /
         -> func ->
                    \
                     -> func -> ...
```

## How to run it safely
We can run it safely with a few alterations to the code:

```bash
bomb() {
  local num=$1
  local name=$2

  # we can send the output to sdterr
  # this guarantees that the bombs are not
  # sending data to each other
  echo "$num $name is running" >&2

  # this will give the code a stopping point
  if ((num == 2)); then
    return 0
  fi

  ((num++))
  bomb "$num" left | bomb "$num" right &
}

bomb 0 init
```

The output is now safe and readable:

```bash
./step-bomb
0 init is running
1 left is running
1 right is running
2 left is running
2 right is running
2 left is running
2 right is running
```

If we bump the `if` statement with `if ((num == 5))` and then `sort` it, we can have a really neat output:

```bash
./step-bomb 2>&1 | sort
0 init is running
1 left is runing
1 right is running
2 left is runing
2 left is runing
2 right is running
2 right is running
3 left is runing
3 left is runing
3 left is runing
3 left is runing
3 right is running
3 right is running
3 right is running
3 right is running
4 left is runing
4 left is runing
4 left is runing
4 left is runing
4 left is runing
4 left is runing
4 left is runing
4 left is runing
4 right is running
4 right is running
4 right is running
4 right is running
4 right is running
4 right is running
4 right is running
4 right is running
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 left is runing
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
5 right is running
```

To get an even neater output we can use some of the tools we learned through the course:

```bash
./step-bomb 2>&1 | sort | awk '{ print $1 }' | uniq -C
 1 0
 2 1
 4 2
 8 3
16 4
32 5
```

This shows how exponentially this grows. The way it reads is that there are 32 processes running on layer 5. So if we don't put a stop on this, and remove the guard-rails, it will run infinite processes!

## DANGER ZONE
What would actually output if you run the original code:

```bash
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
-bash: fork: retry: Resource temporarily unavailable
```

## The End
This course can be found at [ysap.sh](https://course.ysap.sh)
