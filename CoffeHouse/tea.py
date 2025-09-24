import os

# Current working directory
print(os.getcwd())

# List files in a directory
print(os.listdir("."))

# Create a folder
os.mkdir("test_folder")

# Remove a folder
os.rmdir("test_folder")

# Environment variables
print(os.environ.get("PATH"))

# Join paths safely (cross-platform)
print(os.path.join("folder", "file.txt"))

print(os.cpu_count())
print(os.name)
print(os.stat("tea.py"))
print(os.path.abspath("tea.py"))
path1=r"E:\Python code\Starter Pack\CoffeHouse"
print(f"Basename of '{path1}': {os.path.basename(path1)}")
