# Creating Lists in Python

There are several ways to create and populate lists in Python.

## 1. Using `for` Loops

    1. Create an empty list.
    2. Loop over an iterable, such as `range()`.
    3. Append each result to the end of the list.

## 2. Using map() Objects:

    - pass in a funciotn and an iterable, and map() will create an object containing the output

## list comprehensions (more pythonic)

    - define the list and its contents at the same time
    - new_list = [expresion for member in iterable]
    - a single tool that can be use in many different situation (for mapping and looping)
    - dont need to remember the proper order of arguments

new_list1 = [ expression for member in iterable]
new_list2 = [expression for member in iterable (if conditional)]
new_list3 = [expression (if conditional) for member in iterable ]

# set and dict comprehension:

    - set comprehension the output no duplicates and with no particular order
    - {} instead of []

# the walrus operator:

    - also known as the assignment expression
    - it allows to run an expression while simultaneously assigning the output value to a variable
