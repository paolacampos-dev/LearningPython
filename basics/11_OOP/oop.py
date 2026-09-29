# create a class:
class Car:
    pass # placeholder
print(Car) # <class '__main__.Car'>

# to instanciate it:
Car()
print(Car()) # <__main__.Car object at 0x7b4f4b82e6c0>


# =====================================================================
class Point:
    dimensions = 2              # Class atribute: available from the class itself and all instances derived from it
    def __init__(self, x, y):  # the constructor (the sefl object)
        self.x = x
        self.y = y
# print(Point) # <class '__main__.Point'> without the dunder method __str__

# Dunder methods:
    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def __str__(self):
        return f"Point at x: {self.x}, y: {self.y}"
    
    def __eq__(self, other):
        return (
            self.x == other.x and 
            self.y == other.y
        )


# When instanciating we need to pass as many parameters as found in the constructor:
Point(10, 19)

print(Point(20, 30)) # <__main__.Point object at 0x7641ed4027b0>

origin = Point(0, 0)
target = Point(10, 15)
print(origin.x)  # 0
print(target.y)  # 15
print(Point.dimensions)     # 2
print(origin.dimensions)    # 2

center = Point(50, 50)
print(center)   # Point at x: 50, y: 50

distance = Point(25, 25)
center + distance
print(center) # Point at x: 75, y: 75


# Attributes can be changed at a runtime:
target.x = 12
print(target.x) # 12

Point.dimensions = 3
print(Point.dimensions) # 3

# Creating a list from the object class:
shape = [Point(0, 0), Point(5, 5), Point(2, 3)]  # Triangle
print(shape[2].x)   # 2

print(isinstance(origin, Point))    # True
print(origin == target) # False



# ========================================================
class Doggo:
    species = "Canis familiaris"    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instance a method (self is what gives access to the constructor atributes):
    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# print(miles)    # <__main__.Doggo object at 0x7dfd3862e480>  that doesnt give us any info about miles without the __str__ dunder method
# with dunder method __str__ means that everytime we call print that is the info is going to give us for that instance(object) in this case miles
    def __str__(self):
        return f"{self.name} is {self.age} years old"

miles = Doggo("Miles", 4)
print(miles.description())      # Miles is 4 years old
print(miles.speak("Woof Woof")) # Miles says Woof Woof
print(miles)    #Miles is 4 years old 

# dir() --> shows you all the methods are available
print(dir(miles))   # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'description', 'name', 'speak', 'species']



