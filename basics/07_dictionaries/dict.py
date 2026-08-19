
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