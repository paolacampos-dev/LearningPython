# function calling and references:
def say_hello():
    print("Hello!")
say_hello() # Hello!
print(say_hello)    # <function say_hello at 0x79dd4f133d80>

print(print)    # <built-in function print>


# Function references as arguments:
print("You!")   # You!
print("You!", "here", 1)    # You! here 1
print("You!", say_hello)    # You! <function say_hello at 0x73add802ff60>
print("You", print) # You <built-in function print>

print(dir(say_hello))   # ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__']

say_hello.language = "en"
print(say_hello.language)   # en
print(dir(say_hello))   # ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__', 'language']


# Calling function references:
def inside():
    print("This is inside")

def outside(fn):
    print ("This is outside")
    fn()

print(outside(inside))  # This is outside
                        # This is inside
                        # None

# Functions as arguments in stdlib:
animals = ["ferret", "vole", "dog", "gecko"]
sorted(animals) # ferret 6
                # vole 4
                # dog 3
                # gecko 5
for animal in animals:
    print(animal, len(animal))  
sorted(animals, key=len)    # ['gecko', 'dog', 'vole', 'ferret']

# Sorting backwards strings:
print(animals[::-1])

def backwards(name):
    return name[::-1]

print(backwards(animals[1]))    # elov

banimals = []
for animals in animals:
    banimals.append(backwards(animal))

print(banimals) # ['okceg', 'okceg', 'okceg', 'okceg']
print(sorted(animals, key=backwards))   # ['c', 'e', 'g', 'k', 'o']


# Lambda:
also_backwards = lambda x : x[::-1] # ['c', 'e', 'g', 'k', 'o']
print(also_backwards(animals[0]))   # g
print(sorted(animals, key=also_backwards))  #  ['c', 'e', 'g', 'k', 'o']
print(sorted(animals, key=lambda x : x[::-1]))  # ['c', 'e', 'g', 'k', 'o']
print(sorted(animals, key=lambda x : -len(x)))  # ['g', 'e', 'c', 'k', 'o']
print((lambda x : x[::-1])("Monthy"))  # yhtnoM

print((lambda x, y: (x * y) + x)(3, 4)) # 15

print((lambda x: "even" if x % 2 == 0 else "odd")(2))   # even

print((lambda x: (x, x + 1))(5))     # (5, 6)

