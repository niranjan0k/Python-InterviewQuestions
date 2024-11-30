def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(*[1, 2], name="Alice", age=30)