The file we want to import (the importer) needs to be in the same folder as the caller module (file)

Namespace is a collection of names, such as variables names, function names or class names

Every python module has its own namespace

Adjusting Import Statements

Four variations of the import statement (look at modules.py):

1. import <module> (import a namespace from the other file as funcion then in the file add the import.function()) import adder
2. import <module> as <other_name> (as a way to simplify the import name, then you used in the file)
3. from <module> import <name>
4. from <module> import <name> as <other_name>
