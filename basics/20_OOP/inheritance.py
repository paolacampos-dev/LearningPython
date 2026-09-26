# to create a variation of a class:

class Doggo:
    species = "Canis familiaris"    

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    # the same as:
        # return (
        #     f"{self.name} is"
        #     f"{elf.age} years old"
        # )

    def speak(self, sound):
        return f"{self.name} says {sound}"

class Bulldog(Doggo):
    pass

jack = Bulldog("Jim", 5)
print(jack) # Jim is 5 years old
print(jack.speak("buf")) # Jim says buf


# using composition and inheritance together: ==========================================

# Very common way to raise exceptions in python as a subclass:
class WrongNumberOfPoints(Exception):
    pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, points):
        self.points = points # will be a list of points

class Square(Shape):
    def __init__(self, points):
        if(len(points) !=4):
            raise WrongNumberOfPoints
        self.points = points

# square = Square([])
# print(square) # WrongNumberOfPoints

square = Square([
    Point(0, 0), 
    Point(1, 0), 
    Point(1, 1), 
    Point(0, 1), 
])
print(square)   # <__main__.Square object at 0x74bf4a6a6870>