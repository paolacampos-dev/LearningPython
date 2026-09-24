"""Creates a database with an 'employees' table and one record."""

import sqlite3

DATABASE_NAME = "company.db"

# ---------------- Create the DB ----------------
with sqlite3.connect(DATABASE_NAME) as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Create a table named 'employees'
    cursor.execute("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT
        )
    """)

    # Insert a record into the 'employees' table
    cursor.execute("""
        INSERT INTO employees (id, name, role)
        VALUES (?, ?, ?)
    """, (1, "Adisa", "Software Engineer"))