# Level 1
# Declare a first name variable and assign a value to it:
first_name = 'David'
print(first_name)

#Declare a last name variable and assign a value to it
last_name = "Harris"

#Declare a full name variable and assign a value to it
full_name = "David Harris"

#Declare a country variable and assign a value to it
country = "Spain"

#Declare a city variable and assign a value to it
city = "Barcelona"

#Declare an age variable and assign a value to it
age = 34

#Declare a year variable and assign a value to it
year = 2026

#Declare a variable is_married and assign a value to it
is_married = True

#Declare a variable is_true and assign a value to it
is_true = 5

#Declare a variable is_light_on and assign a value to it
is_light_on = 5

#Declare multiple variable on one line
first_name, last_name, country, age, is_married = 'Paola', 'Campos', 'UK', 35, False


# Level 2
#Check the data type of all your variables using type() built-in function
print(type(first_name))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print('First Name Length: ', len(first_name), 'Last Name Length: ', len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print(diff)

#Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product)

#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
reminder = num_one % num_two

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

#The radius of a circle is 30 meters.
radius = 30

#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle =  3.14 * radius ** 2

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * radius * 3.14

#Take radius as user input and calculate the area.
radius = int(input ('Wwhat is the radius of a circle?'))
area_of_circle =  3.14 * radius ** 2
print(area_of_circle)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('what is your first name')
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
country = input("What country are you from? ")
age = int(input("How old are you? "))
print(first_name, ',', last_name, ',', country, ',', age)

# advanced:
first_name, last_name, country, age = input(
    "Enter first name, last name, country, age: "
).split(",")

age = int(age)


