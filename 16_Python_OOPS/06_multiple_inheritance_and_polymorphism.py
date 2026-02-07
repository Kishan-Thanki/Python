# ============================================================
# Multiple Inheritance and Polymorphism
# ============================================================

# Multiple inheritance means:
# A class inherits from more than one parent class.

# Polymorphism allows:
# Different parent classes to define the same method name,
# while the child decides which implementation to use.

# ------------------------------------------------------------
# Multiple Inheritance Example
# ------------------------------------------------------------
class Engine:
    def start(self):
        print("Engine started")

class Electric:
    def start(self):
        print("Electric motor started")

class HybridCar(Engine, Electric):
    pass

car = HybridCar()
car.start()

# Due to MRO, Engine.start is called first.

print(HybridCar.mro())

# ------------------------------------------------------------
# Using super() with Multiple Inheritance
# ------------------------------------------------------------
# super() follows MRO and ensures all parent classes
# get a chance to execute their methods.

class Engine:
    def start(self):
        print("Engine start")

class Electric:
    def start(self):
        print("Electric start")

class HybridCar(Engine, Electric):
    def start(self):
        super().start()
        print("Hybrid ready")

HybridCar().start()

# ------------------------------------------------------------
# Important Guidelines
# ------------------------------------------------------------
# - Always design parent classes to cooperate with super()
# - Avoid deep and complex inheritance trees
# - Prefer composition if inheritance becomes confusing
