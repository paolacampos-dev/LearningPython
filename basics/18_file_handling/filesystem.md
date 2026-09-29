# anatomy of a file:

- there are many type of files
- A file is a sequence of bits (8 bytes from the binary number) which encodes to a character as in UTF-8

# the file system (username or userprofile):

- Provides an abstract representation of the files stored on the computer
- Controls of the storage and retrieval of file data

- Directory Three: used to identify a file's location : File Paths:
  - root/
    - app/
    - photos/
      - fungi/
        - reishi.gif ==> to address it: root/photos/fungi/reishi.gif
      - plants/

- Different OS use different file systems = different file paths
  - Differences between Windows and UNIX systems:
    - Ubuntu Linux: /home/userName/Documents/hello.txt
    - macOS: /Users/userName/Documents/hello.txt
    - Windows: C:\Users\userName\Documents\hello.txt

- Working with file paths is python:
  - use the pathlib module: import pathlib to create path objects from the class Path that represent file path on the OS

# creating path objects (instantiating the class Path)

1. from a string:
   - Representing Windows Paths (When we are in windows) the path uses the backslash ch (`\`)
     - The backslash character (`\`) starts an escape sequence in Python.
     - To avoid those syntax errors, you can:
       1. Use a forward slash (`/`) instead:
          ```python
          pathlib.Path("C:/Users/username or userprofile/Desktop/hello.txt")
          ```
       2. Create a raw string by prefixing the string with `r`
          ```python
          pathlib.Path(r"C:\Users\userName or userprofile\Desktop\filename.txt")
          ```

2. with the Path.home() and Path.cwd() (current working directory) class methods:
   - Path.home() : Home Directory Paths
     `Path.home()` gives you different paths depending on your OS:
     - **Windows:** `C:\Users\<username>`
     - **macOS:** `/Users/<username>`
     - **Ubuntu Linux:** `/home/<username>`
   - Path.cwd() that is a dynamic reference to a directory where a process on the computer is currently working

3. with the / operator (/ exclusivaly for path and is the same as .joinpath("string"))
   - pathlib.Pat.home() / "Destop" / "text.docx"
   - pathlib.Pat.home() / "Destop/text.docx"
   - pathlib.Pat.home().joinpath("Destop").joinpath("text.docx")

# Path Attributes and methods:

**To access path components:**
| Attribute | Description | Example |
| ----------- | ------------------------------------ | ------------------------------------ |
| `.anchor` | Drive + root portion of the path | `p.anchor` → `"/"` |
| `.drive` | Drive name (mainly Windows) | `p.drive` → `"C:"` |
| `.name` | Final file or directory name | `p.name` → `"file.txt"` |
| `.parent` | Parent directory | `p.parent` → `Path("folder")` |
| `.parents` | Sequence of all parent directories | `p.parents[0]` |
| `.parts` | Individual components of the path | `p.parts` → `("folder", "file.txt")` |
| `.root` | Root portion of the path | `p.root` → `"/"` |
| `.stem` | Filename without its final extension | `p.stem` → `"file"` |
| `.suffix` | File's final extension | `p.suffix` → `".txt"` |
| `.suffixes` | List of all file extensions | `p.suffixes` → `[".tar", ".gz"]` |

- if the path points to a resource without a dot in the name, then .name and .stem return the same string, and .suffix returns an empty string

| Method           | Description                                     | Example                   |
| ---------------- | ----------------------------------------------- | ------------------------- |
| `.absolute()`    | Returns an absolute version of the path         | `p.absolute()`            |
| `.chmod()`       | Changes file/directory permissions              | `p.chmod(0o644)`          |
| `.exists()`      | Checks whether the path exists                  | `p.exists()`              |
| `.glob()`        | Finds paths matching a pattern                  | `p.glob("*.txt")`         |
| `.group()`       | Returns the group owning the file               | `p.group()`               |
| `.is_absolute()` | Checks whether the path is absolute             | `p.is_absolute()`         |
| `.is_dir()`      | Checks whether the path is a directory          | `p.is_dir()`              |
| `.is_file()`     | Checks whether the path is a file               | `p.is_file()`             |
| `.is_symlink()`  | Checks whether the path is a symbolic link      | `p.is_symlink()`          |
| `.iterdir()`     | Iterates over directory contents                | `p.iterdir()`             |
| `.joinpath()`    | Joins one or more paths                         | `p.joinpath("file.txt")`  |
| `.lstat()`       | Gets information about the path itself          | `p.lstat()`               |
| `.mkdir()`       | Creates a directory                             | `p.mkdir()`               |
| `.open()`        | Opens the file                                  | `p.open("r")`             |
| `.owner()`       | Returns the owner of the file                   | `p.owner()`               |
| `.read_bytes()`  | Reads the file as bytes                         | `p.read_bytes()`          |
| `.read_text()`   | Reads the file as text                          | `p.read_text()`           |
| `.readlink()`    | Gets the target of a symbolic link              | `p.readlink()`            |
| `.relative_to()` | Makes the path relative to another path         | `p.relative_to("folder")` |
| `.rename()`      | Renames or moves the path                       | `p.rename("new.txt")`     |
| `.replace()`     | Replaces another file/directory with this path  | `p.replace("new.txt")`    |
| `.resolve()`     | Returns an absolute, resolved path              | `p.resolve()`             |
| `.rglob()`       | Recursively finds paths matching a pattern      | `p.rglob("*.txt")`        |
| `.rmdir()`       | Removes an empty directory                      | `p.rmdir()`               |
| `.samefile()`    | Checks whether two paths refer to the same file | `p.samefile(q)`           |
| `.stat()`        | Gets file/directory information                 | `p.stat()`                |
| `.touch()`       | Creates an empty file or updates its timestamp  | `p.touch()`               |
| `.unlink()`      | Deletes a file or symbolic link                 | `p.unlink()`              |
| `.with_name()`   | Returns path with a different filename          | `p.with_name("new.txt")`  |
| `.with_stem()`   | Returns path with a different filename stem     | `p.with_stem("new")`      |
| `.with_suffix()` | Returns path with a different extension         | `p.with_suffix(".pdf")`   |
| `.write_bytes()` | Writes bytes to a file                          | `p.write_bytes(b"Hello")` |
| `.write_text()`  | Writes text to a file                           | `p.write_text("Hello")`   |

.resolve():

- creates an absolute path, resolving links (., .., custom-made symbolic links)

# Absolute and relative paths

- the whole path from the root
- just partial path from the end

# Glob patterns

# Recursive matching

# Creating Directories and Subdirectories: .mkdir()

# Creating Files: .touch()

# Iterating Over Directory Contents: .iterdir()

- the contents are always a subdirectory or a file
- A way to list all the contents of a directory with a for loop or calling a list

# Searching for Files Using .glob()

- .glob(): Returns an iterable of Path objects that match a pattern

# Understanding Common Wildcard Characters:

It applies to the same directory:
You can make them apply to a subdirectory with naming it /

1. one star: \* : any numbers of ch (we can use it as many times as we need inside the same parameter)
2. ? : a single ch
3. [abc] : one ch inside the brackets

It applies to the same directory and subdirectories: 4. two stars: \*\* or .rglob()

# Searching Recursively

# Moving Files and Directories: .replace()

# Deleting Files and Directories (which are empty):

- Delete FILES: .unlink()
  .unlink(missing_ok=True) # parameter: in case the file doesn't exist then an error will not be raise because the default value is False
- Delete FOLDERS: .rmkdir() but just works if the folder is already empty, if is is not then we need to delete the files first

# The shutil module (deleting non-empty direct):

shutil.rmtree()
