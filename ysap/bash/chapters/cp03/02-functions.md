2026-02-06 - 15:51:13
tags: [#ysap]

# Functions
Here is an example of how we can write a function
```bash
greet() {
  local name=$1
  echo "hello $name"

  # returning 0 means success
  return 0
}

for name in "$@"; do
  greet "$name"
done
```

bash is really powerful, with it we can use such functions to move files around, interact with the system with things like `mv`, `cp`, `>>`. When writing functions we start to really see how we can make our scripts really useful, while making use of the shell commands.
