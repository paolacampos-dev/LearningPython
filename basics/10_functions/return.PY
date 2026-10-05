# Explicit Return value:
def get_even(numbers):
    even_nums = [num for num in numbers if not num % 2]
    return even_nums
print(get_even([2, 5, 7, 8]))   # [2,8]

# Closures:
def by_factor(factor):
    def multiply(number):
        return factor * number
    return multiply

double = by_factor(2)
print(double(3))    # 6

# Decorator factores:


# Factory pattern:
class Circle:
    def __init__(self, radius):
        self.radius = radius
    # Class implementation...

class Square:
    def __init__(self, side):
        self.side = side
    # Class implementation...

def shape_factory(shape_name, *args, **kwargs):
    shapes = {"circle": Circle, "square": Square}
    return shapes[shape_name](*args, **kwargs)

# we can use that function to create shapes
circle = shape_factory("circle", radius = 20)
print(circle)   # <__main__.Circle object at 0x7dff5ea1e4e0>
print(circle.radius)    # 20

square = shape_factory("square", side = 10)
print(square)   # <__main__.Square object at 0x7dff5ea1e8d0>
print(square. side) # 10


# EXCEPTION try ...finally:
# finally.py

def func(value):
    try:
        return float(value)
    except ValueError:
        return str(value)
    finally:
        print("Run this before returning")

print(func(9))  # Run this before returning
                # 9.0