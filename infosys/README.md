### Some Basic Questions and Answers asked in Infosys Interview

##### Q. What will be the output of the following programs?
1. 
```s = "put"
s[0] = "c"
print(s)
```
_In Python, string are **immutable**, which means you cannot modify an individual character of a string directly
when you trying to assign a new value to s[0], Python raise a *TypeError*._

`TypeError: 'str' object does not support item assignment`

2. 
```s = "put"
print(s)
s = s + "cat"
print(s)
s.upper()
print(s)
```
*Explanation*
- The first **print(s)** prints the value of **s** which is **"put"**
- The second **print(s)** prints the concatenated string **"putcat"**
- The third **print(s)** prints **"putcat"** because the **upper()** method does not modify the original string **s**
instead, it return a new string with all characters in uppercase. However, since the result is not saved, the original string **s** remain unchanged.