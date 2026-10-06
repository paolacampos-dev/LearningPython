# In case need a custom object creator:
# 1. Create a New Instance with super(). __new__()
# 2. Customize the New Instance
# 3. Return the New Instance

# custom_new_example.py

class SomeClass:
    def __new__(cls, *args, **kwargs):  # always define it with *args and *kwargs
        instance = super().__new__(cls) # just accept cls as argmts
        # Customize instance here...
        return instance

class SomeClass:
    def __init__(self, value):
        self.value = value

some_obj = SomeClass(42)
print(some_obj) # <__main__.SomeClass object at 0x7ad10d97a8a0>