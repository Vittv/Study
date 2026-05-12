# PS1 Variable
## Configuring the shell
### Aliases and `history`
We can define aliases to `bash` by adding them into our `~/.bashrc` file.

If we verify the existence of such file with:

```bash
echo ~/.bashrc
```

Declaring aliases is as simple as:

```bash
alias ls='eza -la --color=auto'
alias grep='grep --color=auto'
```

You declare it with:

- `alias` command
- `name` you want for it
- `'command'` what it actually does 

We can then use `!$` to make our next command use the previous argument used:

```bash
vim !$

# which will do
vim ~/.bashrc

# another example
echo hello how are you
echo !$
echo you
you

# we can also use !! to run the last command entirely
!!
echo you
you
```

All of this can be checked in `history`. You can also run a previous command by simply calling it based on its index in such `history`. Say the command is number `2396`, running `!2396` would run that command from the history.

> [!TIP]
> We can turn such history expansion commands **on** / **off** with `set -H` / `set +H`. Yes it looks inverted, but it's correct.

### `~/.bashrc`
#### `$PS1`
One of the first things we can do to our .bashrc is add this:

```bash
# If not running interactively, don't do anything
[[ -n $PS1 ]] || return
```

If `$PS1` variable is already set, then we stop running. Which would then mean that something has sourced this file and we're not running the shell interactively anymore.

#### `env`
Then we can set our environment variables. These will typically have preferences like your editor of choice, colors for specific tools, prefered pager, timezone, etc:

```bash
# this is a macOS example
export EDITOR='vim'
export PAGER='less'
export TZ='America/New_York'
export PATH=$PATH:/opt/homebrew/bin
```

On Linux, these maybe have a few more things, it gets a little more involved since those variables are needed to run other software variable, like for instance, your UI engines `QT` and `GTK`

```bash
export QT_QPA_PLATFORMTHEME=qt6ct
```

> [!NOTE]
> Often, if using a window manager, the user might declare such items in the window manager's config, rather than in their shell. For instance, this is what a typical `env.lua` file would look like in **hyprland**:
> ```lua
> -- cursor
> hl.env("XCURSOR_THEME", "mactahoe")
> hl.env("XCURSOR_SIZE",  "26")
>
> hl.config({
>   cursor = {
>     no_hardware_cursors = false,
>   },
> })
>
> -- Qt and GTK
> hl.env("GDK_BACKEND",        "wayland,x11,*")
> hl.env("XDG_DATA_DIRS",      "/var/lib/flatpak/exports/share:/home/vitt/.local/share/flatpak/exports/share:/usr/local/share:/usr/share")
> hl.env("QT_QPA_PLATFORM",    "wayland;xcb")
> hl.env("QT_QPA_PLATFORMTHEME", "qt6ct")
> hl.env("QT6CT_PLATFORM_THEME", "qt6ct")
>
> -- electron
> hl.env("ELECTRON_OZONE_PLATFORM_HINT", "auto")
>
> -- screenshots
> hl.env("XDG_SCREENSHOTS_DIR", os.getenv("HOME") .. "/Pictures/pictures/Screenshots")
> ```

#### make-prompt()
You can customize your terminal prompt manually with bash as such:

```bash
make-prompt() {
  local rst=$'\e[0m'
  local bold=$'\e[1m'
  local col1=$'\e[38;5;24m'
  local col2=$'\e[38;5;54m'
  local col3=$'\e[38;5;114m'
  local col4=$'\e[38;5;84m'

  # make prompt: "dave@ysap $ "

  # username
  PS1='\['$col1'\]dave\['$rst'\]'

  # @
  PS1+='\['$bold'\]\['$col2'\]@\['$rst'\]'

  # hostname
  PS1+='\['$col3'\]ysap '

  # prompt character
  PS1+='\['$col4'\]$\['$rst'\] '
}
make-prompt
```

> [!TIP]
> Although this is a very bash-only oriented way of doing things, most shell users will use something like [starship](https://starship.rs/) to customize their prompt.
