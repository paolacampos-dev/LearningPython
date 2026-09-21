class MyContext:

    def __enter__(self):
        print("Starting")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Finishing")


with MyContext():
    print("Doing something")