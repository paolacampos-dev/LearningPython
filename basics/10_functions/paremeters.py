# 1. Function with NO PARAMETERS:
shopping_list = {   # global variable
    "Bread": 1,
    "Milk": 2,
    "Chocolate": 1,
    "Butter": 1,
    "Coffee": 1,
}

def show_list():
    for item_name, quantity in shopping_list.items():
        print(f"{item_name}: {quantity}")
print(show_list())


# 2. With parameters:
shopping_list = {}  # Global scope varible

def add_item(item_name, quantity):  # parameters (placeholders)
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item("apples", 3)   # required arguments 
add_item("apples", 2)
add_item("bread", 1)
print(shopping_list)    # {'apples': 5, 'bread': 1}

# Refactoring it (keys() are not need it here):
def add_item(item_name, quantity):
    if item_name in shopping_list:
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity


# 3. Default values:
def add_item(item_name, quantity=1):  # (1 require param and 1 optional param) default value=1in case quantity argument is not pass
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item("milk")
add_item("pears", 1)
print(shopping_list)


# 4. kwyword arguments:
shopping_list = {}

def show_list(include_quantities=True):
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name="", quantity=1):
    if not item_name:
        quantity = 0    # Falsy value
    if item_name in shopping_list:
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item("Bread")
add_item("Milk", 2)

print(shopping_list)

# 
supermarket_store_list = {}
hardware_store_list = {}

def add_item(item_name, quantity, shopping_list=None):
    if shopping_list is None:
        shopping_list = {}
    if not item_name:
        quantity = 0

    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

# add_item("Bread", 1, shopping_list)

supermarket_store_list = add_item("Nails", 6, supermarket_store_list)
hardware_store_list = add_item("bread", 2, hardware_store_list) 

print(show_list(hardware_store_list))
print(show_list(hardware_store_list))


# args:
shopping_list = {}
def show_list(shopping_list, include_quantities=True):  
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)    # becuause not return it will return none


def add_items(shopping_list, *item_names):
    for item_name in item_names:
        shopping_list[item_name] = 1

    return shopping_list

shopping_list = add_items(
    shopping_list, "coffe", "tea", "cake"
)

print(show_list(shopping_list)) # 1x coffe
                                # 1x tea
                                # 1x cake
                                # None

# kwards:
shopping_list = {}


def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)


def add_items(shopping_list, **things_to_buy):
    for item_name, quantity in things_to_buy.items():
        shopping_list[item_name] = quantity

    return shopping_list    


shopping_list = add_items(
    shopping_list,
    coffee=1,
    tea=2,
    cake=1,
    bread=3
)

print(show_list(shopping_list))     # 1x coffee
                                    # 2x tea
                                    # 1x cake
                                    # 3x bread
