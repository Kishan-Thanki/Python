# -----------------------------------------------------------
# 🍵 Python Lists
# -----------------------------------------------------------

# A List is a collection of items — numbers, strings, or even other lists.
# It’s one of the most commonly used data types in Python.
# It is created using square brackets [].

tea_varieties = ["Black", "Green", "Oolong", "White"]

# You can print the entire list using print()
print(tea_varieties)


# -----------------------------------------------------------
# 🧩 Accessing List Elements
# -----------------------------------------------------------
# Lists are 0-indexed. That means counting starts from 0.
print(tea_varieties[2])  # Access the 3rd element (Oolong)

# You can also use negative indexing to start from the end.
print(tea_varieties[-1])  # Last element


# -----------------------------------------------------------
# ✂️ Slicing (Dicing)
# -----------------------------------------------------------
# The same slicing concept we saw in strings works here too!
print(tea_varieties[1:3])   # from index 1 to 2
print(tea_varieties[0:2])   # from index 0 to 1
print(tea_varieties[2:])    # from index 2 till end
print(tea_varieties[::2])   # step = 2 (every second element)


# -----------------------------------------------------------
# 🧠 Modifying Lists
# -----------------------------------------------------------
# Lists are *mutable*, meaning you can change their contents.

print(tea_varieties[3])
tea_varieties[3] = "Herbal"
print(tea_varieties[3])

# Careful: assigning a string directly replaces range with characters!
tea_varieties[1:2] = "Lemon"
print(tea_varieties)  # See how it broke apart "Lemon" into characters?

# Reset and do it properly:
tea_varieties = ["Black", "Green", "Oolong", "White"]
tea_varieties[1:2] = ["Lemon"]  # ✅ Correct way
print(tea_varieties)

# Replace two elements with new ones
print(tea_varieties[1:3])
tea_varieties[1:3] = ["Mint", "Masala"]
print(tea_varieties)

# You can even *insert* without replacing
tea_varieties = ['Black', 'green', 'Masala', 'White']
print(tea_varieties[1:1])  # empty slice
tea_varieties[1:1] = ["test", "test"]  # inserts at position 1
print(tea_varieties)

# Remove a range by assigning an empty list
tea_varieties[1:3] = []
print(tea_varieties)


# -----------------------------------------------------------
# 🔁 Iterating and Membership Test
# -----------------------------------------------------------
for tea in tea_varieties:
    print(tea, end='\n')

print("White" in tea_varieties)

if "White" in tea_varieties:
    print("I've White Tea ☕")


# -----------------------------------------------------------
# ➕ Adding and Removing Elements
# -----------------------------------------------------------
# Append — adds item to the end of the list
tea_varieties.append("Oolong")
print(tea_varieties)

# Pop — removes the last element and returns it
print(tea_varieties.pop())
print(tea_varieties)

# Remove — deletes a specific element by value
tea_varieties.remove("green")
print(tea_varieties)

# Insert — insert element at specific index
tea_varieties.insert(1, "Green")
print(tea_varieties)


# -----------------------------------------------------------
# 🧬 Copying Lists (Reference vs Real Copy)
# -----------------------------------------------------------
tea_varieties_copy = tea_varieties
# Here both variables point to the same memory (reference copy)

# To make a *separate* copy:
tea_varieties_copy = tea_varieties.copy()
# Now they are stored separately in memory —
# changing one won’t affect the other.


# -----------------------------------------------------------
# ⚡ List Comprehensions (Generator Style)
# -----------------------------------------------------------
# This is a Pythonic way to create lists quickly.
# Example: generate a list of squares from 0 to 10

squared_nums = [x ** 2 for x in range(11)]
print(squared_nums)
