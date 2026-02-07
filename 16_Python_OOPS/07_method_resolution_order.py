# ============================================================
# Method Resolution Order (MRO) in Python
# ============================================================

# Method Resolution Order defines:
# The order in which Python looks for methods and attributes
# when a class is involved in inheritance.

# Python uses the C3 Linearization algorithm.
# This ensures:
# - A consistent order
# - No ambiguity
# - Parent classes appear before their ancestors

# ------------------------------------------------------------
# Basic Inheritance Example
# ------------------------------------------------------------
class A:
    def show(self):
        print("A.show")

class B(A):
    pass

class C(B):
    pass

c = C()
c.show()

# Lookup order:
# C -> B -> A -> object

print(C.mro())

# ------------------------------------------------------------
# Multiple Inheritance Example
# ------------------------------------------------------------
class A:
    def show(self):
        print("A.show")

class B(A):
    def show(self):
        print("B.show")

class C(A):
    def show(self):
        print("C.show")

class D(B, C):
    pass

d = D()
d.show()

# MRO:
# D -> B -> C -> A -> object

print(D.mro())

# ------------------------------------------------------------
# Key Rules of MRO
# ------------------------------------------------------------
# - Python searches from left to right in the inheritance list
# - Child classes are checked before parent classes
# - object is always the last class
# - MRO can be inspected using ClassName.mro()
