2026-02-08 - 17:02:08
tags: [#ysap]

# Case Statements
A case statement is often more elegant than an if statement. Especially in bash, it is easier to write and read. They can be written as easily as such:
```
s=$1

case "$s" in
  dave) echo hi dave;;
  buddy) echo ohhh there he is;;
  guy) echo uh oh here comes trouble;;
  *) echo Idk who you are;;
esac
```

Case statements always end on a `;;`, consider this the `break` of bash's `case` statements. If you write scripts with the `;;` though, have in mind that they will only match the first instance, and won't keep matching afterwards.

To match more possible matching patterns after the first one, we have to use a different syntax.

## Always fallthrough `;&`
If you want some that matches the first pattern and then any subsequent patterns, you'll want to use `;&`. In the following script, only `f`, `foo`, and `*` will match, because they come after `f*`, and the pattern we're looking for is `far`.
```
s="far"

case "$s" in
  d*) echo "matched d*";&
  dave) echo "matched dave";&
  f*) echo "matched f*";&
  foo) echo "matched foo";&
  *) echo "matched *";&
esac
```

## Try again `;;&`
Now, to really get the behavior of matching every possible pattern that matches the desired one, we need `;;*&`. Similar to the previous one in syntax, but very different in functionality. This will make sure to look through the code and only match desired patterns.

## Conclusion
Rarely does Dave use the other two syntaxes, but said it is good to know other variations of commonly used methods.
