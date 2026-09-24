"""Reads and displays data from a SQLite database."""
# An example of how a DB will be displayed as a tuple:
# create.py

import sqlite3

with sqlite3.connect("company.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")

    # Fetch one row - this will be returned as a tuple
    row = cursor.fetchone()

    # Print the row
    print(row) # (1, 'Adisa', 'Software Engineer')
    print(type(row)) # <class 'tuple'>

    # Unpack the values
    employee_id, name, role = row
    print(name) # Adisa
    print(role) # Software Engineer