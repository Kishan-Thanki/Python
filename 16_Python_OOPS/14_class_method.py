# ============================================================
# Class Methods (@classmethod) in Python
# ============================================================

# Class methods are:
#   - Methods bound to the class, not the instance
#   - Receive the class itself as the first argument (cls)
#   - Used to operate on or modify class-level data
#
# In simple terms:
# Class methods work with the class as a whole,
# not with a specific object.

# ------------------------------------------------------------
# Defining a Class Method
# ------------------------------------------------------------

class Car:
    # Class variable
    total_car = 0

    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model
        Car.total_car += 1

    # --------------------------------------------------------
    # Class Method
    # --------------------------------------------------------
    # @classmethod is a decorator
    # It tells Python:
    # "This method receives the class as the first argument"
    @classmethod
    def get_total_car(cls):
        return cls.total_car

    # Another class method (factory-style)
    @classmethod
    def create_electric_car(cls, model):
        return cls("Tesla", model)

    # Instance method
    def get_car(self):
        return f"{self.brand} {self.model}"


# ============================================================
# Creating Objects
# ============================================================

car1 = Car("BMW", "M8")
car2 = Car("Porsche", "911")

# Creating object using class method (factory)
car3 = Car.create_electric_car("Model Y")

# ============================================================
# Calling Class Method
# ============================================================

print(Car.get_total_car())    # 3

# Also callable via instance (allowed, but discouraged)
print(car1.get_total_car())  # 3

# ============================================================
# Calling Instance Method
# ============================================================

print(car1.get_car())         # BMW M8
print(car3.get_car())         # Tesla Model Y

# ============================================================
# Why Use cls Instead of Class Name
# ============================================================

# Using cls ensures:
#   - Proper behavior with inheritance
#   - Correct class is referenced at runtime

class ElectricCar(Car):
    pass

ecar = ElectricCar("Tesla", "Model S")

print(ElectricCar.get_total_car())  # 4

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - cls refers to the calling class
# - When called via ElectricCar, cls == ElectricCar
# - Prevents hard-coding the class name

# ============================================================
# Class Method vs Static Method
# ============================================================

# Static method:
#   - No self, no cls
#   - Utility/helper logic
#
# Class method:
#   - Receives cls
#   - Can access and modify class variables
#   - Supports polymorphism across subclasses

# ============================================================
# When to Use @classmethod
# ============================================================

# Working with class-level data
# Factory methods
# Alternative constructors
# Behavior that should apply to the class, not instances
# Inheritance-aware logic

# Object-specific behavior
# Pure utility functions (use staticmethod instead)

# ============================================================
# Summary
# ============================================================

# - @classmethod binds a method to the class
# - cls represents the calling class
# - Can be called via class or instance
# - Ideal for class-level operations and factories
# - Safer than hard-coding class names
# - Essential for inheritance-friendly design
