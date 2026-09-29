players = ['John', 'Mike', 'Bob']

count = 0
for player in players:
    print(count, player)
    count += 1  # 0 John
                # 1 Mike
                # 2 Bob

# Refactoring iy:
for count, player in enumerate(players):
    print(count, player)    # 0 John
                            # 1 Mike
                            # 2 Bob

# =====================================================
countries = ['France', 'Tanzania', 'Canada']
continents = ['Europe', 'Africa', 'North America']

merged = []
for i in range(len(countries)):
    merged.append((countries[i], continents[i]))
print(merged)   #  [('France', 'Europe'), ('Tanzania', 'Africa'), ('Canada', 'North America')]

# refactoring it with the zip():
merged_2 = zip(countries, continents)
print(merged_2) # <zip object at 0x703e3c22b500>
print(list(merged_2))   # [('France', 'Europe'), ('Tanzania', 'Africa'), ('Canada', 'North America')]

for i in range(100):
    print(i, end=' ')   # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 




## 💻 Exercises: Day 10

### Exercises: Level 1

#1. Iterate 0 to 10 using for loop, do the same using while loop.
#2. Iterate 10 to 0 using for loop, do the same using while loop.

'''
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

```py
    #
    ##
    ###
    ####
    #####
    ######
    #######
```
'''

'''
4. Use nested loops to create the following:
```sh
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
```
'''

'''
5. Print the following pattern:
```sh
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100
```
'''


#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
#7. Use for loop to iterate from 0 to 100 and print only even numbers
#8. Use for loop to iterate from 0 to 100 and print only odd numbers

### Exercises: Level 2
'''
1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
```sh
The sum of all numbers is 5050.
```
'''

'''
2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
```sh
    The sum of all evens is 2550. And the sum of all odds is 2500.
```
'''

### Exercises: Level 3
#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

'''
3. Go to the data folder and use the countries_data.py file.
    a. What are the total number of languages in the data
    b. Find the ten most spoken languages from the data
    c. Find the 10 most populated countries in the world
'''