# ============================================================
# 🧬 Inheritance in Python (Parent & Child Classes)
# ============================================================

# Inheritance allows one class to:
#   👉 Reuse code from another class
#   👉 Extend existing behavior
#   👉 Represent real-world relationships
#
# Example:
#   Car        → Parent class (Base)
#   ElectricCar → Child class (Derived)

# ------------------------------------------------------------
# 🚗 Parent Class (Base Class)
# ------------------------------------------------------------
class Car:
    def __init__(self, brand, model):
        # Common attributes for all cars
        self.brand = brand
        self.model = model

    def full_name(self):
        # Common behavior for all cars
        return f"{self.brand} {self.model}"

# ------------------------------------------------------------
# ⚡ Child Class (Derived Class)
# ------------------------------------------------------------
class ElectricCar(Car):
    # ElectricCar INHERITS from Car
    #
    # That means:
    # ✅ It gets brand, model
    # ✅ It gets full_name()
    # ❌ It does NOT automatically get new attributes

    def __init__(self, brand, model, battery_size):
        # ----------------------------------------------------
        # 🔁 super()
        # ----------------------------------------------------
        # super() calls the parent class's __init__()
        # This avoids rewriting the same code again

        super().__init__(brand, model)

        # New attribute specific to ElectricCar
        self.battery_size = battery_size

# ------------------------------------------------------------
# 🧍 Creating an ElectricCar Object
# ------------------------------------------------------------
my_car = ElectricCar("BMW", "M8", "8000kwt")

# ------------------------------------------------------------
# 📦 Accessing Parent Class Attributes
# ------------------------------------------------------------
print(my_car.brand)        # BMW (from Car)
print(my_car.full_name()) # BMW M8 (method from Car)

# ------------------------------------------------------------
# 🔋 Accessing Child Class Attribute
# ------------------------------------------------------------
print(my_car.battery_size)  # 8000kwt

# ------------------------------------------------------------
# 🧠 What Just Happened?
# ------------------------------------------------------------
# 1️⃣ ElectricCar object is created
# 2️⃣ ElectricCar.__init__() is called
# 3️⃣ super().__init__() runs Car.__init__()
# 4️⃣ brand & model are set
# 5️⃣ battery_size is added
#
# Result:
#   One object
#   Data from Parent + Child

# ------------------------------------------------------------
# 🧩 Mental Model
# ------------------------------------------------------------
# Parent Class  → Common features
# Child Class   → Special features
#
# ElectricCar IS-A Car
# (but Car is NOT an ElectricCar)

# ------------------------------------------------------------
# 🚨 Important Rules of Inheritance
# ------------------------------------------------------------
# ✅ Child class can access parent methods
# ✅ Child class can override parent methods
# ✅ super() avoids code duplication
# ❌ Child does NOT automatically add new attributes
# ❌ Parent class does NOT know about child

# ------------------------------------------------------------
# 🧾 Summary
# ------------------------------------------------------------
# Inheritance promotes code reuse
# Parent class defines common behavior
# Child class extends functionality
# super() initializes parent state
# One object can contain data from multiple levels
