class WrongNumberOfPoints(Exception):
    pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, points):
        for point in points:
            if not isinstance(point, Point):
                raise TypeError ("All points should be members of Point Class")
        self.points = points # will be a list of points

class Square(Shape):
    def __init__(self, points):
        if(len(points) !=4):
            raise WrongNumberOfPoints
        self.points = points