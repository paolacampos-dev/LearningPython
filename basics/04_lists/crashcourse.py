# counting to 20
numbers = list(range(1, 21))
print(numbers)

# add them up
print(sum(numbers))

# odd numbers and print each number
numbers = list(range(1, 21, 2))
for number in numbers:
    print(number)


# make a list of the multiples of 3, from 3 to 30
numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)

# list of the first 10 numbers
cubes = [value**3 for value in range(1, 10)]
print(cubes)
print(cubes[1:4])

# print the 3 items from the middle of a list
middle = (len(cubes)//2)
print(cubes[middle-1:middle+2])

print("The last 3 items of the list are:")
print(cubes[-3:])