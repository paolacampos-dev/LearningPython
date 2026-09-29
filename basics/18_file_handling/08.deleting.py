from pathlib import Path

# Deleting a FILE:
notes_dir = Path.home() / "notes"
file_path = notes_dir / "plans" / "monthly" / "march.md"
file_path.unlink(missing_ok=True)  # parameter: in case the file doesn't exist then an error will not be raise because the default value is False
print(file_path.exists())  # False

# Deleting a FOLDER:
weekly_dir = notes_dir / "plans" / "weekly"
weekly_dir.rmdir()  # just works if the folder (directory) is empty (if there are files or folders then first delete them)
print(weekly_dir.exists()) # False

# Deleting a non-empty folder - deleting all ist contents:
yearly_dir = notes_dir / "plans" / "yearly"
import shutil       # module
shutil.rmtree(yearly_dir)

