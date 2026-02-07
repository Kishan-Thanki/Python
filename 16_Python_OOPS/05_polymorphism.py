# ============================================================
# Polymorphism in Python
# ============================================================

# Polymorphism means:
#   - One interface, many implementations
#   - Same method name behaving differently based on object type
#
# In simple terms:
# Different objects respond differently to the same method call.

# ------------------------------------------------------------
# Types of Polymorphism in Python
# ------------------------------------------------------------
# 1. Method Overloading (Compile-Time concept)
# 2. Method Overriding (Runtime Polymorphism)
# 3. Polymorphic Variables
# 4. Abstraction-based Polymorphism
# 5. Flexibility & Reusability through polymorphism
#
# Note:
# Python is dynamically typed, so "compile-time polymorphism"
# is achieved differently compared to Java/C++.

# ============================================================
# Method Overloading (Python-style)
# ============================================================

# In languages like Java:
#   add(int, int)
#   add(String, String)
#
# Python does NOT support true method overloading by signature.
# Instead, it uses:
#   - Default arguments
#   - Variable-length arguments (*args)

class Calculator:
    def add(self, a, b=None):
        if b is None:
            return a
        return a + b


calc = Calculator()

print(calc.add(5))        # 5
print(calc.add(5, 10))    # 15

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Same method name: add
# - Different behavior based on arguments
# - This mimics method overloading
#
# Achieved at runtime (not compile-time like Java)

# ============================================================
# Method Overriding (Runtime Polymorphism)
# ============================================================

class Animal:
    def speak(self):
        return "Animal makes a sound"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


class Cat(Animal):
    def speak(self):
        return "Cat meows"


# ------------------------------------------------------------
# Runtime Behavior
# ------------------------------------------------------------

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())

# Output:
# Dog barks
# Cat meows
# Animal makes a sound

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Method resolution happens at runtime
# - Same method name: speak()
# - Behavior depends on the object type, not variable type
#
# This is TRUE polymorphism

# ============================================================
# Polymorphic Variables
# ============================================================

# A single variable can reference objects of different subclasses

def make_animal_speak(animal: Animal):
    print(animal.speak())


make_animal_speak(Dog())
make_animal_speak(Cat())

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Variable 'animal' is of type Animal
# - It can hold Dog or Cat objects
# - The correct method is called dynamically
#
# Enables loose coupling

# ============================================================
# Abstraction and Polymorphism
# ============================================================

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        return 10 * 5


class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5


# ------------------------------------------------------------
# Using Abstract Type
# ------------------------------------------------------------

shapes = [Rectangle(), Circle()]

for shape in shapes:
    print(shape.area())

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Shape defines a common interface
# - Concrete classes provide implementations
# - Caller works with abstract type, not concrete classes
#
# Core principle of abstraction-driven polymorphism

# ============================================================
# Duck Typing (Python-specific Polymorphism)
# ============================================================

# "If it looks like a duck and quacks like a duck, it is a duck"

class FileLogger:
    def write(self):
        print("Writing to file")


class DatabaseLogger:
    def write(self):
        print("Writing to database")


def log(writer):
    writer.write()


log(FileLogger())
log(DatabaseLogger())

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - No inheritance required
# - No common base class needed
# - Only method presence matters
#
# Extremely powerful Python polymorphism

# ============================================================
# Flexibility & Reusability
# ============================================================

def process_payment(payment_gateway):
    payment_gateway.pay()

# Any object with pay() method works:
# - CreditCardPayment
# - PayPalPayment
# - CryptoPayment

# ------------------------------------------------------------
# Benefits:
# ------------------------------------------------------------
# - Reduces code duplication
# - Improves extensibility
# - Promotes open/closed principle
# - Makes systems easier to maintain

# ============================================================
# Summary
# ============================================================

# - Polymorphism allows one interface, many implementations
# - Python simulates method overloading using arguments
# - Method overriding enables runtime polymorphism
# - Polymorphic variables hold different subclass objects
# - Abstraction allows working with general types
# - Duck typing enables flexible, decoupled designs
# - Polymorphism increases flexibility and reusability

# ============================================================
# Conceptual Model
# ============================================================

# Same method call → Different behavior
# Based on:
#   - Object type
#   - Implementation
#   - Runtime resolution
