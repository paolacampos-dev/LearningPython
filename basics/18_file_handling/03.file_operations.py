from pathlib import Path

monthly_dir = Path.home() / "notes" / "plans" / "monthly"
january_path = monthly_dir / "january.md"
january_path.touch()
print(january_path.exists()) # True
print(january_path.is_file()) # True



