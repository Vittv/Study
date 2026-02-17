2026-02-06 - 16:34:00
tags: [#ysap]

# For Loops
## Commands
### {a..f}
This iterates from item 1 to item 2. Because these are letters, they will be alphabetically sorted, therefore returning from our for-loop script:
```bash
thing is a
thing is b
thing is c
thing is d
thing is e
thing is f
```

The same can be said for numbers `{1..5}`:
```bash
thing is 1
thing is 2
thing is 3
thing is 4
thing is 5
```

### C style for loop
You can write for loops with mathematical expressions just like in C as long as you wrap it with `(())`. This puts us at math mode, making variables no longer need `$` prepended before their name.
