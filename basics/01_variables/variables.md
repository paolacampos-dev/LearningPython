# Built in functions

In Python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following:

| Function  | Function      | Function  | Function       | Function         |
| --------- | ------------- | --------- | -------------- | ---------------- |
| `abs()`   | `delattr()`   | `hash()`  | `memoryview()` | `set()`          |
| `all()`   | `dict()`      | `help()`  | `min()`        | `setattr()`      |
| `any()`   | `dir()`       | `hex()`   | `next()`       | `slice()`        |
| `ascii()` | `divmod()`    | `id()`    | `object()`     | `sorted()`       |
| `bin()`   | `enumerate()` | `input()` | `oct()`        | `staticmethod()` |
| `bool()`  | `eval()`      | `int()`   | `open()`       | `str()`          |

---

# Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

## Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables

Python developers use snake case(**snake_case**) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

Example:
first_name = 'Paola'
last_name = 'Campos'
country = 'UK'
city = 'London'
age = 35
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
'firstname':'Paola',
'lastname':'Campos',
'country':'UK',
'city':'London'
}
Let us use the print() and len() built-in functions.
Print function takes unlimited number of arguments.
An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

Example:
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

Example:

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

Declaring Multiple Variable in a Line
Multiple variables can also be declared in one line:
Example:
first_name, last_name, country, age, is_married = 'Paola', 'Campos', 'UK', 35, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

## the input() built-in function.

Let us assign the data we get from a user into first_name and age variables.
Example:
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Check Data types--> 00_dataTypes

## Let's declare variables with various data types

first_name = 'Paola' # str
last_name = 'Campos' # str
country = 'UK' # str
city= 'London' # str
age = 35 # int

## Printing out types

print(type('Paola')) # str
print(type(first_name)) # str
print(type(10)) # int
print(type(3.14)) # float
print(type(1 + 1j)) # complex
print(type(True)) # bool
print(type([1, 2, 3, 4])) # list
print(type({'name':'Paola'})) # dict
print(type((1,2))) # tuple
print(type(zip([1,2],[3,4]))) # zip

# Casting:

**Converting one data type to another data type.**
We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

Examples:

## int to float

num_int = 10
print('num_int',num_int) # 10
num_float = float(num_int)
print('num_float:', num_float) # 10.0

## float to int

gravity = 9.81
print(int(gravity)) # 9

## int to str

num_int = 10
print(num_int) # 10
num_str = str(num_int)
print(num_str) # '10'

## str to int or float

num_str = '10.6'
num_float = float(num_str) # Convert the string to a float first
num_int = int(num_float) # Then convert the float to an integer
print('num_int', int(num_str)) # 10
print('num_float', float(num_str)) # 10.6
num_int = int(num_float)
print('num_int', int(num_int)) # 10

## str to list

first_name = 'Paola'
print(first_name) # 'Paola'
first_name_to_list = list(first_name)
print(first_name_to_list) # ['P', 'a', 'o', 'l', 'a']

# Exercises to practice:

## Level 1

Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line

## Level 2

Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
