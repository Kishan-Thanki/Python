# ============================================================
# Static Methods in Python
# ============================================================

# Static methods are:
#   - Methods that belong to a class
#   - Do NOT depend on instance (self)
#   - Do NOT depend on class (cls)
#   - Used for utility or helper functionality
#
# In simple terms:
# Static methods are related to a class conceptually,
# but they do not need object or class state.

# ------------------------------------------------------------
# Defining a Static Method
# ------------------------------------------------------------

class Car:
    # Private class variable
    __total_car = 0

    def __init__(self, brand, model):
        # Instance variables
        self.__brand = brand
        self.__model = model

        # Modify class variable
        Car.__total_car += 1

    # --------------------------------------------------------
    # Static Method
    # --------------------------------------------------------
    # @staticmethod is a decorator
    # It tells Python:
    # "This method does not receive self or cls"
    @staticmethod
    def get_total_car():
        return Car.__total_car

    # Instance method
    def get_car(self):
        return f"{self.__brand} {self.__model}"


# ------------------------------------------------------------
# Creating Objects
# ------------------------------------------------------------

my_car1 = Car("BMW", "M8")
my_car2 = Car("Tesla", "Model Y")
my_car3 = Car("Porsche", "911")

# ------------------------------------------------------------
# Calling Static Method via Instance
# ------------------------------------------------------------

print(my_car1.get_total_car())   # 3
print(my_car2.get_total_car())   # 3
print(my_car3.get_total_car())   # 3

# ------------------------------------------------------------
# Calling Instance Method
# ------------------------------------------------------------

print(my_car1.get_car())         # BMW M8
print(my_car2.get_car())         # Tesla Model Y
print(my_car3.get_car())         # Porsche 911

# ------------------------------------------------------------
# Calling Static Method via Class (Recommended)
# ------------------------------------------------------------

print(Car.get_total_car())       # 3

# ------------------------------------------------------------
# Direct Access to Private Class Variable (Fails)
# ------------------------------------------------------------

# print(Car.__total_car)
# AttributeError: 'Car' object has no attribute '__total_car'

# ============================================================
# Why Car.__total_car Is Not Accessible
# ============================================================

# Python applies name mangling to private variables:
#   __total_car → _Car__total_car
#
# This prevents accidental access from outside the class.

# Technically possible (but discouraged):
print(Car._Car__total_car)       # 3

# ============================================================
# Key Characteristics of Static Methods
# ============================================================

# No access to instance variables (self)
# No access to class variables unless explicitly referenced
# Can be called using:
#   - Class name (preferred)
#   - Object reference (allowed but misleading)
# Behave like normal functions but live inside a class

# ============================================================
# Static Method vs Instance Method
# ============================================================

# Instance method:
#   def get_car(self)
#   - Requires object
#   - Can access instance + class data
#
# Static method:
#   def get_total_car()
#   - No self, no cls
#   - Can only access what you explicitly reference

# ============================================================
# Static Method vs Class Method (Preview)
# ============================================================

# Static method:
#   - No self, no cls
#   - Utility/helper logic
#
# Class method:
#   - Uses @classmethod
#   - Receives cls
#   - Used to operate on class-level data

# ============================================================
# When to Use Static Methods
# ============================================================

# Utility/helper functions related to the class
# Validation logic
# Factory helpers (sometimes)
# Grouping logic for readability

# Accessing or modifying instance state
# Heavy interaction with class variables (prefer classmethod)

# ============================================================
# Summary
# ============================================================

# - Static methods belong to the class namespace
# - They do not receive self or cls
# - They behave like normal functions
# - Use them for logic conceptually related to the class
# - Prefer calling them using the class name
# - They help keep code organized and readable
