2026-02-06 - 14:19:30
tags: [#ysap]

# Programs and Commands
## Commands
### file
Shows you the file type of a file. For instance, if we run `file file.txt` it will output `file.txt: ASCII text`. But it can perform a lot more complex operations such as `file /bin/rm` where it will thoroughly show a command's or program's file type as well as other crucial details.

### $PATH
So we may wonder how these programs and commands open automatically as type their name, since their proper path is `/bin/command` a lot of the times. That's because we have a `$PATH` variable that lists all of these in there for us. A lot of this stuff comes preconfigured on your shell as well.

For example, if we `echo $PATH` in our `/home/vitt` directory, we get:
```
/home/vitt/.local/bin /usr/sbin /home/vitt/.local/bin /home/vitt/.local/share/nvim/mason/bin /home/vitt/.local/bin /
home/vitt/.local/bin /home/vitt/.local/bin /usr/local/sbin /usr/local/bin /usr/bin /sbin /bin /home/vitt/.local/bin 
/var/lib/flatpak/exports/bin /usr/lib/jvm/default/bin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl /ho
me/vitt/.local/bin /home/vitt/.local/bin /home/vitt/.local/bin /home/vitt/.local/bin
```

So anything that runs from our home will have to go through all of those paths and eventually find the correct one. If something specific you've recently installed is not on your path yet, you can easily add it with `export PATH="/path/to/your/folder:$PATH"`.

### tr
You can also use the `tr` (translate) command to make the `$PATH` output more readable, by giving each path a line break `echo $PATH | tr : '\n'`:
```
/home/vitt/.config/nvm/versions/node/v24.12.0/bin
/home/vitt/.local/bin
/home/vitt/.local/bin
/usr/sbin
/home/vitt/.local/bin
/home/vitt/.local/share/nvim/mason/bin
/home/vitt/.local/bin
/home/vitt/.local/bin
/home/vitt/.local/bin
/usr/local/sbin
/usr/local/bin
/usr/bin
/sbin
/bin
/home/vitt/.local/bin
/var/lib/flatpak/exports/bin
/usr/lib/jvm/default/bin
/usr/bin/site_perl
/usr/bin/vendor_perl
/usr/bin/core_perl
/home/vitt/.local/bin
/home/vitt/.local/bin
/home/vitt/.local/bin
/home/vitt/.local/bin
```

> [!CAUTION] Caution
> When scripting, always make sure to "$PATH" with quotes, or there is some weirdness that can happen.
