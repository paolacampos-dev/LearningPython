# built in print():

# Back Slash End "\":
# | Character | Meaning                            |
# | --------- | ---------------------------------- |
# | `\n`      | Newline                            |
# | `\t`      | Tab                                |
# | `\a`      | ASCII Bell                         |
# | `\ooo`    | Character with octal value `"ooo"` |
# | `\xhh`    | Character with hex value `"hh"`    |
# | `\\`      | Backslash                          |
# | `\"`      | Double quote                       |
# | `\'`      | Single quote                       |
# | `\b`      | Backspace                          |
# | `\r`      | Carriage return                    |


# Formating strings:
# | Method            | Example                                       | Notes                              |
# | ----------------- | --------------------------------------------- | ---------------------------------- |
# | **C-style (`%`)** | `'Hello %s' % name`                           | Older style                        |
# | **`.format()`**   | `'My name is {}, {}'.format('James', 'Bond')` | Added in Python 3.0                |
# | **f-string**      | `f'I am {age} years old'`                     | Added in Python 3.6; commonly used |

# C-style:
first = 'James'
last = 'Bond'
age = 90

message = 'No, Mr. %s, I expect you to die!' % last
print(message)
print('The name is %s, %s %s' % (last, first, last))
print('Sean Connery is now %d years old' % age)

import math
print('pi: %f, %s' % (math.pi, math.pi))

# f-string literals:
message2 = f'No, Mr {last} I expect you to see'
print(message)
print(f'The name is {last}, {first}')


# Print can take multiple arguments:
# print(*objets, sep=' ', end='\n', file=sys.stdout, flush=False)  # default values
# Flush has to do with it is store momentaneantly in the buffer. if True is shows the output immediatly
# "*objects" argument is accesible as a list inside of the function, but after define it, the other arguments must be define too ??
print('There are', 6, 'members')    # we cant add an interger to a string in print() is a TypeError
message = 'There are' + str(6)  + 'members'
print(message)

members =   [
    ['year', 'last', 'first'],
    [1943, 'Idle', 'Eric'],
    [1939, 'Cleese', 'John']
]
for row in members:
    print(*row, sep=", ")   # year, last, first
                            # 1943, Idle, Eric
                            # 1939, Cleese, John


# count_items:
def count_items(items):
    print('Counting', end=' ')
    num = 0
    for item in items:
        num += 1
        print('.', end='')

    print(f'\nThere were {num} items')
