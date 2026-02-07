# ============================================================
# 🏠 Python Scopes & Closures (Deep Dive)
# ============================================================

# In Python (and most languages), understanding *scope* is critical.
# Scope decides:
#   👉 Where a variable lives in memory
#   👉 Where it can be accessed
#   👉 Which value is picked when names clash

# ------------------------------------------------------------
# 🧠 What is Scope?
# ------------------------------------------------------------
# Scope defines the *region of code* where a variable is accessible.
#
# In many languages:
#   { }  → define scope
#
# In Python:
#   👉 Indentation defines scope (NO curly braces)

# ------------------------------------------------------------
# 🏠 Mental Model: House & Rooms
# ------------------------------------------------------------
# Think of memory like this:
#
# 🌍 Global scope   → The whole world
# 🏠 Function scope → A house inside the world
# 🚪 Inner function → Rooms inside the house
#
# Rules:
# ✅ House can access its rooms
# ❌ Rooms cannot access outside the house directly
# ❌ Outside world cannot peek inside rooms

# ------------------------------------------------------------
# 🌍 Global Scope Example
# ------------------------------------------------------------
my_name = "Welcome to Python!!"

def greets():
    my_name = "Hello, World"

greets()
print(my_name)   # 👉 "Welcome to Python!!"

# Explanation:
# - Function created its own "house"
# - my_name inside function ≠ global my_name
# - Global value remains untouched

# ------------------------------------------------------------
# 🏠 Nested Scopes (Rooms inside a House)
# ------------------------------------------------------------
def greets():
    my_name = "Hello, World"

    def greet2():
        my_name = "Bye Bye"

    greet2()

    if True:
        my_name = "From If Statement"

greets()

# Notes:
# ✅ greets() can see everything inside it
# ❌ greet2() / if-block variables are NOT visible outside
# ❌ if-block does NOT create a new scope in Python
#     (functions DO)

# ------------------------------------------------------------
# ☕ Example: Variable Lookup (Climbing Up)
# ------------------------------------------------------------
drink = "coffee"

def func():
    drink = "chai"
    print(drink)

print(drink)   # coffee
func()         # chai

# Rule:
# - Python first looks in LOCAL scope
# - If not found → goes one level up
# - Continues until GLOBAL
# - If not found → NameError

# ------------------------------------------------------------
# 🪜 LEGB Rule (Behind the Scenes)
# ------------------------------------------------------------
# Python resolves names in this order:
#
# L → Local
# E → Enclosing (outer functions)
# G → Global
# B → Built-ins

# ------------------------------------------------------------
# 🔢 Global Variable Access (Read-Only)
# ------------------------------------------------------------
x = 99

def func2(y):
    z = x + y   # x is taken from GLOBAL scope
    return z

print(func2(1))   # 100

# ------------------------------------------------------------
# ⚠️ global Keyword (USE WITH CARE)
# ------------------------------------------------------------
def func3():
    global x
    x = 88

func3()
print(x)   # 88

# 🚨 WARNING:
# - global allows mutation of global variables
# - Dangerous in team projects
# - Makes debugging unpredictable
# - Avoid unless absolutely required

# ------------------------------------------------------------
# 🏠 Nested Functions & Enclosing Scope
# ------------------------------------------------------------
x = 99

def f1():
    x = 88   # Local to f1()

    def f2():
        print(x)   # Looks in enclosing scope

    f2()

f1()   # 👉 88

# Explanation:
# - f2() does NOT find x locally
# - Moves up to f1()
# - Stops there (does NOT go to global)

# ------------------------------------------------------------
# 🎒 Closures: Function + Backpack
# ------------------------------------------------------------
# When a function is returned,
# Python packs:
#   ✅ Function definition
#   ✅ References to required variables
#
# This package is called a *closure*

def chai(num):
    def actual(x):
        return x ** num
    return actual

# Create closures
f = chai(2)   # Square
g = chai(3)   # Cube

print(f(3))   # 9
print(g(3))   # 27

# Explanation:
# - chai(2) returns actual + num=2 (packed)
# - chai(3) returns actual + num=3 (packed)
# - Each closure remembers its own num

# ------------------------------------------------------------
# 🧳 Backpack Analogy (Closure Intuition)
# ------------------------------------------------------------
# Returning function alone ❌
# Returning function + environment ✅
#
# The "backpack" carries:
#   - Enclosing variables
#   - Their memory references
#   - Even after outer function exits

# ------------------------------------------------------------
# 🧩 Summary
# ------------------------------------------------------------
# ✅ Indentation defines scope in Python
# ✅ Functions create NEW scopes
# ✅ Python searches variables using LEGB rule
# ✅ Inner functions can access outer variables
# ❌ Outer scopes cannot access inner variables
# ⚠️ global should be avoided
# 🎒 Closures = function + remembered environment
