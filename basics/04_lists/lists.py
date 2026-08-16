# A. Exercises: Level 1

# 1. Declare an empty list

# 2. Declare a list with more than 5 items

# 3. Find the length of your list

# 4. Get the first item, the middle item and the last item of the list

# 5. Declare a list called mixed_data_types, put your name, age, height, marital status and address

# 6. Declare a list variable named it_companies and assign the initial values:
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon

# 7. Print the list using print()

# 8. Print the number of companies in the list

# 9. Print the first, middle and last company

# 10. Print the list after modifying one of the companies

# 11. Add an IT company to it_companies

# 12. Insert an IT company in the middle of the companies list

# 13. Change one of the it_companies names to uppercase (IBM excluded!)

# 14. Join the it_companies with the string '#; '

# 15. Check if a certain company exists in the it_companies list

# 16. Sort the list using the sort() method

# 17. Reverse the list in descending order using the reverse() method

# 18. Slice out the first 3 companies from the list

# 19. Slice out the last 3 companies from the list

# 20. Slice out the middle IT company or companies from the list

# 21. Remove the first IT company from the list

# 22. Remove the middle IT company or companies from the list

# 23. Remove the last IT company from the list

# 24. Remove all IT companies from the list

# 25. Destroy the IT companies list

# 26. Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node', 'Express', 'MongoDB']

# 27. After joining the lists in question 26, copy the joined list and assign it
# to a variable called full_stack. Then insert Python and SQL after Redux.




# B. Exercises: Level 2

# 1. The following is a list of 10 students' ages: 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the minimum and maximum age
ages.sort() #changes the original list still ages() just ordered
print(ages)

print(ages[0])
print(ages[-1])
# Add the minimum age and the maximum age again to the list
ages.insert(0, ages[0])  # or ages.apend(ages[0])
ages.append(ages[-1])
# Find the median age
middle = len(ages) // 2
ages[middle - 1]
print(ages[middle])

middle = len(ages) // 2
median = (ages[middle - 1] + ages[middle]) / 2
print(median)

# Find the average age
count = len(ages)
total = sum(ages)
average = total / count

# Find the range of the ages (maximum age minus minimum age)
ages.sort()
print(ages[-1] - ages[0])

# Compare the value of (min - average) and (max - average)
# using the abs() function
min_diff = ages[0] - average
max_diff = ages[-1] - average
min_abs = abs(min_diff)
max_abs = abs(max_diff)
print(min_abs == max_abs)



# Given the following list:
countries = [
    'China',
    'Russia',
    'USA',
    'Finland',
    'Sweden',
    'Norway',
    'Denmark'
]

# 2. Find the middle country or countries in the countries list
print(len(countries)) #7
print(countries[3])
# or:
middle = len(countries) // 2
print(countries[middle])

# 3. Divide the countries list into two equal lists. If the number of countries is odd, the first half should contain one more country.
first_half = countries[:middle + 1]
second_half = countries[middle + 1:]
print(first_half)
print(second_half)

# Unpack the first three countries and assign the rest to a variable called scandic countries
first, second, third, *scandic_countries = countries
print(countries)







