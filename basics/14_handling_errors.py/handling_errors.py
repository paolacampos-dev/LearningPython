# int(input()):
while True:
    # Loop until the user gives a valid answer
    try:
        age = int(input("How old are you? "))
        print(f"Next year you will be {age + 1}")
        break
    except ValueError:
        print("Please enter a number for your age")

