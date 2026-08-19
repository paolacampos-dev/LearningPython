# 💻 Exercises:

# Exercises: Level 1
'''
1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```
'''
age = int(input('enter your age: ' ))
if age >= 18:
    print('You are old enough to drive')
else:
    missing_years = 18 - int(age)
    print(f'You need {missing_years} more years to learn to drive')


'''
2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```
'''
age = int(input('Enter your age: '))
my_age = 25

if age > my_age:
    difference = age - my_age
    if difference == 1:
        print(f'You are {difference} year older than me.')
    else:
        print(f'You are {difference} years older than me.')
elif age < my_age:
    difference = my_age - age
    if difference == 1:
        print(f'You are {difference} year younger than me.')
    else:
        print(f'You are {difference} years younger than me.')
else:
    print('We are the same age.')


'''
3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```
'''
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is less than {b}')
else:
    print(f'{a} and {b} are equal')

# Exercises: Level 2
'''
1. Write a code which gives grade to students according to theirs scores:
    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```
'''
score = int(input('Enter your score: '))

if score >= 90:
    print('You got and A')
elif score >=80:
    print('you got a B')
elif score >= 70:
    print('You got a C')
elif score >= 60:
    print('You got a D')
else:
    print('You got an F')


'''
2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
    June, July or August, the season is Summer

month = input('Which month are we now: ')
if month == 'September' or month == 'October' or month == 'November':
    print('Is Autumn')
'''
month = input('Which month are we now: ').capitalize() #accepts all: september, September, SEPTEMBER and convert them all to September
if month in ['September', 'October', 'November']:
    print('It is Autumn')
elif month in ['December', 'January', 'February']:
    print('It is Winter')
elif month in ['March', 'April', 'May']:
    print('It is Spring')
elif month in ['June', 'July', 'August']:
    print('It is Summer')
else:
    print('Invalid month')


'''
3. The following list contains some fruits:
    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```
    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''
fruit = input('Tell me a fruit: ')
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit not in fruits:
        fruits.append(fruit)
        print(fruits)
else:
    print('That fruit already exist in the list')

# Exercises: Level 3

# 1. Here we have a person dictionary. 
person={
    'first_name': 'Paola',
    'last_name': 'Campos',
    'age': 25,
    'country': 'Uk',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'postcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    middle = len(person['skills']) // 2
    print(person['skills'][middle])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    if 'Python' in person['skills']:
        print('True')
    elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('This person is a EF dev')
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('This person is a backend developer')

    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('This person is a fullstack developer')

    else:
        print('Unknown title')

#another way:
if 'skills' in person:
    if 'Python' in person['skills']:
        print(True)
    else:
        print(False)

    if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('This person is a fullstack developer')

    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('This person is a backend developer')

    elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('This person is a front end developer')

    else:
        print('Unknown title')     

'''
If the person is not married and if she lives in the Uk, print the information in the following format:
```py
    Paola Campos lives in the Uk. She is not married.
```
'''
if not person['is_married'] and person ['country'] == 'Uk':
    print(f"{person['first_name']} {person['last_name']} lives in the Uk. She is not married.") 