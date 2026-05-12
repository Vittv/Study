# Customizing Bash
## Dave's custom commands and `config`
### `cdspell`
Attempts to autocorrect misspelt `cd` arguments.

```bash
cd emtpy
empty

# actually puts us there
pwd
/Users/dave/foo/empty
```

### Aliases
```bash
# Aliases
alias ..='echo "cd .."; cd ..'
alias ag='rg' # sorry silver searcher
alias chomd='chmod'
alias externalip='curl -sS https://ysap.sh/ip'
alias gerp='grep'
alias hl='rg --passthru'
alias l='ls'
alias ll='ls -lha'
alias suod='sudo'

# Aliases (if applicable)
grep --color=auto < /dev/null &>/dev/null &&
  alias grep='grep --color=auto'

xdg-open --version &>/dev/null &&
  alias open='xdg-open'

# Enable color support of ls
if ls --color=auto /dev/null &>/dev/null; then
  alias ls='ls -p --color=auto'
else
  alias ls='ls -p -G'
fi
```

### `prompt-command()`
This is code that runs every time the prompt runs:

```bash
# Prompt command
_prompt_command() {
  local user=$USER
  local host=${HOSTNAME%%.*}
  local pwd=${PWD/#$HOME/\~}
  local ssh=
  [ -n $SSH_CLIENT ] && ssh='[ssh] '
  printf "\033]0;%s%s@%s:%s\007" "$ssh" "$user" "$host" "$pwd"
}
PROMPT_COMMAND=_prompt_command
```

> [!NOTE]
> The `printf` statement is how you set the `titlebar` in your terminal. I don't use title bars though.

More of these on his [dotfiles](https://github.com/bahamas10/dotfiles).
