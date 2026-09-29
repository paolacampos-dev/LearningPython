# import adder

# value = adder.add(2, 4)
# print(value) # 6

# double_value = adder.double(value)
# print(double_value) # 12

#==================================================
# import adder as a

# value = a.add(2, 4)
# print(value) # 6

# double_value = a.double(value)
# print(double_value) # 12


#========================================================
# from adder import add, double

# value = add(2, 4)
# print(value) # 6

# double_value = double(value)
# print(double_value) # 12

#======================================================
from adder import add as a, double as d

value = a(2, 4)
print(value) # 6

double_value = d(value)
print(double_value) # 12