class Doggo:    
    species = "Canis familiaris"    

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    
# Overriding a method from a parent class:
class BullDog(Doggo):
    def speak(self, sound="Arf"):  # default argument (then overrides the parent one is not argument is pass)
        return f"{self.name} says {sound}"

miles = BullDog("Miles", 5)
print(miles.speak()) # Miles says Arf
print(miles.speak("grrr")) # Miles says grrr

class Labrador(Doggo):
    def speak(self):
        return "Hello"

gandhi = Labrador("Gandhi", 6)
print(gandhi.speak())   # Hello

