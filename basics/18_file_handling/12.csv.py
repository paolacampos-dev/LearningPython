import csv
from pathlib import Path

path = Path("people-100.csv")

# READ Data with a csv.reader(): ==========================================================================
with path.open(encoding="utf-8", newline="") as file: # mode="r" is the default mode
    reader = csv.reader(file)   
    for row in reader:  # it provides the rows to read as strings
        print(row)  
        # ['Index', 'User Id', 'First Name', 'Last Name', 'Sex', 'Email', 'Phone', 'Date of birth', 'Job Title']
        # ['1', '88F7B33d2bcf9f5', 'Shelby', 'Terrell', 'Male', 'elijah57@example.net', '001-084-906-7849x73518', '1945-10-26', 'Games developer']
        # ['2', 'f90cD3E76f1A9b9', 'Phillip', 'Summers', 'Female', 'bethany14@example.com', '214.112.6044x4913', '1910-03-24', 'Phytotherapist']
        # ['3', 'DbeAb8CcdfeFC2c', 'Kristine', 'Travis', 'Male', 'bthompson@example.com', '277.609.7938', '1992-07-02', 'Homeopath']
        # upto the 100's

file = path.open(encoding="utf-8", newline="")
reader = csv.DictReader(file)
print(reader.fieldnames)    # ['Index', 'User Id', 'First Name', 'Last Name', 'Sex', 'Email', 'Phone', 'Date of birth', 'Job Title']
for row in reader:
    print(row)  # every row is now a pict dictionary with keys and values
                # {'Index': '1', 'User Id': '88F7B33d2bcf9f5', 'First Name': 'Shelby', 'Last Name': 'Terrell', 'Sex': 'Male', 'Email': 'elijah57@example.net', 'Phone': '001-084-906-7849x73518', 'Date of birth': '1945-10-26', 'Job Title': 'Games developer'}
                # {'Index': '2', 'User Id': 'f90cD3E76f1A9b9', 'First Name': 'Phillip', 'Last Name': 'Summers', 'Sex': 'Female', 'Email': 'bethany14@example.com', 'Phone': '214.112.6044x4913', 'Date of birth': '1910-03-24', 'Job Title': 'Phytotherapist'}
                # {'Index': '3', 'User Id': 'DbeAb8CcdfeFC2c', 'First Name': 'Kristine', 'Last Name': 'Travis', 'Sex': 'Male', 'Email': 'bthompson@example.com', 'Phone': '277.609.7938', 'Date of birth': '1992-07-02', 'Job Title': 'Homeopath'}
                # upto 100's
file.close()


# WRITE Data with a csv.writer(): ============================================================================
with open("people.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)   # can be a list or a tupple
    writer.writerow(["John", "Doe", 42])
    writer.writerow(["Anna", "Smith", 42])
    writer.writerows([
        ["John", "Doe", 42],
        ["Anna", "Smith", 42],
    ])

with open("people.csv", mode="w", encoding="utf-8", newline="") as file:
    columns = ["first_name", "last_name", "age"]
    writer = csv.DictWriter(file, columns)   
    writer.writeheader()
    writer.writerow({
        "first_name": "John", "last_name": "Doe", "age": 42
    })


