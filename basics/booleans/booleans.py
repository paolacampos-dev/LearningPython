# 1. AND:
from itertools import product 

for x, y in product([True, False], repeat=2):
    print(f"\t{x} and {y} = {x and y}")
        # True and True = True
        # True and False = False
        # False and True = False
        # False and False = False

for x, y in product([True, False], repeat=2):
    print(f"\t{x} and {y} = {x or y}")
        #  True and True = True
        # True and False = True
        # False and True = True
        # False and False = False


# Chaining function calls:
from pathlib import Path

file = Path("hello.txt")
file.touch()
file.read_text()

# To all function be execute it all of them need to be true, if one is not it will end there the execution of the code
file.exists() and file.write_text("Hello!") and file.read_text()


# 2. OR:
# default values:
a = []
b = {}

x = a or b or None
print(x)

default = "Sunday"
a = "Monday"

y = a or default
print(y)    # Monday

a = ""

y = a or default
print(y)     #Sunday


# Divide by zero:
def divide(a, b):
    return b == 0 or a / b
print(divide (95, 3))   # 31.66666
print(divide(5,0))  # True


def dividing():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    quotient = divide(a, b)

    if quotient == True:
        print("no result, division by zero attempted")
    else:
        print(f"The result of {a} divided by {b} is {quotient}.")

print(dividing())




