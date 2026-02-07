# ============================================================
# 🧠 Python Dictionaries
# ============================================================

# When we studied lists, we focused on the order of elements.
# In a list, order matters — we access values using their index positions (0, 1, 2...).
# Example: items[0] gives the first element.

# But what if the *order* doesn’t matter, and instead we care about
# mapping a specific key to a specific value?

# That’s where dictionaries come in!
# Dictionaries store data as **key–value pairs**.
# Each key is unique and acts like an identifier for its value.

# ------------------------------------------------------------
# ✅ Creating a Dictionary
# ------------------------------------------------------------

# You can create an empty dictionary like this:
# chai_types = dict()
# or simply:
# chai_types = {}

# Let's create one with some values.
chai_types = {
    "Masala": "Spicy",
    "Ginger": "Zesty",
    "Green": "Mild"
}

print(chai_types)

# ------------------------------------------------------------
# 🎯 Accessing Values
# ------------------------------------------------------------

# You can access a value by its key — similar to how you use indices in a list.
print(chai_types["Masala"])

# But if you try to access a key that doesn't exist, it will raise a KeyError:
# print(chai_types["Masalaa"])  # ❌ KeyError

# To avoid that, use the `.get()` method:
print(chai_types.get("Masala"))   # ✅ Safe access
print(chai_types.get("Masalaa"))  # ✅ Returns None (no error)

# ------------------------------------------------------------
# 📝 Modifying Values
# ------------------------------------------------------------

chai_types["Green"] = "Fresh"  # Update an existing key
print(chai_types)

# ------------------------------------------------------------
# 🔁 Iterating through Dictionaries
# ------------------------------------------------------------

# You can loop through keys:
for key in chai_types:
    print(key, chai_types[key], sep=': ')

# Or loop through both keys and values together:
for key, value in chai_types.items():
    print(f"{key}: {value}")

# ------------------------------------------------------------
# 🔍 Checking Keys and Length
# ------------------------------------------------------------

if "Masala" in chai_types:
    print(chai_types["Masala"])

print("Total items:", len(chai_types))

# ------------------------------------------------------------
# ➕ Adding New Items
# ------------------------------------------------------------

chai_types["Earl Grey"] = "Citrus"
print(chai_types)

# ------------------------------------------------------------
# ❌ Removing Items
# ------------------------------------------------------------

# pop() removes a specific key and returns its value
print(chai_types.pop("Ginger"))
print(chai_types)

# popitem() removes the last inserted item
print(chai_types.popitem())
print(chai_types)

# del keyword deletes a key (and its value) entirely
del chai_types["Masala"]
print(chai_types)

# ------------------------------------------------------------
# 📋 Copying Dictionaries
# ------------------------------------------------------------

chai_types_copy = chai_types.copy()
chai_types.popitem()  # remove last item to check difference
print("Original:", chai_types)
print("Copy:", chai_types_copy)

# ------------------------------------------------------------
# 🧩 Nested Dictionaries
# ------------------------------------------------------------

# You can store dictionaries inside dictionaries (nested structure)
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "tea": {"Green": "Mild", "Black": "Strong"}
}

print(tea_shop)
print(tea_shop["chai"])           # Access nested dictionary
print(tea_shop["chai"]["Masala"]) # Access nested value

# ------------------------------------------------------------
# 🧮 Dictionary Comprehension
# ------------------------------------------------------------

# Create a dictionary with keys and computed values
squared_nums = {x: x ** 2 for x in range(6)}
print(squared_nums)

# ------------------------------------------------------------
# 🧹 Clearing All Items
# ------------------------------------------------------------

squared_nums.clear()
print(squared_nums)

# ------------------------------------------------------------
# 🪄 Using fromkeys()
# ------------------------------------------------------------

# If you have a list of keys and want to assign them all the same value:
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
