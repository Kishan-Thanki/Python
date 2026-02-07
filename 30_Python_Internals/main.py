"""
Python Internals (Advanced)

This file provides a clean, professional, and conceptual overview of
Python internals. These topics explain how Python works under the hood
and are essential for advanced developers, performance tuning,
debugging, and system-level understanding.

Topics covered:
- CPython architecture
- Bytecode
- GIL internals
- Import system
- Memory model

This file is explanatory by design. Some sections include illustrative
examples rather than production code.
"""

# ============================================================
# Python Internals (Advanced)
# ============================================================
#
# Python internals describe how Python executes code, manages memory,
# handles concurrency, and loads modules.
#
# Unless specified otherwise, "Python" here refers to CPython,
# the reference implementation of Python.


# ============================================================
# 1. CPython Architecture
# ============================================================
#
# CPython is the default and most widely used Python implementation.
# It is written in C and executes Python source code in several stages.
#
# High-level execution flow:
#
#   Python source (.py)
#        ↓
#   Parsing (AST generation)
#        ↓
#   Compilation
#        ↓
#   Bytecode (.pyc)
#        ↓
#   Python Virtual Machine (PVM)
#
# Key CPython components:
# - Parser: Converts source code into an Abstract Syntax Tree (AST)
# - Compiler: Converts AST into bytecode
# - Python Virtual Machine: Executes bytecode
# - Memory Manager: Manages objects and garbage collection
#
# CPython is optimized for simplicity and correctness,
# not raw multi-threaded performance.


# ============================================================
# 2. Bytecode
# ============================================================
#
# Python code is compiled into bytecode, which is a low-level,
# platform-independent instruction set.
#
# Bytecode is executed by the Python Virtual Machine (PVM).
#
# Bytecode files:
# - Stored as .pyc files
# - Usually located in __pycache__ directory
# - Automatically generated and managed by Python

def add(a, b):
    return a + b

# Inspect bytecode using the dis module
import dis
dis.dis(add)

# Important notes:
# - Bytecode is not machine code
# - Bytecode changes between Python versions
# - Bytecode execution is interpreted, not JIT-compiled (in CPython)


# ============================================================
# 3. Global Interpreter Lock (GIL) Internals
# ============================================================
#
# The Global Interpreter Lock (GIL) ensures that only one thread
# executes Python bytecode at a time in CPython.
#
# Why the GIL exists:
# - Simplifies memory management
# - Makes reference counting thread-safe
# - Reduces interpreter complexity
#
# Consequences:
# - CPU-bound multithreaded programs do not scale well
# - I/O-bound threads work efficiently
#
# The GIL is:
# - A mutex (lock)
# - Released during blocking I/O
# - Switched periodically between threads

import threading

def task():
    for _ in range(10**6):
        pass

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

# This does not run in parallel on multiple CPU cores for CPU-bound work.

# Alternatives to bypass GIL limitations:
# - multiprocessing
# - asyncio
# - Native extensions written in C
# - Other Python implementations (PyPy, Jython)


# ============================================================
# 4. Import System
# ============================================================
#
# Python’s import system is responsible for loading modules and packages.
#
# Import process:
# 1. Check sys.modules (cache)
# 2. Search built-in modules
# 3. Search directories in sys.path
# 4. Load module
# 5. Execute module code
# 6. Cache module in sys.modules

import sys

print(sys.path)
print("math" in sys.modules)

import math

print("math" in sys.modules)

# Key concepts:
# - Modules are executed only once
# - Subsequent imports reuse cached module
# - Circular imports can cause runtime issues
#
# Special variables:
# - __name__
# - __file__
# - __package__


# ============================================================
# 5. Python Memory Model
# ============================================================
#
# Python manages memory automatically using:
# - Reference counting
# - Garbage collection
#
# Every object in Python:
# - Has an identity (id)
# - Has a type
# - Has a reference count

a = []
b = a

print(id(a), id(b))  # Same object reference

# Reference counting:
# - Object is deallocated when reference count reaches zero
#
# Garbage collection:
# - Handles reference cycles
# - Implemented via the gc module

import gc

print(gc.get_threshold())
print(gc.get_count())

# Memory optimizations:
# - Small integer caching
# - String interning
# - Object reuse


# ============================================================
# 6. Object Model Internals
# ============================================================
#
# Python objects are implemented as C structures.
# Each object contains:
# - Reference count
# - Type pointer
# - Object-specific data
#
# Attribute storage:
# - Instance attributes stored in __dict__
# - __slots__ can reduce memory usage

class Example:
    def __init__(self, x):
        self.x = x

obj = Example(10)
print(obj.__dict__)


# ============================================================
# 7. Why Python Internals Matter
# ============================================================
#
# Understanding internals helps with:
# - Writing performant code
# - Debugging complex issues
# - Choosing correct concurrency models
# - Designing scalable systems
# - Reading CPython source code
#
# Python internals knowledge separates
# Python users from Python engineers.


# ============================================================
# 8. Summary
# ============================================================
#
# - CPython compiles source code into bytecode
# - Bytecode runs on the Python Virtual Machine
# - GIL enforces single-threaded bytecode execution
# - Import system caches and executes modules
# - Memory is managed via reference counting and GC
# - Object model defines how everything behaves internally
#
# Mastery of Python internals enables advanced-level development.
