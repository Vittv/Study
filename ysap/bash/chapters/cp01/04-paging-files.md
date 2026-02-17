2026-02-06 - 14:19:03
tags: [#ysap]

# Paging Files
## Commands
### less
Sometimes a better use than cat, `less` is a command that prints the content on the terminal, but instead of being a simple print, it's more of a pager. Which means it's not actually printed, but previewed. This is better for inspecting contents because you are able to scroll up and down with your arrow keys or page up and page down. Because this preview takes control of the terminal, making your arrow up and down no longer show your previous or forwards commands. This is one of the ways to properly scroll through content displayed on a terminal, without using your mouse. Once you're done with the preview, it is simply gone, it wasn't actually printed into the terminal. You can quit the preview, just like on every other terminal application, with the command `q`.

You can also vim motions in `less`, so `j` and `k` will also work for up and down.

Pressing `/` turns the command line at the bottom into a search (just like vim) where you can search for patterns inside. `n` goes to next instance of pattern, `N` goes to previous reference.

#### more
You can actually use `more`, which also comes installed by default in some systems. They work the same exact way.

### less use cases
less can be very powerful due to its ability to preview and be used with other chained commands. You can `cat /usr/share/dict/words | grep dave | less` and it would give you that list with `dave` already searched for.
