# ================================================================
# 🧠 Python Internal Breakdown
# ================================================================
# This file explains — in code and commentary — how Python actually
# works internally: memory allocation, references, garbage collection,
# optimizations, and the mutable vs immutable distinction.
# ================================================================


# ----------------------------------------------------------------
# ⚙️  Python's Data and Object Types
# ----------------------------------------------------------------
# Numbers       → int, float, complex, binary, Decimal, Fraction
# Strings       → str, bytes, unicode
# Lists []      → ordered, mutable collections
# Tuples ()     → ordered, immutable collections
# Dict {}       → key-value pairs
# Set ()        → unordered unique collections
# Files         → file objects (open handles)
# Boolean       → True / False (0/1)
# None          → special singleton representing "no value"
# Functions     → first-class objects, closures
# Modules       → imported namespaces
# Classes       → blueprints for custom objects
#
# Advanced types:
# Decorators, Generators, Iterators, Meta-programming objects
# ----------------------------------------------------------------


# ================================================================
# 🧩 Internal Mechanics
# ================================================================

# 🧱 1. Memory & Object Creation
print("=== 🧱 Memory & Object Creation ===")

# Everything in Python is an *object*. When you write:
score = 10
# - A new integer object `10` is created in memory.
# - The variable `score` is just a *reference* to that object.

# If another variable holds the same literal:
a_score = 10
# Python internally optimizes small integers and strings
# (called *interning*), so both may point to the same object.

print(f"score id: {id(score)}")
print(f"a_score id: {id(a_score)}")
print(f"Same object? {score is a_score}")  # Often True due to interning


# 🧹 2. Reference Counting & Garbage Collection
print("\n=== 🧹 Reference Counting & Garbage Collection ===")
import sys

x = 5
print(f"Reference count of 5: {sys.getrefcount(x)}")  # ⚠️ Not exact; includes temporary references.

# Every object keeps a "reference count".
# When the count hits zero, Python's Garbage Collector (GC)
# deallocates the object's memory.

# But optimizations exist:
# - Small integers and short strings are cached → not immediately freed.
# - So reference counts may look "fake" or confusing.

# Demonstration of reference counting
y = x  # Another reference to the same object
z = x  # Yet another reference
print(f"After adding references: {sys.getrefcount(x)}")


# 🧠 3. Variables Have No Type — Objects Do
print("\n=== 🧠 Variables Have No Type — Objects Do ===")
a = 3
print(f"a = {a}, type: {type(a)}")
# Here, the *object* 3 is of type int.
# Variable `a` has *no* inherent data type.
# Type belongs to the object in memory, not the variable name.

a = "hi and code"
print(f"a = {a}, type: {type(a)}")
# Now `a` references a different object (a string).
# The integer `3` may be freed later if no other references exist.


# 🧩 4. Immutable vs Mutable Behavior
print("\n=== 🧩 Immutable vs Mutable Behavior ===")
# Numbers and strings are *immutable* → never change in place.
# Lists and dictionaries are *mutable* → can change in place.

a = 5
print(f"Original a id: {id(a)}")
b = 2
a = a + 2  # Creates a *new* int(7) object, not mutating the old one.
print(f"After operation a id: {id(a)}")  # Different ID!
print(f"Values: a={a}, b={b}")

# 🧠 The old int(5) may be garbage collected later, not immediately.


# 📋 Lists Demonstration (Mutable)
print("\n=== 📋 Lists Demonstration (Mutable) ===")
my_list1 = [1, 2, 3]
my_list2 = my_list1
print(f"my_list1 id: {id(my_list1)}")
print(f"my_list2 id: {id(my_list2)}")
print(f"Same object? {my_list1 is my_list2}")

# Both point to the same reference.
my_list1[0] = 33
print("After modification:")
print("my_list1:", my_list1)  # [33, 2, 3]
print("my_list2:", my_list2)  # [33, 2, 3] — same object!


