anna = {
    'first': 'Anna', 
    'last': 'Clarck', 
    'city': 'Madrid'
}

laura = {
    'first': 'Laura', 
    'last': 'Winston', 
    'city': 'London'
}

peter = {
    'first': 'Peter', 
    'last': 'Smith', 
    'city': 'Leeds'
}

people = [anna, laura, peter]

for person in people:
    print(f"Friend: {person}")
    full_name = f"{person['first']} {person['last']}"
    location = person['city']

    print(f"Full name: {full_name}")
    print(f"Location: {location}")

# --------------------------------------------
# A dictionary in a dictionary:
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


# --------------------------------------------------
# People: Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
person_1 = {
    'first': 'albert',
    'last': 'einstein',
    'age': 76,
    'city': 'princeton',
}

person_2 = {
    'first': 'marie',
    'last': 'curie',
    'age': 66,
    'city': 'paris',
}

person_3 = {
    'first': 'isaac',
    'last': 'newton',
    'age': 84,
    'city': 'cambridge',
}
people = [person_1, person_2, person_3]
for person in people:
    full_name = f"{person['first']} {person['last']}"
    location = person['city']
    age = person['age']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tI am {age} years old")
    print(f"\tLocation: {location.title()}")
    print("\n")



# --------------------------------------------------------------
# Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and, as you do, print everything you know about each pet.
pet_1 = {
    'animal': 'dog',
    'owner': 'john',
}

pet_2 = {
    'animal': 'cat',
    'owner': 'sarah',
}

pet_3 = {
    'animal': 'rabbit',
    'owner': 'mike',
}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    animal = pet['animal']
    owner = pet['owner']
    print(f"{owner.title()} is the owner of a {animal}")


# Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person's name and their favorite places.
favorite_places = {
    'john': ['paris', 'london', 'tokyo'],
    'sarah': ['new york', 'rome', 'barcelona'],
    'mike': ['dubai', 'istanbul', 'seoul'],
}
for person, favorite_places_info in favorite_places.items():
    print(f"{person.title()}'s favourite places are: {favorite_places_info}")


# Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.

favorite_numbers = {
    'john': [7, 21, 42],
    'sarah': [3, 8, 15],
    'mike': [10, 25, 50],
}
for person, favorite_number in favorite_numbers.items():
    print(f"{person.title()}'s favourite numbers are: {favorite_number}")


# Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'The Eiffel Tower is in Paris.',
    },

    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'Tokyo is the capital of Japan.',
    },

    'cairo': {
        'country': 'egypt',
        'population': 10000000,
        'fact': 'Cairo is near the pyramids of Giza.',
    },
}

for capitals, city in cities.items():
    print(f"Capital of {city['country'].title()} is {capitals.title()} with a population of {city['population']} and {city['fact']}")

# Exercise: We're now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
cities = {
    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'The Eiffel Tower is in Paris.',
        'language': 'french',
        'continent': 'europe',
    },

    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'Tokyo is the capital of Japan.',
        'language': 'japanese',
        'continent': 'asia',
    },

    'cairo': {
        'country': 'egypt',
        'population': 10000000,
        'fact': 'Cairo is near the pyramids of Giza.',
        'language': 'arabic',
        'continent': 'africa',
    },
}
for capitals, city in cities.items():
    # print(f"The country of {city['country'].title()}, its capital is {capitals} and its continent is {city['continent'].title()}.\n{capitals.title()} has {city['population']/ 1_000_000} million of people who speak {city['language']}")
    print(
        f"The country of {city['country'].title()}, its capital is "
        f"{capitals.title()} and its continent is {city['continent'].title()}."
    )
    print(
        f"{capitals.title()} has {city['population'] / 1_000_000} "
        f"million people who speak {city['language'].title()}.\n"
    )