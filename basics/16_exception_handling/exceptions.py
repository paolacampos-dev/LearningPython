names = ["Sue", "Jaspreet", "Alex"]

# names[3] throw an IndexError then we create the exception:
try:
    names[3]
except IndexError:
    print("Your list doesn't have that index")
# multiple excepts:
# else:
# finally:


# built-in exceptions in pyton:
# https://docs.python.org/3/builtins/exceptions.html

def squared(numbers):
    if not isinstance(numbers, (list | tuple)):
        raise TypeError("function only supports lists or tuples")
    return [number**2 for number in numbers]


# Custom exceptions (exceptions are objects):
class GradeValueError(Exception):
    pass

def calculate_average(grades):
    total = 0
    for grade in grades:
        if grade < 0 or grade > 100:
            raise GradeValueError("grade must be between 0 and 100")
        total += grade
    return round(total / len(grades), 2)

calculate_average([85, 90, 110])    # GradeValueError: grade must be between 0 and 100

# Exception Object as an instance:
try:
    result = 42 / 0
except Exception as error:
    error.add_note("Infinite or undefined, you decide")
    my_error = error
    tb = error.__traceback__

my_error

# ---------------------------------------
class GradeValueError(Exception):
    pass

raise GradeValueError("Invalid grade")






