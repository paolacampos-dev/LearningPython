import pathlib

# 1. Create a path object trough a string:
p = pathlib.Path("/home/paola/notes")
print(p) # return a path object /home/paola/notes

# 2. Path.home() and Path.cwd()  when files are in the same OS:
p = pathlib.Path.home()
print(p) # /home/paola

p = pathlib.Path.cwd()
print(p) # /home/paola/learning/learningPython

# 3. using the / operator:
p = pathlib.Path.home() / "notes"
print(p) # /home/paola/notes


