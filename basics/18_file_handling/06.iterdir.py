from pathlib import Path

notes_dir = Path.home() / "notes"
print(notes_dir.is_dir())  # True

# Iterate over the contents of a folder, will return an iterable (i can do a for loop):
print(notes_dir.iterdir()) # <generator object Path.iterdir at 0x75397c259ff0>
for path in notes_dir.iterdir():
    print(path) # /home/paola/notes/plans

readme_file = notes_dir / "README.md"
readme_file.touch()
for path in notes_dir.iterdir():
    print(path)     # /home/paola/notes/plans
                    # /home/paola/notes/README.md

print(list(notes_dir.iterdir()))   # [PosixPath('/home/paola/notes/plans'), PosixPath('/home/paola/notes/README.md')]

# .glob():
for path in notes_dir.glob("*.md"):  # needs to have a parameter = pattern (kind of a filter)
    print(path) # /home/paola/notes/README.md

print(list(notes_dir.glob("*.md"))) # [PosixPath('/home/paola/notes/README.md')]

