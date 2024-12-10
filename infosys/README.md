### Some Basic Questions and Answers asked in Infosys Interview

##### Q What will be the output of the following programs?

```s = "put"
s[0] = "c"
print(s)
```
_In Python, string are **immutable**, which means you cannot modify an individual character of a string directly
when you trying to assign a new value to s[0], Python raise a *TypeError*._

`TypeError: 'str' object does not support item assignment`
