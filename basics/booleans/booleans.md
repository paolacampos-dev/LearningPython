Booleans class is a subclass of the int class, then inherits all its maths operations
bool()
True = 1
False = 0

T + T + T + F = 3

# Boolean or Logiacal Operators:

1. **not** (negation):
   - It is the only unary Boolean operator implemented in Python
   - not x
   - It can be applied to any object
   - It returns only True of False

   - | x   | not x |
     | --- | ----- |
     | T   | F     |
     | F   | T     |

2. **and** (conjunction):
   - It is a binary operator
   - x and y
   - Returns True only when both operands evaluate to True
   - | (x, y) | x and y |
     | ------ | ------- |
     | (T, T) | T       |
     | (T, F) | F       |
     | (F, T) | F       |
     | (F, F) | F       |

   - Return the value of one ot its operands in the truth table from above:
     - First x is evaluate it: if x is false (falsy) then x value is returned
     - Otherwise y is evaluates and the resulting value of y is returned

- **or** (disjunction):
  - Binary operator
  - x or y
  - returns False when both operands evaluate to False
  - | (x, y) | x or y |
    | ------ | ------ |
    | (T, T) | T      |
    | (T, F) | T      |
    | (F, T) | T      |
    | (F, F) | F      |
