# 1. What is the output of the below program
print([f(2) for f in [lambda x: x * i for i in range(5)]])

# 2. Do you know what list and dict comprehensions are? Can you give an example? 
x = [(a, a+1) for a in range(5)]
y = dict((a, b) for a, b in x)
print(x)
print(y)

# 3. Show me three different ways of fetching every third item in the list 
theList = [1, 2, 4, 3, 9, 5, 8, 6]
print([x for i, x in enumerate(theList) if i%3 == 0])

for i, x in enumerate(theList):
    if i % 3:
        continue
    # yield x
    print(x)

a = 0
for x in theList:
    if a%3:
        a += 1
        continue
    # yield x
    a += 1
    print(x)

# 