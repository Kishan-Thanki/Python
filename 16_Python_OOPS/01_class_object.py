# ============================================================
# 🚗 Python Classes and Objects (Step-by-Step)
# ============================================================

# In Python:
#   - We use `def` to define FUNCTIONS
#   - We use `class` to define CLASSES
#
# A class is like a blueprint.
# An object is the real thing created from that blueprint.

# ------------------------------------------------------------
# 🧠 What is a Class?
# ------------------------------------------------------------
# A class defines:
#   👉 What an object SHOULD have (attributes)
#   👉 What an object CAN do (methods)

# Naming convention:
# ✅ Class names use PascalCase
# ❌ Avoid lowercase or snake_case for class names

# ------------------------------------------------------------
# 🏗️ Defining an Empty Class
# ------------------------------------------------------------
class Car:
    pass

# Explanation:
# - `pass` means "do nothing for now"
# - This class has no attributes or methods yet
# - But it is still a valid class

# ------------------------------------------------------------
# 🧱 Class Attributes (Variables inside a Class)
# ------------------------------------------------------------
# Classes can have attributes (variables)
# These act as a structure / template

class Car:
    # These are class attributes
    # Initially set to None (no value)
    brand = None
    model = None

# ------------------------------------------------------------
# 🧍 Creating an Object (Instance of a Class)
# ------------------------------------------------------------
# To create an object, we CALL the class like a function

Car()   # This creates a new Car object

# Usually, we store it in a variable
my_car = Car()

# Let’s print the object
print(my_car)

# Output looks like:
# <__main__.Car object at 0x10470b250>

# Explanation:
# - This is NOT an error
# - Python is showing:
#     - Module name (__main__)
#     - Class name (Car)
#     - Memory address (0x10470b250)

# ------------------------------------------------------------
# ❓ How Do We Assign Values to Attributes?
# ------------------------------------------------------------
# Manually setting attributes every time is messy.
# Instead, we use a special method called __init__()

# ------------------------------------------------------------
# ⚙️ __init__ Method (Constructor)
# ------------------------------------------------------------
class Car:
    # __init__ is a special method
    # It runs AUTOMATICALLY when an object is created
    #
    # Purpose:
    #   👉 Initialize (set up) the initial state of the object

    def __init__(self, brand: str, model: str):
        # `self` refers to the CURRENT object
        # Each object gets its own copy of these values

        self.brand = brand
        self.model = model

# ------------------------------------------------------------
# 🚀 Creating Objects with Data
# ------------------------------------------------------------
my_car = Car("BMW", "M8")

# Access object attributes using dot notation
print(my_car.brand)   # BMW
print(my_car.model)   # M8

# Think of it like:
#   my_car.brand
# is actually:
#   <Car object at 0x10470b250>.brand

# ------------------------------------------------------------
# 🔁 Creating Multiple Objects from Same Class
# ------------------------------------------------------------
my_car2 = Car("Porsche", "911")

print(my_car2)
print(my_car2.brand)   # Porsche
print(my_car2.model)   # 911

# Internally, it looks like:
#   <Car object at 0x1001d7250>.brand

# Each object:
# ✅ Has its own memory address
# ✅ Has its own values
# ❌ Does NOT share data with other objects

# ------------------------------------------------------------
# 🧩 Mental Model
# ------------------------------------------------------------
# Class  → Blueprint
# Object → Real car built from that blueprint
#
# One class → Many objects
# Same structure → Different data

# ------------------------------------------------------------
# 🧾 Summary
# ------------------------------------------------------------
# class keyword defines a class
# Objects are created by calling the class
# __init__ initializes object data
# self refers to the current object
# Dot notation accesses object attributes
# Each object has its own memory and state
