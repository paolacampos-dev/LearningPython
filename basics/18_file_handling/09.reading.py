from pathlib import Path


# 1. We need to open the file, and for that we need to know the path where is found:
print(Path.cwd())   # /home/paola/learning/learningPython

# open("/home/username/documents/filename.txt") # first we need to open the file to the file being read it, twith its path include it
file = open("basics/18_file_handling/people-100.csv")  # means: start from my cd and then go into basics ...
file.close()
print(file.closed)  # True

# file = None
# try:
#     file = open("data.csv")
# finally:
#     if file:
#         file.close()
# the same as this code but cleanly:
# Use a Context Manager (with statment):
# with open ("basics/18_file_handling/people-100.csv") as file:
#     pass

# refactoring it as:
# path = Path("documents") / "data.csv" if it would be in a different folder

path = Path("basics/18_file_handling/people-100.csv")
with path.open(encoding="utf-8") as file:
    pass

import this

text = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# print(text)

with open("zen.txt", mode="w", encoding="utf-8") as file:
    file.write(text)
print(len(text))

with open("incremental.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello!, ")  # 7
    file.write("World!")    # 6
file = open("incremental.txt", encoding="utf-8")
print(file.read())  # Hello!, World!
print(file.read())  # NOTHING EMPTY
print(file.seek(5)) # 5
print(file.read())  # STARTS TO READ FROM THE CHR 5: !, World!
print(file.seek(0)) # 0
print(file.read(5)) # hello  (just reads the 5 first chr)
print(file.tell())  # 5
file.close()


# Working with multiple-line files:
file = open("zen.txt", encoding="utf-8")
print(file.readline())  # The Zen of Python, by Tim Peters
print(file.readline())  # shows nothing as the next line in the text
print(file.readline())  # Beautiful is better than ugly.  (next line in the text)

for line in file:
    print(line) # prints all the text

# Delete the empty lines between lines:
# A:
file.seek(0)
for line in file:
    print(line.rstrip()) # to delete the lines in between

# B:
file.seek(0)
for line in file:
    print(line, end="")

# C:
file.readlines()
file.seek(0)
print(file.readlines())
file.close()





