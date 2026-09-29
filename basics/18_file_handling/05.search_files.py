from pathlib import Path

notes_dir = Path.home() / "notes"

paths = [
    notes_dir / "goals1.txt",
    notes_dir / "goals2.txt",
    notes_dir / "plans" / "goals3.txt",
    notes_dir / "plans" / "monthly" / "february.txt",
    notes_dir / "plans" / "monthly" / "march.md",
]

for path in paths:
    path.touch()

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

# 1. The wild character * filter out: =============================================================
print(list(notes_dir.glob("*.txt"))) # [PosixPath('/home/paola/notes/goals2.txt'), PosixPath('/home/paola/notes/goals1.txt')]

plans_dir = notes_dir /"plans"
print(plans_dir) # /home/paola/notes/plans

# the first parameter is where to starts...
print(list(plans_dir.glob("monthly*y*"))) # []
print(list(plans_dir.glob("monthly/*y*"))) # [PosixPath('/home/paola/notes/plans/monthly/january.md'), PosixPath('/home/paola/notes/plans/monthly/february.txt')]
print(list(plans_dir.glob("monthly/*md"))) # [PosixPath('/home/paola/notes/plans/monthly/march.md'), PosixPath('/home/paola/notes/plans/monthly/january.md')]
print(list(plans_dir.glob("monthly/*y.*"))) # [PosixPath('/home/paola/notes/plans/monthly/january.md'), PosixPath('/home/paola/notes/plans/monthly/february.txt')]

# 2. The ? Wildcard:  ===============================================================
print(list(notes_dir.glob("goals?.txt")))   # [PosixPath('/home/paola/notes/goals2.txt'), PosixPath('/home/paola/notes/goals1.txt')]
print(list(notes_dir.glob("?oals?.txt")))   # [PosixPath('/home/paola/notes/goals2.txt'), PosixPath('/home/paola/notes/goals1.txt')]
print(list(notes_dir.glob("*.??")))     # [PosixPath('/home/paola/notes/README.md')] ; the ?? is limiting it to 2 ch in this case .md


# 3. The [] Wildcard (it matches a single ch inside the []):===========================================================================================
print(list(notes_dir.glob("goals[13].txt")))    # [PosixPath('/home/paola/notes/goals1.txt')]  ; [13] for goals 1 or 3

# 4. double star pattern: ** (to look in all subdirect) or .rglob():
print(list(notes_dir.glob("**/*.txt")))     # [PosixPath('/home/paola/notes/goals2.txt'), PosixPath('/home/paola/notes/goals1.txt'), PosixPath('/home/paola/notes/plans/goals3.txt'), PosixPath('/home/paola/notes/plans/monthly/february.txt')]
print(list(notes_dir.rglob("*.md")))    # [PosixPath('/home/paola/notes/README.md'), PosixPath('/home/paola/notes/plans/monthly/march.md'), PosixPath('/home/paola/notes/plans/monthly/january.md')]