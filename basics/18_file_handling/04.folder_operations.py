from pathlib import Path  # Path is the class we import to instantiate the object

# Folder (mkdir):

# 1. Create: 
notes_dir = Path.home() / "notes"
# notes_dir.exists() # False

# Because it doesnt exist, then create one:
# notes_dir.mkdir()
# print(notes_dir.exists()) # True
# print(notes_dir) # /home/paola/notes

# Once is create it if we call it again notes_dir.mkdir() it will give an error, therefore to skip the error:
notes_dir.mkdir(exist_ok=True)
# the same as saying:
if not notes_dir.exists():
    notes_dir.mkdir()


# 2. Create a subdirectory:
monthly_dir = notes_dir / "plans" / "monthly"  # Just builds the path no creates anything
print(monthly_dir) # /home/paola/notes/plans/monthly
# monthly_dir.mkdir()  # FileNotFoundError: [Errno 2] No such file or directory: '/home/paola/notes/plans/monthly'
# to solve it, create all the missing parent directory:
# monthly_dir.mkdir(parents=True)
print(monthly_dir.exists()) # True

weekly_dir = notes_dir / "plans" / "weekly"
weekly_dir.mkdir(parents=True, exist_ok=True)
print(weekly_dir) # /home/paola/notes/plans/weekly
print(weekly_dir.exists()) # True


