inventory = {
    "goblet": 25,
    "loaf of bread": 30,
    "quill": 10,
    "rose": 8,
    "mead": 0,
}

request_list = ["goblet", "mead", "rose", "dagger"]


def inquire_availability(ware):
    if ware not in inventory:
        print("We trade not in {ware}")
    elif inventory[ware] <= 0:
        print(f"Forgive me, but {ware} is not at hand.")
    else:
        print(f"inventory[ware] of {ware} dost remain!")

for ware in request_list:
    inquire_availability(ware)  # Forgive me, but mead is not at hand.
                                # inventory[ware] of rose dost remain!
                                # We trade not in {ware}
