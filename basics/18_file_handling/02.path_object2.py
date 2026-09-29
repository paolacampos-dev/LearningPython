import pathlib

# 1. Creating from a string:
# A:
# path = pathlib.Path("/mnt/c/Users/username/Desktop/text.docx")

# B:
# from pathlib import Path
# path = Path("/mnt/c/Users/username/Desktop/text.docx")  # mnt where WSL mounts Windows drives

# 2. Path.home() and Path.cwd()  when files are in the same OS:
home = pathlib.Path.home()  # or .cwd()
print(home) #if wrking in WSL2 and want to find out first the windowns path:
desk = home / "Desktop"
docs = home / "Documents"
hi_desk = docs / "text.docx"
hi_docs = desk / "text.docx"
print(hi_docs.exists()) # False
print(hi_desk.exists()) # False

# =========================================================================================================
# import subprocess
#
# username = subprocess.check_output(
#     ["cmd.exe", "/c", "echo %USERPROFILE%"], # it could be %USERNAME% instead
#     text=True
# ).strip()
# print(username) #userName ==> then construct the windows path  "/mnt/c/Users/username or userprofile"
#============================================================================================================

# Some Mthods on Path object:
path = pathlib.Path("/mnt/c/Users/userprofile/Desktop/VSC.docx")
print(path.exists())    # True
print(path.is_file())   # True
print(path.is_dir())    # False

hi_rel_path = pathlib.Path("Destopk/VSC.doc") 
print(hi_rel_path.is_absolute()) # False

# resolve completes the path from the relative given add the absolute one at the begin:
print(hi_rel_path.resolve()) # /home/paola/learning/learningPython/Destopk/VSC.doc  







