# Interview questions and Answers
# Q 1. What will be the output of below code
s = "put"
s[0] = "c"
print(s)
# O/P : TypeError: 'str' object does not support item assignment


# Q 2. What will be the output of the below program
s = "put"
print(s)
s = s + "cat"
print(s)
s.upper()
print(s)
# O/P : 
# put
# putcat
# putcat

# Q 3. What will be the output of the below program
l = [1, 2, 3, 4, 5]
print(l[::-1])
# O/P : [5, 4, 3, 2, 1]

# Q 4. What will be the output of the below program
d = {"a":10, "b":20, "c": 10, "a": 100}
print(d)
# O/P : {'a': 100, 'b': 20, 'c': 10}

# Q 5. What will be the output of the below program
p = [1, 2, 3, 4]
q = p
q[0] = 100
print(p)
# O/P : [100, 2, 3, 4]

# Q 6. What will be the output of the below program
d = {"a":10, "b":20, "c": 100}
print(d["x"])
# O/P : KeyError: 'x'




