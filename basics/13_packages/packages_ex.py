# How to import from:
# from mypackage_ex.module1 import greet
# from mypackage_ex.module2 import depart

# greet("Cedar") # Hello, Cedar!
# depart("Cedar") # Goodbay, Cedar!

from mypackage_ex.module1 import greet
from mypackage_ex.mysubpackage.module3 import people

for person in people:
    greet(person)   # Hello, Charles!
                    # Hello, Andrew!
                    # Hello, Dan!
