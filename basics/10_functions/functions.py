# side effects funcion:
print("hello") # hello
return_value = print("hello")
return_value

# prints returns a value called none
type(print) # nonetype

def shout_and_return(input_string):
    loud_input = input_string.upper()
    print(loud_input)
    return loud_input

shout_and_return("hello")   # HELLO   (print value)  side effect
                            # 'HELLO'  (return value)

my_return = shout_and_return("hi") # HI   side effect of the print function
my_return # 'HI'


# Scope LEGB:====================================================================
counter = 0
def update_counter():
    global counter          # needs to be added to be able to use the global counter
    counter = counter + 1
    print(counter)

update_counter()


# Refactoring:
counter = 0
def update_counter(current_counter):
    return current_counter +1

counter = update_counter(counter)
print(counter)
