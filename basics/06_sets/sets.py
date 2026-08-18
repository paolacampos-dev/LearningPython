# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Exercises: Level 1
#1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['X', 'Netwie'])

# 4. Remove one of the companies from the set it_companies
it_companies.remove('X')

# 5. What is the difference between remove and discard?


# Exercises: Level 2
# 1. Join A and B
A.union(B)

# 2. Find A intersection B
A.intersection(B)

# 3. Is A a subset of B?
A.issubset(B)

# 4. Are A and B disjoint sets?
A.isdisjoint(B)

# 5. Join A with B and B with A
A.union(B)
B.union(A)

# 6. What is the symmetric difference between A and B?
A.symmetric_difference(B)

# 7. Delete the sets completely
del A
del B


# Exercises: Level 3
# 1. Convert the ages to a set and compare the length of the list and the set. Which one is bigger?
print(len(age))
set_age = set(age)
print(len(set_age))

# 2. Explain the difference between the following data types: string, list, tuple, and set
# The set is not bigger—the list is bigger because it contains repeated ages.

'''
3. "I am a teacher and I love to inspire and teach people."
    How many unique words have been used in the sentence?
    Use the split() method and set to get the unique words.
'''
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print(len(unique_words))