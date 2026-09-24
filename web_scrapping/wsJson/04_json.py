import json

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

json_str = json.dumps("Will", 29)
print(json_str) # gives an error