# 🧪 Fresh reference using slicing
print("\n=== 🧪 Fresh Reference Using Slicing ===")
h1 = [1, 2, 3]
h2 = h1[:]  # copy via slicing
print(f"h1 id: {id(h1)}, h2 id: {id(h2)}")
print(f"Same object? {h1 is h2}")

h1[0] = 55
print("After modifying h1:")
print(f"h1: {h1}, h2: {h2}")  # h1 mutated, h2 unchanged

# Copy module (shallow & deep copies)
import copy
print("\n=== Copy Module (Shallow & Deep Copies) ===")
h3 = copy.copy(h1)       # one-level copy
h4 = copy.deepcopy(h1)   # recursive copy for nested lists
print(f"Shallow copy same? {h1 is h3}")
print(f"Deep copy same? {h1 is h4}")

# Demonstrate nested list copying
nested_list = [1, [2, 3], 4]
shallow_copy = copy.copy(nested_list)
deep_copy = copy.deepcopy(nested_list)

print(f"\nOriginal nested: {nested_list}")
nested_list[1][0] = 99
print(f"After modification:")
print(f"Original: {nested_list}")
print(f"Shallow: {shallow_copy}")  # Inner list affected!
print(f"Deep: {deep_copy}")        # Completely unaffected


# 🧱 5. Identity vs Equality
print("\n=== 🧱 Identity (is) vs Equality (==) ===")
m = [1, 2, 3]
n = m
print(f"m == n: {m == n}")  # True  (values equal)
print(f"m is n: {m is n}")  # True  (same memory reference)

# If reassigned explicitly:
m = [1, 2, 3]
print("After creating new list with same values:")
print(f"m == n: {m == n}")  # True  (values equal)
print(f"m is n: {m is n}")  # False (different objects in memory)


# 🧮 6. Optimization by Python Interpreter
print("\n=== 🧮 Optimization by Python Interpreter ===")
# Python caches:
# - Small integers (-5 to 256)
# - Interned strings
# - Frequently used constants like True, False, None

a = 100
b = 100
print(f"Small integers same? {a is b}")  # True

c = 1000
d = 1000  
print(f"Large integers same? {c is d}")  # False (usually)

# String interning
s1 = "hello"
s2 = "hello"
print(f"Short strings same? {s1 is s2}")  # True

s3 = "a longer string that might not be interned"
s4 = "a longer string that might not be interned"
print(f"Long strings same? {s3 is s4}")  # False (usually)

# So reference reuse is an optimization mechanism, not a "bug".


# ================================================================
# 🔬 Advanced Examples & Edge Cases
# ================================================================

print("\n" + "="*60)
print("🔬 ADVANCED EXAMPLES & EDGE CASES")
print("="*60)

# Example 1: Integer interning range
print("\n1. Integer Interning Range:")
for i in range(-10, 260):
    a = i
    b = i
    if a is not b:
        print(f"Integer {i} is NOT interned")
        break
else:
    print("All integers from -10 to 259 are interned")

# Example 2: String behavior with different creation methods
print("\n2. String Behavior:")
str1 = "python"
str2 = "python"
str3 = "python internals"
str4 = "python internals"
print(f"Short strings same object: {str1 is str2}")
print(f"Long strings same object: {str3 is str4}")

# Example 3: List mutation effects
print("\n3. List Mutation Effects:")
original = [1, 2, 3]
reference = original
copy_list = original[:]

original.append(4)
print(f"Original: {original}")
print(f"Reference: {reference}")  # Changed!
print(f"Copy: {copy_list}")      # Unchanged

# Example 4: Function parameter passing (references)
print("\n4. Function Parameter Passing:")
def modify_list(lst):
    lst.append("modified")
    
def modify_number(num):
    num += 10
    return num

test_list = [1, 2, 3]
print(f"List before: {test_list}")
modify_list(test_list)
print(f"List after: {test_list}")  # Modified! (mutable)

test_num = 5
print(f"Number before: {test_num}")
modify_number(test_num)
print(f"Number after: {test_num}")  # Unchanged! (immutable)

