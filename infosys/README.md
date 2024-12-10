### Some Basic Questions and Answers asked in Infosys Interview

##### Q. What will be the output of the following programs?
1. 
```
s = "put"
s[0] = "c"
print(s)
```
_In Python, string are **immutable**, which means you cannot modify an individual character of a string directly
when you trying to assign a new value to s[0], Python raise a *TypeError*._

`TypeError: 'str' object does not support item assignment`

2. 
```
s = "put"
print(s)
s = s + "cat"
print(s)
s.upper()
print(s)
```
*Explanation:*
- The first **print(s)** prints the value of **s** which is **"put"**.
- The second **print(s)** prints the concatenated string **"putcat"**.
- The third **print(s)** prints **"putcat"** because the **upper()** method does not modify the original string **s**.
instead, it return a new string with all characters in uppercase. However, since the result is not saved, the original string **s** remain unchanged.

3. 
```
l = [1, 2, 3, 4, 5]
print(l[::-1])
```
_Output:_
`[5, 4, 3, 2, 1]`

**l[::-1]** uses **list slicing** to create new list, it gives a new list with the element of **l** in reverse order.

4. 
``` 
d = {"a":10, "b":20, "c": 10, "a": 100}
print(d)
```

In Python, _dictionary cannot have duplicate keys_, and the final dictionary is **{'a': 100, 'b': 20, 'c': 10}** because of the value of **"a"** was overwritten by **100**

5. 
``` 
p = [1, 2, 3, 4]
q = p
q[0] = 100
print(p)
```
_Output:_
`[100, 2, 3, 4]`

Both **p** and **q** refer to the same list, so modifying **q** also modify **p**. The first element of list is updated to **100**, and this changes reflected in both **p** and **q**.

6. 
```
d = {"a":10, "b":20, "c": 100}
print(d["x"])
```
_Output:_
`KeyError: 'x'`
This will result in a **KeyError**, because the dictionary does not contain a key **"x"**.