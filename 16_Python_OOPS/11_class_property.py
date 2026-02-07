# ============================================================
# Class Property (@property) in Python
# ============================================================

# Properties are:
#   - A way to access private attributes like public attributes
#   - Used to enforce encapsulation with controlled access
#   - Implemented using decorators
#
# In simple terms:
# Properties let you READ / WRITE data using attribute syntax,
# while still controlling the logic internally.

# ------------------------------------------------------------
# Why Properties Exist
# ------------------------------------------------------------

# Direct access to private attributes is not allowed
# Properties provide safe, controlled access
# They look like attributes, but behave like methods

# ============================================================
# Class with Property
# ============================================================

class Car:
    __total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand       # private instance variable
        self.__model = model       # private instance variable
        Car.__total_car += 1

    # --------------------------------------------------------
    # Static Method (already covered)
    # --------------------------------------------------------
    @staticmethod
    def get_total_car():
        return Car.__total_car

    # --------------------------------------------------------
    # Property (Getter)
    # --------------------------------------------------------
    @property
    def model(self):
        return self.__model

    # --------------------------------------------------------
    # Property Setter
    # --------------------------------------------------------
    @model.setter
    def model(self, value):
        # Validation logic can be added here
        if not value:
            raise ValueError("Model name cannot be empty")
        self.__model = value

    # Instance method
    def get_car(self):
        return f"{self.__brand} {self.__model}"


# ============================================================
# Creating Object
# ============================================================

my_car = Car("BMW", "M8")

# ============================================================
# Invalid Direct Access (Fails)
# ============================================================

# print(my_car.__brand)
# AttributeError: 'Car' object has no attribute '__brand'

# print(my_car.__model)
# AttributeError: 'Car' object has no attribute '__model'

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# Private attributes use name mangling:
#   __brand → _Car__brand
#   __model → _Car__model
#
# Direct access is intentionally blocked.

# ============================================================
# Correct Access
# ============================================================

print(my_car.get_car())    # BMW M8
print(my_car.model)        # M8  (property getter)

# ============================================================
# Incorrect Assignment (Creates a NEW attribute!)
# ============================================================

my_car.__model = "M7"

print(my_car.model)       # Still M8

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# This does NOT modify the private variable.
# It creates a new attribute:
#   my_car.__model
#
# This is a common beginner pitfall.

# ============================================================
# Correct Assignment Using Property
# ============================================================

my_car.model = "M7"        # Calls @model.setter
print(my_car.model)        # M7

# ============================================================
# Internal State Check (Educational)
# ============================================================

print(my_car.__dict__)

# Example output:
# {
#   '_Car__brand': 'BMW',
#   '_Car__model': 'M7',
#   '__model': 'M7'   <-- shadowed attribute (bad practice)
# }

# ============================================================
# Key Characteristics of @property
# ============================================================

# Accessed like an attribute
# Backed by methods (getter/setter)
# Preserves encapsulation
# Allows validation & transformation
# No breaking change for API users

# ============================================================
# Property vs Getter Method
# ============================================================

# Getter method:
#   get_model()
#   - Explicit method call
#
# Property:
#   obj.model
#   - Cleaner syntax
#   - More Pythonic
#   - Preferred in modern Python

# ============================================================
# When to Use Properties
# ============================================================

# When accessing private attributes
# When validation is required
# When logic may change in future
# When you want attribute-style access

# When simple public attributes are enough

# ============================================================
# Summary
# ============================================================

# - @property provides controlled access to private data
# - Private attributes cannot be accessed directly
# - Property setters allow validation and safety
# - Assigning to __attr creates a new attribute (pitfall!)
# - Properties are the Pythonic way to enforce encapsulation
