"""
======================================================
PYTHON INTERNALS EXPLAINED
======================================================

This file explains:
1. How __pycache__ is created
2. What __pycache__ is
3. Where the files inside __pycache__ come from
4. How Python internally executes your code
5. What Bytecode and Python Virtual Machine (PVM) are
======================================================
"""

# ----------------------------------------------------
# 1️⃣  What is __pycache__?
# ----------------------------------------------------
# The __pycache__ folder is automatically created by Python
# when you run a Python script that imports other modules.
# It stores the *compiled bytecode* of imported modules
# as `.pyc` files (Python Compiled files).
#
# Example:
# greetings.py  ->  __pycache__/greetings.cpython-313.pyc
#
# These .pyc files help Python run faster the next time,
# since it won’t need to re-parse and re-compile the same
# source file again.


# ----------------------------------------------------
# 2️⃣  Where does __pycache__ come from?
# ----------------------------------------------------
# When you execute:    python main.py
# The following happens internally:
#
# 1. The Python interpreter (the python software itself)
#    starts and reads your script.
#
# 2. The interpreter compiles your script into *Bytecode*.
#    (Intermediate representation, not machine code)
#
# 3. The Bytecode is executed by the Python Virtual Machine (PVM).
#
# 4. When imports are detected, the imported files are compiled
#    into `.pyc` bytecode and stored inside the __pycache__ folder.


# ----------------------------------------------------
# 3️⃣  Python Execution Flow
# ----------------------------------------------------
#   Script (.py)  ➜  Bytecode (.pyc)  ➜  PVM executes
#
# The Bytecode step is often hidden, but when you import modules,
# you can see the compiled bytecode files in __pycache__.
#
# Don’t confuse Python’s Bytecode with Java’s Bytecode —
# they are similar in concept (intermediate representation)
# but not identical in structure or design.


# ----------------------------------------------------
# 4️⃣  What is Bytecode?
# ----------------------------------------------------
# Bytecode is an intermediate, low-level, platform-independent code.
# It is not machine code, but a more optimized form of your source.
#
# Python “compiles” source code into bytecode — that’s why even though
# Python is called an *interpreted language*, a compilation step still exists.
#
# Once compiled, the Bytecode can be executed by any system that has
# a Python Virtual Machine (PVM). This makes Python cross-platform.
#
# Advantages:
# - Faster execution (syntax and parsing are already done)
# - Platform-independent
#
# The compiled bytecode files (.pyc) are also known as “Frozen Binaries”.


# ----------------------------------------------------
# 5️⃣  Naming Convention of .pyc Files
# ----------------------------------------------------
# Example: greetings.cpython-313.pyc
#
# Breakdown:
# - greetings          → Original module name
# - cpython            → Implementation type (standard Python)
# - 313                → Python version (3.13)
#
# Why versioned?
# Different Python versions may generate slightly different bytecodes.
# Storing version info ensures compatibility.


# ----------------------------------------------------
# 6️⃣  When are .pyc files created?
# ----------------------------------------------------
# .pyc files are only generated for *imported* modules.
#
# - If you run a single Python file (no imports), no __pycache__ appears.
# - If you have multiple files, and one imports another,
#   the imported ones are compiled and cached inside __pycache__.
#
# Reason:
#   When a file is imported multiple times, the bytecode cache helps
#   optimize loading by avoiding redundant recompilation.


# ----------------------------------------------------
# 7️⃣  Python Virtual Machine (PVM)
# ----------------------------------------------------
# The Python Virtual Machine is a small software-based engine
# that executes the bytecode line by line.
#
# Internally, the PVM runs an infinite loop that:
#   - Reads the next bytecode instruction
#   - Executes it
#   - Moves to the next instruction
#
# That’s why Python is called an *interpreted* language.
# Execution is handled line-by-line inside this runtime engine.


# ----------------------------------------------------
# 8️⃣  Run-Time Engine (PVM)
# ----------------------------------------------------
# Every programming language needs a runtime engine to execute code.
# In Python, this runtime engine is the **PVM (Python Virtual Machine)**.
#
# The PVM can execute:
#   - Source code directly (.py)
#   - Bytecode (.pyc)
#
# Hence, .pyc isn’t always created — the interpreter can directly
# execute scripts line-by-line when optimization is unnecessary.


# ----------------------------------------------------
# 9️⃣  Important Notes
# ----------------------------------------------------
# - Bytecode is NOT Machine Code.
# - It cannot be executed directly by the CPU.
# - Machine Code is the actual CPU instruction (binary level),
#   whereas Bytecode needs the PVM to interpret it.
#
# Think of Bytecode as:
#   “Halfway between Python source code and actual machine code.”


# ----------------------------------------------------
# 🔟  Quick Summary
# ----------------------------------------------------
# ✅ Python code execution flow:
#     Source Code (.py)
#          ↓
#     Bytecode (.pyc)
#          ↓
#     Python Virtual Machine (Executes)
#
# ✅ __pycache__:
#     Stores compiled .pyc bytecode for imported modules
#
# ✅ Python Virtual Machine:
#     Executes bytecode line-by-line
#
# ✅ Benefit:
#     Faster load time for modules, cross-platform compatibility
#
# ✅ Remember:
#     Bytecode is *not* machine code — it’s Python’s internal format.
# ----------------------------------------------------