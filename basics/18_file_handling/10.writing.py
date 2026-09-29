# To WRITE in the file:
file = open("incremental.txt", mode="r+", encoding="utf-8")
print(file.tell())  # 0
print(file.readlines()) # ['Hello!, World!']
(file.writelines(["\n", "the 3rd line\n", "the 4th line\n", "the 5th line"]))
file.seek(0)
print(file.readlines()) # ['Hello!, World!\n', 'the 3rd line\n', 'the 4th line\n', 'the 5th line']

# We can use the print option to write in the file too:
print("This is", file=file)
print("written by print()", file=file)
file.seek(0)
print(file.read())  # Hello!, World!
                    # the 3rd line
                    # the 4th line
                    # the 5th lineThis is
                    # written by print()