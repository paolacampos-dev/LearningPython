# Exercises: --------------------------------------------------------
# Declare your age as integer variable
age = 35

# Declare your height as a float variable
height = 68.7


'''
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
'''
b = int(input("what is the base of the triangle"))
h = int(input ('What is the radius of a circle?'))
area_of_triangle = 0.5 * b * h

print(area_of_triangle)

#------------------------------------------------------------

'''
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
'''

a = int(input("how long is the first side of the triangle?"))
b = int(input("how long is the second side of the triangle?"))
c = int(input("how long is the third side of the triangle?"))
perimeter_of_triangle = a + b + c
print(perimeter_of_triangle)


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input ('Wwhat is the radius of a circle?'))
pi = 3.14
area_of_circle =  pi * r * r
print(area_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2 (y = mx + b)
slope_equation = 2
b = -2
x_intercept = - b / slope_equation
y_intercept = b
#f stands for formated string literal (f-string)
print(f"x_intercept: {x_intercept}")
print(f"y_intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10) (d=(x2​−x1​)2+(y2​−y1​)^2​)
#math.sqrt() math module that calculates the square root of a number.
import math
x1 = 2
y1 =2
x2 = 6 
y2 = 10
point_one = (x1 , y1)
point_two = (x2, y2)
slope_points = (y2-y1)/(x2-x1)
print(slope_points)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance}")

# Compare the slopes in tasks 8 and 9.
slope_equation = 2
slope_points = (y2 - y1) / (x2 - x1)

print(f"Slope from equation: {slope_equation}")
print(f"Slope from points: {slope_points}")

if slope_equation == slope_points:
    print("The slopes are equal.")
else:
    print("The slopes are different.")


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len1 = len('python')
len2 = len('dragon')
print(len1 is not len2)

# refactored:
print(len('python') != len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')
    

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print( 'on' not in 'python' and 'on' not in 'jargon')

# Find the length of the text python and convert the value to float and convert it to string
str(float(len('python')))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

'''
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
'''
hours = int(input('How many hours do you work?'))
rate = int(input('What is your rate per hour?'))
total = hours * rate
print(f'Your weekly earning is {total}')

'''
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
'''
years = float(input('How old are you?'))
seconds = 60 * 60 * 24 *365
totalSeconds = years * seconds
print(f'You have lived for {totalSeconds}')

'''
Write a Python script that displays the following table
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
'''

