# Pitfall: String Length
Let's say we're trying to write "Hello World" in yellow, store its value in variable, and read its length:

```bash
# echo yellow hello world
echo $'\e[33mHello World\e[0m'
Hello World

# declare it into a variable
s=$'\e[33mHello World\e[0m'
Hello World

# echo the variable
echo"$s" 
Hello World

# read its length
echo"${#s}"
20
```

It says 20, but Hello World is an 11 char long sentence. This happens because of all the escaping and color codes we have around the words. `bash` here is saying that this variable has 20 bytes, it is not concerned with its actual length. As we can test here:

```bash
echo -n "${s}" | wc -c
20
```

This gets trickier as we don't use only characters, but emojis:

```bash
s=🎉
echo "${s}"
🎉

echo -n "${s}" | wc -c
4
```

Once we get its word-count, it shows 4. Not because we have 4 characters, it's clearly a single emoji, but because that emoji takes 4 bytes.

So just be aware that this is yet *another* rabbit hole to learn about. `UTF`, `unicode` and what not. Getting string length in `bash` can be tricky, so it's best to do your research on how these characters and their respective properties work, before scripting anything too feature-rich.
