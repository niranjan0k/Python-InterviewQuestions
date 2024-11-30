# 1. Can we add new method to an object (class instance)?
class MyClass:
    def hello(self):
        return "Hello"

# Creating new method 
def new_method(self):
    return self.hello() + " Niranjan"

obj = MyClass()

# Now adding the new_method into the class instance
obj.new_method = new_method.__get__(obj)

# Calling new method here
print(obj.new_method()) # output: Hello Niranjan

# Yes, we can new method to an instance of a class at runtime,
# it allow for a high degree of flexibility.

# 2. How are you going to check is method was added dynamically or defined in class?
def is_dynamic_method(instance, method_name):
    method = getattr(instance, method_name, None)
    if method is None:
        return True
    return method_name not in instance.__class__.__dict__

print(is_dynamic_method(obj, 'my_method'))  # output: True
print(is_dynamic_method(obj, 'hello'))      # output: False

print("\n=======================================\n")

# 3. How are you going to modify behavior of each method in class (decorate each user method)? 

def my_decorator(method):
    def wrapper(self, *args, **kwargs):
        print(f"Before calling method '{method.__name__}'")
        result = method(self, *args, **kwargs)
        print(result)
        print(f"After calling method '{method.__name__}'")
        return result
    return wrapper

def decorate_methods(cls):
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and not attr_name.startswith("__"):
            decorated_method = my_decorator(attr)
            setattr(cls, attr_name, decorated_method)
    return cls


@decorate_methods
class TestClass:
    def hi(self):
        return "Hi!"
    def bye(self):
        return "bye"
    
obj = TestClass()
obj.hi()
obj.bye()