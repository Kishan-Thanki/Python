# ============================================================
# Encapsulation in Python
# ============================================================

# Encapsulation refers to:
#   - Hiding internal data
#   - Controlling how data is accessed
#   - Protecting object state from accidental misuse
#
# In simple terms:
# Internal attributes should not be accessed directly.
# Interaction should happen through well-defined methods.

# ------------------------------------------------------------
# Class with Private and Protected Attributes
# ------------------------------------------------------------
class Car:
    def __init__(self, brand, model):
        # Private attributes (double underscore)
        self.__brand = brand
        self.__model = model

        # Protected attribute (single underscore)
        self._engine_status = "OFF"

    # --------------------------------------------------------
    # Getter Method for Private Attribute
    # --------------------------------------------------------
    # Getter methods provide controlled read access
    # Naming convention: get_<attribute_name>
    def get_brand(self):
        return self.__brand

    # --------------------------------------------------------
    # Method Using Protected Attribute
    # --------------------------------------------------------
    def start_engine(self):
        self._engine_status = "ON"
        print("Engine started")

    def full_name(self):
        return f"{self.__brand} {self.__model}"

# ------------------------------------------------------------
# Creating an Object
# ------------------------------------------------------------
my_car = Car("BMW", "M8")

# ------------------------------------------------------------
# Direct Access to Private Attributes (Fails)
# ------------------------------------------------------------
# The following lines raise AttributeError
#
# print(my_car.__brand)
# print(my_car.__model)

# Private attributes are not accessible outside the class.

# ------------------------------------------------------------
# Accessing Protected Attribute (Possible but Discouraged)
# ------------------------------------------------------------
print(my_car._engine_status)  # OFF

# This works, but accessing protected attributes outside the class
# violates encapsulation conventions.

# ------------------------------------------------------------
# Correct Access Using Methods
# ------------------------------------------------------------
print(my_car.get_brand())    # BMW
my_car.start_engine()
print(my_car._engine_status) # ON (still discouraged externally)

# ------------------------------------------------------------
# Private Attributes and Name Mangling
# ------------------------------------------------------------
# Python applies name mangling to private attributes:
#   __brand becomes _Car__brand
#
# This access is technically possible but should be avoided.
print(my_car._Car__brand)    # BMW

# ------------------------------------------------------------
# Encapsulation with Inheritance
# ------------------------------------------------------------
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def show_details(self):
        # Private attributes from parent class are NOT accessible
        #
        # print(self.__brand)  -> AttributeError

        # Protected attributes ARE accessible in child classes
        print(self._engine_status)

# ------------------------------------------------------------
# Inheritance Behavior Check
# ------------------------------------------------------------
ecar = ElectricCar("Tesla", "Model S", "100kWh")

# print(ecar.__brand)       -> AttributeError
# print(ecar._Car__brand)   -> Works but breaks encapsulation

ecar.start_engine()
ecar.show_details()         # ON

# ------------------------------------------------------------
# Public vs Protected vs Private Attributes
# ------------------------------------------------------------
# public attribute:
#   attr
#   - Accessible everywhere
#
# protected attribute:
#   _attr
#   - Accessible inside the class and child classes
#   - Should not be accessed externally by convention
#
# private attribute:
#   __attr
#   - Accessible only within the defining class
#   - Not accessible in child classes
#   - Uses name mangling to prevent accidental access

# ------------------------------------------------------------
# Conceptual Model
# ------------------------------------------------------------
# public attributes:
#   Intended for unrestricted access
#
# protected attributes:
#   Intended for internal use and subclass access
#
# private attributes:
#   Intended for strict internal use within the class

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - Encapsulation controls how object data is accessed
# - Public attributes are freely accessible
# - Protected attributes are for internal and subclass use
# - Private attributes are restricted to the defining class
# - Child classes cannot access parent private attributes
# - Name-mangled access exists but should not be used in practice
