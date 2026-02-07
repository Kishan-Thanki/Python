# ============================================================
# 🍵 Python Tuples
# ============================================================

# First of all — when we already have Lists, why do we need Tuples?
# Lists work great with [] brackets, so why use () parentheses?

# The answer lies in MUTABILITY.
# ------------------------------------------------------------
# A List is mutable — meaning its elements can be changed or updated.
# But sometimes we want a sequence of values that should never change.
# For that, Python gives us an immutable version of a list — called a Tuple.
# ------------------------------------------------------------

# ✅ Creating a Tuple
tea_types = ("Black", "Green", "Oolong")
print(tea_types)

# ------------------------------------------------------------
# 🎯 Accessing Tuple Elements
# ------------------------------------------------------------
# Just like lists, tuples are ordered — so indexing and slicing work the same way.

print(tea_types[0])   # First element
print(tea_types[-1])  # Last element
print(tea_types[1:])  # Slice from index 1 onward

# ------------------------------------------------------------
# ⚠️ Tuples are Immutable
# ------------------------------------------------------------
# You cannot change or reassign any element in a tuple.
# Uncommenting the below line will cause an error:
# tea_types[0] = "Lemon"  # ❌ TypeError: 'tuple' object does not support item assignment

# ------------------------------------------------------------
# 📏 Tuple Length
# ------------------------------------------------------------
print(len(tea_types))

# ------------------------------------------------------------
# ➕ Tuple Concatenation
# ------------------------------------------------------------
# You can join tuples using the + operator to form a new one.
more_teas = ("Herbal", "Earl Grey", "Herbal")
all_tea = more_teas + tea_types
print(all_tea)

# ------------------------------------------------------------
# 🎁 Tuple Unpacking
# ------------------------------------------------------------
# You can unpack tuple values directly into variables.
(black, green, oolong) = tea_types
print(black, green, oolong, sep=", ")

# ------------------------------------------------------------
# 🔍 Tuple Type Check
# ------------------------------------------------------------
print(type(tea_types))

# ------------------------------------------------------------
# 🧠 Notes:
# ------------------------------------------------------------
# ✅ Tuples are faster than lists — useful for fixed data.
# ✅ Often used for data that shouldn’t change (like coordinates, settings).
# ✅ You can also have nested tuples or mix types inside them.
