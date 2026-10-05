# 1. Attributes:
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property   # decorator: creates a method  that is accessed as an attribute
    def full_name(self):
        return f"{self.first} {self.last}"

tim = Person("Tim", "of Tivia")
print(tim.full_name)    # Tim of Tivia

#====================================
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("Radius must be a postive number")
        self._radius = value   # store the value in a non public attribute (private)

small = Circle(3)
print(small.radius) # 3

small.radius = 4
print (small.radius)    # 4



# 2. Methods:
# vehicle.py

class Vehicle:

    @classmethod
    def water_vehicle(cls, name, dimensions):
        vehicle = cls()
        vehicle.name = name
        vehicle.dimensions = dimensions
        vehicle.floats = True
        vehicle.num_wheels = 0
        return vehicle

    @classmethod
    def road_vehicle(cls, name, dimensions, num_wheels):
        vehicle = Vehicle()
        vehicle.name = name
        vehicle.dimensions = dimensions
        vehicle.floats = False
        vehicle.num_wheels = num_wheels
        return vehicle

    def volume(self):
        return self.dimensions[0] * self.dimensions[1] * self.dimensions[2]

    @staticmethod
    def all_float(vehicles):
        for vehicle in vehicles:
            if not vehicle.floats:
                return False
        return True

boat = Vehicle.water_vehicle ("Mirrow", (30, 40, 10))
print(boat.name)    # Mirrow

