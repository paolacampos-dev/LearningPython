# Exercises: Level 1
# 1. Create an empty tuple
colors = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Sam', 'Charles')
sisters = ('Louise',)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Father', 'Mother')
family_members = siblings + parents

# Exercises: Level 2
# 1. Unpack siblings and parents from family_members

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'orange')
vegetables = ('carrots', 'potatoes', 'tomatoes')
animal_products = ('hamburg', 'meat balls')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_list) // 2
first_half = food_stuff_list[:middle]

# 5. Slice out the first three items and the last three items from food_stuff_lt list
food_stuff_list[:3]
food_stuff_list[-3:]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in a tuple:
'onion' in food_stuff_list



nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

