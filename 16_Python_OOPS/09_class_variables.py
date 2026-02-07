# ============================================================
# Class Variables in Python
# ============================================================

# Class variables are:
#   - Shared across all instances of a class
#   - Defined inside the class but outside any instance methods
#   - Used to represent data common to all objects

# In simple terms:
# One variable → One copy → Shared by all objects

# ------------------------------------------------------------
# Defining a Class Variable
# ------------------------------------------------------------

class Car:
    # Class variable (shared across all instances)
    total_car = 0

    def __init__(self, brand, model):
        # Instance variables (unique to each object)
        self.__brand = brand
        self.__model = model

        # Modifying class variable using class name
        Car.total_car += 1

    def get_full_name(self):
        return f"{self.__brand} {self.__model}"


# ------------------------------------------------------------
# Creating Objects
# ------------------------------------------------------------

my_car1 = Car("BMW", "M8")
my_car2 = Car("Tesla", "Model Y")
my_car3 = Car("Porsche", "911")

# ------------------------------------------------------------
# Accessing Instance-Specific Data
# ------------------------------------------------------------

print(my_car1.get_full_name())   # BMW M8
print(my_car2.get_full_name())   # Tesla Model Y
print(my_car3.get_full_name())   # Porsche 911

# ------------------------------------------------------------
# Accessing Class Variable
# ------------------------------------------------------------

# Preferred and correct way
print(Car.total_car)     # 3

# Also accessible via instances (but not recommended)
print(my_car1.total_car) # 3
print(my_car2.total_car) # 3
print(my_car3.total_car) # 3

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - total_car belongs to the class, not individual objects
# - All instances see the same value
# - Each object creation increments the same variable
# - Accessing via class name is best practice
# - Accessing via object works due to attribute lookup rules

# ============================================================
# Important Concept: Attribute Lookup Order
# ============================================================

# When Python evaluates:
#   my_car1.total_car
#
# Python checks in this order:
# 1. Instance namespace (my_car1.__dict__)
# 2. Class namespace (Car.__dict__)
# 3. Parent classes (if any)

# Since total_car is not found in the instance,
# Python retrieves it from the class.

# ============================================================
# Common Pitfall: Shadowing Class Variables
# ============================================================

# If we assign through an instance:
my_car1.total_car = 10

print(my_car1.total_car)  # 10 (instance variable created!)
print(my_car2.total_car)  # 3  (class variable unchanged)
print(Car.total_car)      # 3

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Assignment via instance creates a NEW instance attribute
# - It does NOT modify the class variable
# - This is called variable shadowing
# - Can cause hard-to-debug bugs if misunderstood

# ============================================================
# Correct Way to Modify Class Variables
# ============================================================

# Always use the class name
Car.total_car = 5

print(Car.total_car)      # 5
print(my_car1.total_car)  # 10 (still shadowed)
print(my_car2.total_car)  # 5

# ============================================================
# Class Variables vs Instance Variables
# ============================================================

# Instance variables:
#   - Defined using self
#   - Unique per object
#   - Stored in object.__dict__

# Class variables:
#   - Defined in class body
#   - Shared across all instances
#   - Stored in Class.__dict__

# ============================================================
# When to Use Class Variables
# ============================================================

# ✔ Object counters (like total_car)
# ✔ Shared configuration values
# ✔ Constants related to the class
# ✔ Caching common data

# ❌ Object-specific state
# ❌ Data that varies per instance

# ============================================================
# Summary
# ============================================================

# - Class variables are shared across all instances
# - Only one copy exists per class
# - Modify class variables using the class name
# - Access via instance works but is discouraged
# - Instance assignment shadows class variables
# - Understanding lookup order is crucial

