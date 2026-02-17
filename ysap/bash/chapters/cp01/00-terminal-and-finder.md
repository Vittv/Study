2026-02-06 - 14:18:03
tags: [#ysap]

# Terminal and Finder
Bash can be use anywhere, you don't need to necessarily be on Linux to make use of it. Even though for example macOS uses zsh as their shell, all scripting will always still be done in bash.

The terminal works as a REPL, which stands for read eval print loop. The terminal is just a program, running your shell. Bash is the shell. So it waits for me to give it an input. `echo hi` will print "hi" to the terminal.

## Commands
### echo
Echo prints anything you input it with into your terminal. `echo something` will print `something`.

### pwd
Bash doesn't exist in a vacuum, it is always in a directory. To find where you are in the terminal, we can use the command `pwd` which stands for `print working directory`. In this current computer, when we open our terminal we will automatically be at our home's root. So when we run `pwd` we'll be at `/home/vitt/`. It is important to understand that a lot of basic file management that can be done on the terminal through bash can also be done from a graphical user interface. So if you opened a file manager (finder, explorer, nautilus, dolphin) and you made a folder or a new file in your home directory, you would also immediately see the change in your terminal. The system is still one, all that changes is how you display its information on the screen.

### ls
`lists` every file we can see inside such directory. It can be used both from current directory `ls`, or be used to see the contents of another directory you're not currently in. `ls Documents`, or to be more thorough: `ls ~/Documents/`

### rm
`remove` is a dangerous command, since it doesn't send your file into the trash like a typical "delete" or "remove" feature usually would. This deletes your file permanently with no confirmation. Use it carefully.

### cd
Stands for `change directory`. Can be used both with and without an argument. Every command expects and argument. Argument is what comes after the command, such as ls Documents. It needs to know where/what you want to see/modify. You can also use cd with no argument and this will always make you land at your home root again. When in doubt or lost in the terminal just `cd` alone and you will be back `home`.

> [!NOTE] Note
> Folder and Directory can be used interchangeably, they are the same exact thing. Typically directory is more used in the terminal/CLI (Command Line Interface) world, while Folders are more common in the GUI (Graphical User Interface) world such as file managers.

### touch
Makes a new file. It will make as many files as you tell it to, so it can be chained like `touch file1.tx file2.html file3.css`. It expects a file format at the end of the name, so it knows what type of file to make.

### mkdir
Can't finish this before at least mentioning mkdir. Same as touch, but it instead makes a directory `mkdir - make directory`. Perhaps one of the most obvious looking commands. 
