"""
======================================================
PYTHON SHELL EXPLAINED
======================================================

This file explains:
1. What the Python Shell is
2. How to activate and exit it
3. How it differs from running a Python file
4. When and why to use the Python Shell
======================================================
"""

# ----------------------------------------------------
# 1️⃣  What is the Python Shell?
# ----------------------------------------------------
# The Python Shell is an **interactive command-line interface**
# that allows you to execute Python code directly — line by line.
#
# It’s a live environment that responds immediately after you type a command.
#
# The shell is also called:
# - Python Interactive Shell
# - Python REPL (Read–Eval–Print Loop)
#
# “REPL” means:
# - READ the input
# - EVALuate it
# - PRINT the result
# - LOOP back for the next command
#
# Example:
# >>> print("Hello, World!")
# Hello, World!


# ----------------------------------------------------
# 2️⃣  How to activate the Python Shell
# ----------------------------------------------------
# To start the Python shell:
# Open your terminal or command prompt and type:
#
#     python
#
# (or sometimes `python3`, depending on your setup)
#
# Once it starts, you’ll see something like:
#
#     Python 3.13.0 (main, Oct 21 2025, 14:30:00)
#     >>> 
#
# The `>>>` is the Python prompt — it means the shell is ready to take input.


# ----------------------------------------------------
# 3️⃣  How to exit the Python Shell
# ----------------------------------------------------
# You can exit the shell in several ways:
#
# - Type:
#       exit()
#
# - Or use keyboard shortcuts:
#       CTRL + D   (on macOS/Linux)
#       CTRL + Z   (on Windows, then press ENTER)
#
# Any of these methods will close the Python shell and return to your terminal.


# ----------------------------------------------------
# 4️⃣  Difference between Python Shell and .py File
# ----------------------------------------------------
# When you write code in a file (example: main.py) and run it using:
#
#     python main.py
#
# - The code is **saved**, executed, and can be reused.
# - Output is shown after execution completes.
#
# When you write code in the **Python Shell**:
# - Code runs **immediately** after you press ENTER.
# - It is **not saved** automatically.
# - There are **no code suggestions** or IDE features.
# - Best suited for **quick tests**, not full programs.


# ----------------------------------------------------
# 5️⃣  When to Use the Python Shell
# ----------------------------------------------------
# ✅ To quickly test a small snippet or logic.
# ✅ To perform mathematical calculations.
# ✅ To debug or verify a function's behavior.
# ✅ To experiment with Python syntax or built-in modules.
#
# Example:
# >>> 5 * 9
# 45
#
# >>> import math
# >>> math.sqrt(25)
# 5.0


# ----------------------------------------------------
# 6️⃣  Importing Modules in the Shell
# ----------------------------------------------------
# You can import and explore modules directly in the shell.
#
# Example:
# >>> import datetime
# >>> datetime.datetime.now()
# datetime.datetime(2025, 10, 21, 19, 45, 00)
#
# This is useful for checking how functions behave before using them
# inside your main program or project.


# ----------------------------------------------------
# 7️⃣  When Not to Use the Python Shell
# ----------------------------------------------------
# ❌ When writing large or complex programs.
# ❌ When you need to save your work.
# ❌ When debugging multi-file projects.
#
# Instead, use a script (.py file) and an IDE or code editor.
#
# The Python shell is mainly for **interactive exploration and testing**.


# ----------------------------------------------------
# 🔟  Summary
# ----------------------------------------------------
# ✅ Command to start:   python
# ✅ Command to exit:    exit() or CTRL + D / CTRL + Z
# ✅ Purpose:            Quick code testing, debugging, and learning
# ✅ Limitation:         Code is not saved automatically
# ✅ Best for:           Small snippets, experiments, or quick checks
# ----------------------------------------------------
