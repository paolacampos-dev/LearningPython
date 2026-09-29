# strings:
# str can be between "" or ''
print ("hello world") 
print ('hello world') 

hello = "Hello 'baby!'"
print(hello)    # Hello 'baby!'

my_name = "I'm Paola"
print(my_name)  # I'm Paola

# also we can use \' instead
your_name = 'You\'re Tom'
print(your_name)    # You're Tom

# scape character \ can be use:
# To jump a line at the end \n:
x = "This is line 1.\nThis is line 2."
print(x)    # This is line 1.
            # This is line 2.

# To add tabs:
z = "One\tTwo\tThree"
print(z)    # One     Two     Three

#raw str:
zr = r"One\tTwo\tThree"
print(zr)    # One\tTwo\tThree


# in py we dont need ; (that is a  single line comment )
"""
this is a  comment
in multiple lines
"""

'''
also 
a multiple lines
comment
'''

# interger, float and complex number 
# boolean: true or false

#consultar el tipo de dato:
print(type("hello python")) # <class 'str'>
print(type(5)) # <class 'int'>
print(type(5.5)) # <class 'float'>
print(type([1, 2,  3])) # <class 'list'>
print(type({9.8, 3.14, 5.5})) # <class 'set'>
print(type((5.5, 3.14, 2.7))) # <class 'tuple'>
print(type({'name':'Paola'})) # <class 'Dictionary'>



# Intergers:
# Find a bynary number:
c = 0b100100111
print(c) # 295 in decimal

# Find an Octal:
d = 0o454312    
print(d)    # 153802

# findind x for decimal:
e = 0xac4d
print(e)    # 44109


f = 500
print(bin(f))   # 0b111110100
print(oct(f))   # 0o764
print(hex(f))   # 0x1f4


# Floats:

# Scientif notation XeX:
j = 4e3
print(j)    # 4000.0

k = 4e-3
print(k)    # 0.004


# Be aware of the error, when working in finance or maths operations related:
a = 0.2
b = 0.1
c = a + b
print(c)    # 0.30000000000000004



# Complex number (ax + bj):
m = 2+3j
print(m)    # (2+3j)
print(type(m))  # <class 'complex'>

