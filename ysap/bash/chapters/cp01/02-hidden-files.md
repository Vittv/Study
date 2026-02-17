2026-02-06 - 14:18:36
tags: [#ysap]

# Hidden files
When we write a file with "." as its prefix, we make it a hidden file. So any file that looks like this `.file.txt` will be hidden.

## Commands
### ls -a
This will show every file when you `ls`, even hidden ones. Once you do this you might see `./` and `../` and get confused. Those are not files, they are built-in from your shell and are more of a directory indicator.

  - `./` means current directory

  - `../` means directory above (up one level)

### cd . cd .. cd -
So if you `cd .` you will be still on the same directory you were before. If you `cd ..` you will be sent a directory above. I say above because directories are nested. A parent directory will have its children inside of it, forming a sort of tree. Running `cd -` will send you back to the last directory you were in.

### Tab completion
When running all these commands and doing some quick file manipulation, You can press tab while writing a file name and your shell will try and autocomplete it for you. This can save a lot of time, so definitely useful to know and start using from now on. If such completion is ambiguous and has more than one option, bash will show all available options to you. This behavior can be avoided by writing the file name a little further to make it more specific.