# Example 5: Tuple immutability
print("\n5. Tuple Immutability:")
tuple1 = (1, 2, [3, 4])
print(f"Original tuple: {tuple1}")
tuple1[2].append(5)  # Can modify mutable elements inside tuple!
print(f"After modifying inner list: {tuple1}")

# Example 6: Dictionary behavior
print("\n6. Dictionary Behavior:")
dict1 = {'a': 1, 'b': 2}
dict2 = dict1
dict3 = dict1.copy()

dict1['a'] = 100
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")  # Changed!
print(f"dict3: {dict3}")  # Unchanged!


# ================================================================
# 🧰 Deep Dive Recap
# ================================================================
print("\n" + "="*60)
print("🧰 DEEP DIVE RECAP")
print("="*60)

recap_points = [
    "🔹 Every Python value is an object stored in memory.",
    "🔹 Variables are just names bound to object references.", 
    "🔹 Mutability determines whether in-place modification happens.",
    "🔹 Reference count controls object lifetime.",
    "🔹 Garbage collection cleans unreferenced objects.",
    "🔹 Small-object caching gives you 'same id()' illusions sometimes.",
    "🔹 Use `is` to compare identity, `==` to compare values.",
    "🔹 Slicing or `copy.copy()` creates shallow copies; `deepcopy()` creates deep ones.",
    "🔹 Type belongs to the object, not the variable.",
    "🔹 Integers -5 to 256 are interned (cached).",
    "🔹 Short strings are often interned.",
    "🔹 Function parameters are passed by object reference.",
    "🔹 Tuples are immutable but can contain mutable objects."
]

for i, point in enumerate(recap_points, 1):
    print(f"{i:2d}. {point}")


# ================================================================
# 🎯 Practical Tips & Best Practices
# ================================================================
print("\n" + "="*60)
print("🎯 PRACTICAL TIPS & BEST PRACTICES")
print("="*60)

tips = [
    "✅ Use `is` for comparing with None, True, False",
    "✅ Use `==` for comparing values of objects",
    "✅ Use slicing `[:]` or `copy()` for shallow copies of lists",
    "✅ Use `deepcopy()` for nested mutable structures", 
    "✅ Be careful when passing mutable objects to functions",
    "✅ Remember that 'immutable' tuples can contain mutable lists",
    "✅ Use `sys.getrefcount()` cautiously - results can be misleading",
    "✅ Understand that small integer/string caching is an optimization",
    "✅ Variables are references, not storage containers"
]

for i, tip in enumerate(tips, 1):
    print(f"{i:2d}. {tip}")


# ================================================================
# 🧭 Conclusion
# ================================================================
print("\n" + "="*60)
print("🧭 CONCLUSION")
print("="*60)
print("Understanding these internals makes debugging, optimization,")
print("and data-structure behavior in Python crystal clear.")
print("After this — numbers, lists, dicts all 'fly' effortlessly.")
print("\nKey Insights:")
print("• Python's 'everything is an object' model is fundamental")
print("• Reference counting + garbage collection manage memory")  
print("• Mutability determines if objects can change in-place")
print("• Optimizations (interning) explain 'surprising' behaviors")
print("• Variables are labels, objects are the actual data")
print("="*60)


# ================================================================
# 🚀 Quick Testing Area
# ================================================================

print("\n" + "="*60)
print("🚀 QUICK TESTING AREA")
print("="*60)

# Test your understanding here!
def test_your_understanding():
    print("\nTest Your Understanding:")
    
    # Question 1
    a = [1, 2, 3]
    b = a
    b[0] = 99
    print(f"Q1: a = {a}")  # What will this print?
    
    # Question 2  
    x = 100
    y = 100
    print(f"Q2: x is y = {x is y}")  # True or False?
    
    # Question 3
    list1 = [1, 2, 3]
    list2 = list1[:]
    list1.append(4)
    print(f"Q3: list2 = {list2}")  # What will this print?

test_your_understanding()

print("\n" + "="*60)
print("END OF PYTHON INTERNAL BREAKDOWN")
print("="*60)