# Composing with classes (use one class as a way of building the attributes of another class):

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, points):
        self.points = points # will be a list of points

triangle = Shape([
    Point(0, 0),
    Point(5, 5),
    Point(2, 4)
])

print(triangle.points) # [<__main__.Point object at 0x7ba077c5e6c0>, <__main__.Point object at 0x7ba077c5e630>, <__main__.Point object at 0x7ba077c5e930>]

bottom_left = Point(0, 0)
bottom_right = Point(10, 0)
top_left = Point(0, 10)
top_right = Point(10, 10)

square = Shape([bottom_left, bottom_right, top_left, top_right])
print(square) # <__main__.Shape object at 0x71f4f737e6f0>
print(square.points) # [<__main__.Point object at 0x72133ce7e7e0>, <__main__.Point object at 0x72133ce7ea20>, <__main__.Point object at 0x72133ce7e990>, <__main__.Point object at 0x72133ce7e8a0>]