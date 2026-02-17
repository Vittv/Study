2026-02-06 - 14:21:40
tags: [#ysap]

# File Permissions
## Commands
### ls -l
`-l` stands for long-listing and it displays a lot of meta data. Showing permissions, user, date, time. When you use this and don't find an x at the end of the permissions, it means it currently does not have the `executable` permission.

### chmod +x
We can use this command to make scripts executable. The `+x` literally means to add that missing x at the end of the permissions tray. Doing so will not only make the script executable and give it an x at its permissions tray when you `ls -l`, but it will also make the script file **highlighted**, which makes it a little more obvious that it's an executable now.

#### script best practices
It might be better to not give your scripts a `.sh` file extension. This makes the script necessarily [POSIX-compliant](../../../../../resources/posix-compliance.md). Which is something limiting to some of bash's features. Because we already have a shebang `#!/usr/bin/env bash`, any system with such script, even if just called `script` with no file extension, will already know that it is a bash script. So at least for bash scripting, the file extension is completely unnecessary. If ever in doubt, once again, you can check if it's being recognized as a bash script by running `file script`.
