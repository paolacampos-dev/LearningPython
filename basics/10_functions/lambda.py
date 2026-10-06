# Lambda: allows us to define a function witout using the tipical notation (functional programming)
(lambda x : x + 1)  (3) # 4
incr = (lambda x : x + 1)
print(incr(3))  # 4

lambda_funct = lambda h, w : print(h, end=' ') or print(w)
print(lambda_funct("hello", "world"))   # hello world
                                        # none

# reversing sequences:
name = "Monty Python"
print(name[::-1])   # nohtyP ytnoM

also_backwards = lambda x : x[::-1]
print(also_backwards(name)) # nohtyP ytnoM