# ============================================================
# Python Introspection & Dynamic Object Tools
# ============================================================

# These built-in tools allow:
#   - Type inspection
#   - Inheritance checks
#   - Attribute inspection
#   - Dynamic access and modification
#   - Behavior validation at runtime
#
# These are essential for:
#   - Polymorphism
#   - Duck typing
#   - Frameworks & libraries
#   - Dynamic and flexible code

# ------------------------------------------------------------
# Tools Overview
# ------------------------------------------------------------
#
# Purpose                  Tool
# -----------------------  ----------------
# Instance check           isinstance
# Exact type check         type
# Inheritance check        issubclass
# Attribute existence      hasattr
# Dynamic access           getattr
# Dynamic modification     setattr
# Callable detection       callable

# ============================================================
# Example Classes
# ============================================================

class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


dog = Dog()

# ============================================================
# isinstance → Instance Check
# ============================================================

print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True
print(isinstance(dog, object))   # True

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Checks object against class OR its parent classes
# - Preferred over type() for polymorphism
# - Respects inheritance hierarchy

# ============================================================
# type → Exact Type Check
# ============================================================

print(type(dog) == Dog)          # True
print(type(dog) == Animal)       # False

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Checks exact class only
# - Does NOT consider inheritance
# - Use sparingly (breaks polymorphism)

# ============================================================
# issubclass → Inheritance Check
# ============================================================

print(issubclass(Dog, Animal))   # True
print(issubclass(Animal, Dog))   # False

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Checks class-to-class relationship
# - Useful in metaprogramming and frameworks
# - Works only with classes, not instances

# ============================================================
# hasattr → Attribute Existence Check
# ============================================================

print(hasattr(dog, "speak"))     # True
print(hasattr(dog, "run"))       # False

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Safely checks if attribute exists
# - Prevents AttributeError
# - Useful in duck typing

# ============================================================
# getattr → Dynamic Attribute Access
# ============================================================

method_name = "speak"

if hasattr(dog, method_name):
    method = getattr(dog, method_name)
    print(method())              # Dog barks

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Access attributes dynamically by name
# - Supports default value:
#   getattr(obj, "attr", default)
# - Core tool in plugins & reflection

# ============================================================
# setattr → Dynamic Attribute Modification
# ============================================================

setattr(dog, "age", 3)
print(dog.age)                   # 3

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Adds or modifies attributes at runtime
# - Extremely powerful but dangerous if misused
# - Can break encapsulation if careless

# ============================================================
# callable → Callable Detection
# ============================================================

print(callable(dog.speak))       # True
print(callable(dog))             # False

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Checks if an object can be called like a function
# - Used heavily in decorators and frameworks

# ============================================================
# Combined Real-World Example
# ============================================================

def invoke_if_callable(obj, method_name):
    if hasattr(obj, method_name):
        attr = getattr(obj, method_name)
        if callable(attr):
            return attr()
    return None


print(invoke_if_callable(dog, "speak"))  # Dog barks

# ============================================================
# Best Practices
# ============================================================

# Prefer isinstance over type
# Avoid strict type checks unless necessary
# Use hasattr + getattr for safe dynamic access
# Use callable before invoking unknown objects
# Be cautious with setattr (encapsulation risk)

# ============================================================
# Summary
# ============================================================

# - isinstance checks object identity across inheritance
# - type checks exact class
# - issubclass checks class inheritance
# - hasattr checks attribute existence
# - getattr accesses attributes dynamically
# - setattr modifies objects dynamically
# - callable checks if an object is executable

# These tools enable:
#   - Polymorphism
#   - Duck typing
#   - Reflection
#   - Framework-level flexibility
