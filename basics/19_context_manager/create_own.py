# 1. Custom CM:
class BonjourLeMonde:
    # Is it call at the begining of when CM is called:
    def __enter__(self):
        print("Entering context")
        return "Salut"

    # to close it:
    def __exit__(self, exc_type, exc_value, exc_tb): # exeptions included in the params
        if exc_tb is not None:
            print("Exception occurred in context", exc_type, exc_value, exc_tb) # debiggin

        print("Leaving context")


# 2. :
# a.- As a class:
import sys

class RedirectStdout:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.saved_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, *args):
        sys.stdout = self.saved_output

with open("...", "w")as file:
    with RedirectStdout(file):
        pass

# b. with the help of another CM:

from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()