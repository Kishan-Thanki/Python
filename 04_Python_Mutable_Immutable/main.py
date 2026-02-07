"""
======================================================
PYTHON MUTABLE & IMMUTABLE OBJECTS EXPLAINED
======================================================

This file explains:
1. How Python handles variables, memory, and references.
2. What “mutable” and “immutable” mean in Python.
3. How Python internally manages object references.
4. How assignment, copying, and modification work in memory.
======================================================
"""

# ----------------------------------------------------
# 1️⃣  Everything in Python is an OBJECT
# ----------------------------------------------------
# In Python, every type of data — integers, strings, lists, functions, etc. —
# is represented internally as an OBJECT.
#
# Each object has:
# - An ID (its memory address)
# - A Type (data type, e.g., str, int, list)
# - A Value (actual data stored)
#
# Example:
# username = "Paul"
#
# Here, Python allocates a portion of memory to hold the string "Paul".
# The variable name `username` acts as a **reference** to that memory address.
# It does not hold the value directly — it points to the object containing that value.
#
# username → (reference) → "Paul"

username = "Paul"
print(username)   # Output: Paul


# ----------------------------------------------------
# 2️⃣  Understanding Immutability
# ----------------------------------------------------
# Strings, numbers, and tuples in Python are **immutable**.
# That means their values cannot be changed once created.
#
# Example:
# username = "Paul"
# username = "John"
#
# Here, when we reassign "John", Python doesn’t change the existing "Paul" object.
# Instead, it creates a NEW string object with the value "John",
# and updates the reference of `username` to point to that new object.

username = "Paul"
username = "John"
print(username)   # Output: John

# Internally:
# [Before]
# username ──> "Paul"
#
# [After Reassignment]
# username ──> "John"
#
# The old object "Paul" is no longer referenced and will be automatically deleted
# by Python's **Garbage Collector**.

# ✅ Note:
# Unlike C or C++, in Python you don’t have to manually free memory.
# Unreferenced objects are automatically removed.


# ----------------------------------------------------
# 3️⃣  Mutable vs Immutable in Action
# ----------------------------------------------------
# Let’s visualize this with integers.

x = 10
y = x   # y takes the same reference as x
print("Initially:", x, y)  # Output: 10 10

# Now we change x
x = 15
print("After changing x:", x, y)  # Output: 15 10

# Explanation:
# Initially:
# x ─┬─> 10
# y ─┘
#
# After x = 15:
# x ─> 15
# y ─> 10
#
# `x` now references a new object (15).
# `y` still references the old object (10).
#
# Hence, integers (like strings) are immutable — their values cannot be modified in place.


# ----------------------------------------------------
# 4️⃣  Mutable Example: Lists
# ----------------------------------------------------
# Lists, dictionaries, and sets in Python are **mutable** objects.
# Their content can be changed without changing their reference.

a = [1, 2, 3]
b = a   # Both refer to the same list object
print("Before change:", a, b)  # Output: [1, 2, 3] [1, 2, 3]

# Modify the list
a.append(4)
print("After change:", a, b)   # Output: [1, 2, 3, 4] [1, 2, 3, 4]

# Internally:
# Both a and b point to the same object in memory.
# When we modify the list, the change reflects for both,
# because they share the same memory reference.


# ----------------------------------------------------
# 5️⃣  String Immutability Example
# ----------------------------------------------------
# Strings cannot be modified in place.

s = "chai and code"

# Suppose we want to make “and” uppercase.
# We cannot change part of a string directly.
# Instead, Python creates a NEW string object.

s_new = s.replace("and", "AND")
print(s_new)  # Output: chai AND code
print(s)      # Output: chai and code

# The original string `s` remains unchanged.
# This demonstrates immutability — a new object is created instead of altering the existing one.


# ----------------------------------------------------
# 6️⃣  Why Immutability Matters
# ----------------------------------------------------
# Immutability ensures:
# - Predictable behavior
# - Safety in shared data (especially with threads)
# - Hashability (immutable objects can be used as dictionary keys or set elements)
#
# Mutability allows:
# - Efficient in-place modification (e.g., appending to lists)
# - Flexible and dynamic data structures


# ----------------------------------------------------
# 7️⃣  Garbage Collection
# ----------------------------------------------------
# In Python, unused or unreferenced objects are automatically cleaned up
# by the **Garbage Collector (GC)**.
#
# This means:
# - You don’t need to manually free memory.
# - Once no variable references an object, it becomes eligible for deletion.
#
# Example:
# username = "Paul"
# username = "John"
# Now, "Paul" is no longer referenced by any variable,
# so the GC will remove it automatically.


# ----------------------------------------------------
# 8️⃣  Summary
# ----------------------------------------------------
# 🔹 Everything in Python is an object.
# 🔹 Variables hold REFERENCES, not values.
# 🔹 Immutable objects (like str, int, tuple):
#       - Cannot be modified in place.
#       - Creating a new value creates a new object.
# 🔹 Mutable objects (like list, dict, set):
#       - Can be changed in place.
#       - Reference remains the same.
# 🔹 Python handles memory management automatically (Garbage Collection).
#
# Understanding this helps you write optimized, efficient, and bug-free code.
# ----------------------------------------------------
