my_dog = {
    "name": "Frieda",
    "age": 5,
    "nicknames": ["Fru-Fru", "Lady McNugget"],
    "hungry": True
}

print(my_dog)   # {'name': 'Frieda', 'age': 5, 'nicknames': ['Fru-Fru', 'Lady McNugget'], 'hungry': True}


# to acces the key called name:
print(my_dog["name"])  # Frieda

# Add a new value pair to the dict:
my_dog["breed"] = "poodle"
print(my_dog)  # {'name': 'Frieda', 'age': 5, 'nicknames': ['Fru-Fru', 'Lady McNugget'], 'hungry': True, 'breed': 'poodle'}

# Change value:
my_dog["age"] = 6
print(my_dog) # {'name': 'Frieda', 'age': 6, 'nicknames': ['Fru-Fru', 'Lady McNugget'], 'hungry': True, 'breed': 'poodle'}

# Delete a key-value pair:
del my_dog["hungry"]


# Check from a value:
print(my_dog["breed"]) # poodle

if "hungry" in my_dog:
    print(my_dog["hungry"])  # because it doesnt exist it doesnt give an error


# Loop over a dict:
# Over the keys:
for features in my_dog:
    print(features)     # name
                        # age
                        # nicknames
                        # breed
# Over the pair-values:
for features in my_dog:
    print(features, my_dog[features])   # name Frieda
                                        # age 6
                                        # nicknames ['Fru-Fru', 'Lady McNugget']
                                        # breed poodle
# This way of code is more Pythonic:
for features, character in my_dog.items(): 
    print(features, character)              # name Frieda
                                            # age 6
                                            # nicknames ['Fru-Fru', 'Lady McNugget']
                                            # breed poodle

# Nesting dictionaries:======================================================================
states = {
    "California": {
        "capital": "Sacramento",
        "flower": "California Poppy"
    },
    "New York": {
        "capital": "Albany",
        "flower": "Rose"
    },
    "Texas": {
        "capital": "Austin",
        "flower": "Bluebonnet"
    }
}

for state, facts in states.items():
    print(state, facts)    # California {'capital': 'Sacramento', 'flower': 'California Poppy'}
                            # New York {'capital': 'Albany', 'flower': 'Rose'}
                            # Texas {'capital': 'Austin', 'flower': 'Bluebonnet'}
# To access just flower:
for state, facts in states.items():
    print(state, facts["flower"])  

# aceess the nexted value directly:
print(states["Texas"]["capital"]) # Austin

# challenge:

captains = {
    "Enterprise": "Picard",
    "Voyager": "Janeway",
    "Defiant": "Sisko", 
}

if "Enterprise" in captains:
    print("Exists")
else:
    print("unkonwn")  # Exists

if "Discovery" in captains:
    print("Exists")
else:
    print("unkonwn")  # Unknown

# for key, value in dictionary.items():
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")  # The Enterprise is captained by Picard
                                                    # The Voyager is captained by Janeway
                                                    # The Defiant is captained by Sisko




# 💻 Exercises: 

#1. Create  an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Chalie'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# 3. Create a student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML', 'CSS'],
    'country': 'United Kingdom',
    'city': 'London',
    'address': '123 Main Street'
}

print(student)

#4. Get the length of the student dictionary
print(len(student))

#5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

#6. Modify the skills values by adding one or two skills
student['skills'].extend(['PHP', 'Next']) # add multiple items
student['skills'].append('React') # add just one item
student['skills'] = ['Flask', 'SQL'] # replace the entire skills list with a tupple

#7. Get the dictionary keys as a list
keys = student.keys()
print(keys)

#8. Get the dictionary values as a list
values = student.values()
print(values)

#9. Change the dictionary to a list of tuples using _items()_ method
items = list(student.items())
print(items)

#10. Delete one of the items in the dictionary
del student['address']

#11. Delete one of the dictionaries
del dog