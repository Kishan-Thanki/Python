"""
File Handling and I/O in Python

This file provides a clean, professional, and complete overview of
file handling and input/output operations in Python.

Topics covered:
- open()
- Text vs binary files
- read, write, append
- with statement
- File iteration
- os and pathlib
"""

# ============================================================
# File Handling and I/O in Python
# ============================================================
#
# File handling allows programs to store data permanently,
# read external data, and interact with the filesystem.


# ============================================================
# 1. open() Function
# ============================================================
#
# open(file, mode) is used to open a file.
#
# Common modes:
# - 'r'  : read (default)
# - 'w'  : write (overwrites file)
# - 'a'  : append
# - 'x'  : create (fails if file exists)
# - 't'  : text mode (default)
# - 'b'  : binary mode

file = open("example.txt", "w")
file.write("Hello, File Handling")
file.close()


# ============================================================
# 2. Text vs Binary Files
# ============================================================
#
# Text files:
# - Handle human-readable text
# - Automatically encode/decode characters
#
# Binary files:
# - Handle raw bytes
# - Used for images, videos, executables, etc.

# Text file
with open("text_file.txt", "w") as f:
    f.write("This is a text file")

# Binary file
with open("binary_file.bin", "wb") as f:
    f.write(b"\x00\x01\x02\x03")


# ============================================================
# 3. Reading Files
# ============================================================

# read(): reads entire file
with open("text_file.txt", "r") as f:
    content = f.read()
    print(content)

# readline(): reads one line at a time
with open("text_file.txt", "r") as f:
    line = f.readline()
    print(line)

# readlines(): returns list of lines
with open("text_file.txt", "r") as f:
    lines = f.readlines()
    print(lines)


# ============================================================
# 4. Writing and Appending
# ============================================================

# Write mode (overwrites file)
with open("data.txt", "w") as f:
    f.write("First line\n")

# Append mode (adds to file)
with open("data.txt", "a") as f:
    f.write("Second line\n")


# ============================================================
# 5. with Statement (Context Manager)
# ============================================================
#
# The with statement:
# - Automatically closes files
# - Prevents resource leaks
# - Is the recommended way to handle files

with open("data.txt", "r") as f:
    print(f.read())

# No need to call f.close()


# ============================================================
# 6. File Iteration
# ============================================================
#
# Files are iterable objects.
# Python reads them line by line internally.

with open("data.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())


# ============================================================
# 7. os Module (Legacy but Still Used)
# ============================================================
#
# os provides low-level operating system interaction.

import os

# Get current working directory
print(os.getcwd())

# List files in directory
print(os.listdir("."))

# Check if file exists
print(os.path.exists("data.txt"))

# Create directory
if not os.path.exists("sample_dir"):
    os.mkdir("sample_dir")

# Remove file
# os.remove("example.txt")


# ============================================================
# 8. pathlib Module (Modern and Recommended)
# ============================================================
#
# pathlib provides an object-oriented way to work with paths.

from pathlib import Path

# Create Path object
path = Path("pathlib_example.txt")

# Write to file
path.write_text("Using pathlib for file operations")

# Read from file
print(path.read_text())

# Check existence
print(path.exists())

# Get file name and suffix
print(path.name)
print(path.suffix)

# Create directory
dir_path = Path("pathlib_dir")
dir_path.mkdir(exist_ok=True)

# Iterate over directory
for file in Path(".").iterdir():
    print(file)


# ============================================================
# 9. When to Use os vs pathlib
# ============================================================
#
# os:
# - Older
# - Procedural
# - Still used in legacy code
#
# pathlib:
# - Modern
# - Object-oriented
# - Cleaner and more readable
# - Recommended for new code


# ============================================================
# 10. Summary
# ============================================================
#
# - open() opens files with different modes
# - Text files handle strings, binary files handle bytes
# - read, write, append control file I/O
# - with statement ensures safe file handling
# - Files are iterable line by line
# - os provides system-level file operations
# - pathlib offers a modern, clean API for filesystem paths
#
# File handling is fundamental for real-world Python applications.
