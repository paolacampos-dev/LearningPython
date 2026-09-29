from pathlib import Path

#     notes/
# ├── plans/
# │   ├── monthly/
# │   │   ├── february.txt
# │   │   ├── january.md
# │   │   └── march.md
# │   ├── weekly/
# │   └── goals3.txt
# ├── README.md
# ├── goals1.txt
# └── goals2.txt


# Move FILES:
notes_dir = Path.home() / "notes"
old_path_goals_3 = notes_dir / "plans" / "goals3.txt"
print(old_path_goals_3)  # /home/paola/notes/plans/goals3.txt

new_path_goals_3 = notes_dir / "goals3.txt"
old_path_goals_3.replace(new_path_goals_3)
print(new_path_goals_3) # /home/paola/notes/goals3.txt
print(list(notes_dir.iterdir())) # [PosixPath('/home/paola/notes/goals2.txt'), PosixPath('/home/paola/notes/goals1.txt'), PosixPath('/home/paola/notes/plans'), PosixPath('/home/paola/notes/README.md'), PosixPath('/home/paola/notes/goals3.txt')]
print(list((notes_dir / "plans").iterdir())) # [PosixPath('/home/paola/notes/plans/monthly'), PosixPath('/home/paola/notes/plans/weekly')]


# Move FOLDERS:
source = notes_dir / "where it lives"
destination = notes_dir / "where it goes - folder" / "where it goes - folder" 
source.replace(destination)

