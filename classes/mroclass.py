# 1. What do you know about MRO (Method Resolution Order)? 
# Ans
# MRO Rule:
# 1. Depth-First Search:
#     MRO is determined using a depth-first search from the class itself to its base classes. The search respects the order of inheritance as defined in the class definition.

# 2. C3 Linearization:
#       Python employs the C3 linearization algorithm, which ensures that:
#         A class appears before its parents in the MRO.
#         If a class appears as a base in multiple classes, it should only be included once in the MRO.
#         The order of base classes in the inheritance list is preserved.

# 3. No Ambiguity:
#     MRO must avoid ambiguity. If two base classes define the same method, Python will call the method from the class that appears first in the MRO.

# 4. Base Classes Before Derived:
#     In any derived class, its base classes must come before the derived class itself in the MRO.

# 5. Object Class:
#     All classes ultimately derive from the built-in object class in Python3. Thus, the MRO will always include object as the last class in the resolution order.

class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):
    pass

class E(C, B):
    pass


d = D()
d.method()

e = E()
e.method()

# checking mro
print(D.mro())
print(D.__mro__)