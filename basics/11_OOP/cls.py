# point.py

class Point:

    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

point = Point.__new__(Point)    # 1. Create a new instance of Point.
point.__init__(11, 44)          # 2. Initialize the new instance of Point.
print(point)     # Point(x=11, y=44)           

point1 = Point(21, 42)
print(point1)       # 1. Create a new instance of Point.
                    # 2. Initialize the new instance of Point.
                    # Point(x=21, y=42)

#----------------------------------------------------------------
class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A.")
        self.a_value = a_value

class B:
    def __new__(cls, *args, **kwargs):
        return A(42)

    def __init__(self, b_value):
        print("Initialize the new instance of B.")
        self.b_value = b_value

b = B(21)   # Initialize the new instance of A.
print(b)    # <__main__.A object at 0x780f8fb96c90>
# b.b_value   # AttributeError: 'A' object has no attribute 'b_value'. Did you mean: 'a_value'?
print(b.a_value)    # 42
print(isinstance(b, B)) # False
print(isinstance(b, A)) # True

# -----------------
class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError(f"positive width expected, got {width}")
        
        self.width = width
        if not (isinstance(height, (int, float)) and height > 0):
            raise ValueError(f"positive height expected, got {height}")

        self.height = height

rentangle = Rectangle(-21, 42)  # ValueError: positive width expected, got -21 