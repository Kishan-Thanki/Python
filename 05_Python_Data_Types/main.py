# ============================================
# PYTHON DATA TYPES / OBJECT TYPES
# ============================================

# In Python, **everything is an object** — even basic data types.
# Each type defines how the data behaves, how it’s stored in memory, and what operations can be performed on it.


# --------------------------------------------
# Core / Built-in Data Types
# --------------------------------------------

# 1️⃣ Numbers
# Numeric data types include integers, floating-point numbers, complex numbers, binary, Decimal, and Fraction.
# They are immutable (their value can’t be changed in place).

# Examples:
num_int = 1234                # Integer
num_float = 3.14              # Float
num_complex = 3 + 4j          # Complex number
num_binary = 0b111            # Binary literal (7 in decimal)
from decimal import Decimal
num_decimal = Decimal('10.5') # Decimal for precision arithmetic
from fractions import Fraction
num_fraction = Fraction(1, 3) # Fraction object


# 2️⃣ String
# A string is a sequence of Unicode characters — immutable and very powerful in Python.
# Different representations possible:
str_single = 'spam'
str_double = "Bob's"
str_bytes = b'a\x01c'        # Bytes literal
str_unicode = u'sp\xc4m'     # Unicode string


# 3️⃣ List []
# Ordered, mutable, and allows duplicates.
# Commonly used to store a collection of related data.

list_example = [1, [2, 'Three'], 4.5]
list_range = list(range(10))


# 4️⃣ Tuple ()
# Ordered, immutable sequences.
# Similar to lists but cannot be modified once created.

tuple_example = (1, 'spam', 4, 'U')
tuple_from_str = tuple('spam')

# Named tuples (from collections) give tuple elements names:
from collections import namedtuple
Person = namedtuple('Person', 'name age')
person = Person(name='John', age=30)


# 5️⃣ Dictionary {}
# Unordered key-value pairs (mutable, very fast lookup using keys).
dict_example = {'food': 'spam', 'taste': 'yum'}
dict_constructor = dict(hours=10, task='coding')


# 6️⃣ Set ()
# Unordered, mutable collection of unique elements.
set_example = set('abc')
set_literal = {'a', 'b', 'c'}


# 7️⃣ File
# File objects are used for reading/writing data to disk.
# They are created using the open() function.

file_read = open('eggs.txt', 'r')
file_write = open(r'C:\ham.bin', 'wb')


# 8️⃣ Boolean
# Boolean values are True or False — internally represented as 1 and 0.
flag_true = True
flag_false = False
flag_int_0 = 0
flag_int_1 = 1


# 9️⃣ None
# Represents the absence of a value — or “no value here”.
nothing = None


# 🔟 Functions
# Defined using `def` or `lambda`.
# Functions are first-class objects — meaning they can be passed as arguments, returned, or assigned to variables.

def greet(name):
    return f"Hello, {name}!"


# 1️⃣1️⃣ Modules
# A module is a file containing Python definitions and statements.
# It can be imported into other files to reuse code.

# Example: import math, os, sys


# 1️⃣2️⃣ Classes
# Classes are user-defined data structures that hold data (attributes) and behavior (methods).
# They form the foundation of Object-Oriented Programming (OOP) in Python.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        return f"{self.brand} is driving."


# ============================================
# ADVANCED TYPES / CONCEPTS
# ============================================

# 1️⃣ Decorators
# Functions that modify the behavior of other functions or methods.
# Often used for logging, authentication, and performance measurement.

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper


# 2️⃣ Generators
# Special type of iterator that yields values one at a time using `yield`.
# Useful for memory-efficient looping over large datasets.

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


# 3️⃣ Iterators
# Objects that implement the iterator protocol (`__iter__()` and `__next__()`).
# Used for sequential access to elements.

lst = [10, 20, 30]
it = iter(lst)
print(next(it))  # 10
print(next(it))  # 20


# 4️⃣ Meta Programming
# Techniques that allow modification or creation of classes/functions at runtime.
# Achieved using decorators, metaclasses, and introspection features (`getattr`, `setattr`, etc.).


# ============================================
# SUMMARY
# ============================================

# Everything in Python is an object.
# Data types define object behavior and memory representation.
# Immutable types: int, float, complex, str, tuple, frozenset, bytes
# Mutable types: list, dict, set, bytearray
# Advanced features like Decorators, Generators, and Meta Programming
# let you write more powerful and dynamic Python programs.