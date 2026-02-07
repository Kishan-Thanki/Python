# ============================================================
# 🧠 Class Methods and `self` in Python
# ============================================================

# Till now, we learned:
#   - What a class is
#   - How objects are created
#   - How __init__ initializes object data
#
# Now let’s understand:
#   👉 How objects BEHAVE
#   👉 What `self` actually means
#   👉 How methods work inside a class

# ------------------------------------------------------------
# 🚗 Class with Attributes
# ------------------------------------------------------------
class Car:
    def __init__(self, brand, model):
        # These are instance attributes
        self.brand = brand
        self.model = model

    # --------------------------------------------------------
    # ⚙️ Class Method (Custom Behavior)
    # --------------------------------------------------------
    # This is a NORMAL method (not special like __init__)
    # It defines what an object can DO
    #
    # `self` is mandatory here
    # It represents the CURRENT object calling this method

    def full_name(self):
        # Using self to access object data
        return f"{self.brand} {self.model}"

# ------------------------------------------------------------
# 🧍 Creating an Object
# ------------------------------------------------------------
my_car = Car("BMW", "M8")

# ------------------------------------------------------------
# 📞 Calling a Method using Object
# ------------------------------------------------------------
# We call methods using dot notation
print(my_car.full_name())   # BMW M8

# ------------------------------------------------------------
# 🧠 What is `self` REALLY?
# ------------------------------------------------------------
# When you write:
#   my_car.full_name()
#
# Python internally converts it to:
#   Car.full_name(my_car)
#
# So `self` === my_car
#
# That’s why:
#   self.brand  → my_car.brand
#   self.model  → my_car.model

# ------------------------------------------------------------
# ❓ Why is `self` Needed?
# ------------------------------------------------------------
# Because the SAME method works for MANY objects

my_car2 = Car("Porsche", "911")

print(my_car2.full_name())  # Porsche 911

# Internally:
#   Car.full_name(my_car2)
#
# Same method
# Different object
# Different data

# ------------------------------------------------------------
# 🚨 Important Rules About `self`
# ------------------------------------------------------------
# ✅ `self` is NOT a keyword (just a convention)
# ❌ But NEVER rename it (don’t confuse others)
# ✅ It must be the FIRST parameter of instance methods
# ❌ You don’t pass it manually — Python does it for you

# ------------------------------------------------------------
# 🧩 Mental Model
# ------------------------------------------------------------
# Method → Common behavior
# self   → Which object is using that behavior
#
# Think:
#   "This object is calling this method"

# ------------------------------------------------------------
# 🧾 Summary
# ------------------------------------------------------------
# Methods define object behavior
# `self` refers to the current object
# Methods access data using `self`
# Same method works for multiple objects
# Python passes `self` automatically
