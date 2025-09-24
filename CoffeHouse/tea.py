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