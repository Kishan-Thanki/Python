# ============================================================
# ⚙️ Python Functions
# ============================================================

# Now, the most important thing you should know about functions is:
#   1️⃣ Function Definition
#   2️⃣ Function Usage (calling or invoking)
#
# Functions are reusable blocks of code designed to perform a specific task.
# Instead of writing the same logic again and again, 
# we wrap it in a function and simply call it whenever needed.

# ------------------------------------------------------------
# 🧩 Function Definition
# ------------------------------------------------------------
# The keyword 'def' is used to define a function in Python.

def make_tea():
    print("Boil Water")
    print("Add Tea Leaves")
    print("Add Milk and Sugar")
    print("Serve Hot Tea")

# ------------------------------------------------------------
# 🧪 Function Call
# ------------------------------------------------------------
# Simply call the function by using its name followed by parentheses.
make_tea()

# ------------------------------------------------------------
# 🎯 Functions with Parameters
# ------------------------------------------------------------
# We can also pass data to functions using *parameters*.
# These act as input variables for the function.

def make_tea_with_flavor(flavor):
    print(f"Making {flavor} Tea")

make_tea_with_flavor("Masala")
make_tea_with_flavor("Lemon")

# ------------------------------------------------------------
# 🔄 Functions with Multiple Parameters
# ------------------------------------------------------------
# You can define multiple parameters separated by commas.

def make_tea_with_details(flavor, quantity):
    print(f"Preparing {quantity} cups of {flavor} tea")

make_tea_with_details("Ginger", 2)

# ------------------------------------------------------------
# 🎁 Returning Values
# ------------------------------------------------------------
# Functions can return results using the 'return' statement.
# This is useful when you want to store or reuse the result later.

def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# ------------------------------------------------------------
# 🧮 Default Parameter Values
# ------------------------------------------------------------
# You can set default values for parameters.
# If no argument is passed, Python uses the default.

def make_tea_default(flavor="Masala"):
    print(f"Preparing {flavor} Tea")

make_tea_default()          # Uses default flavor
make_tea_default("Green")   # Overrides default flavor

# ------------------------------------------------------------
# 🔹 Keyword Arguments
# ------------------------------------------------------------
# You can also pass arguments by naming them explicitly.

def describe_tea(flavor, strength):
    print(f"{flavor} Tea - {strength} strength")

describe_tea(strength="Strong", flavor="Black")

# ------------------------------------------------------------
# ✳️ Arbitrary Arguments (*args)
# ------------------------------------------------------------
# If you don’t know how many arguments will be passed, use *args.
# It collects all extra arguments into a tuple.

def make_many_teas(*flavors):
    print("Available Tea Flavors:")
    for tea in flavors:
        print("-", tea)

make_many_teas("Masala", "Lemon", "Ginger", "Green")

# ------------------------------------------------------------
# ✴️ Keyword Arbitrary Arguments (**kwargs)
# ------------------------------------------------------------
# Similar to *args, but used when you want to pass key-value pairs.
# **kwargs collects them into a dictionary.

def tea_order(**details):
    print("Order Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

tea_order(customer="Hitesh", flavor="Green", quantity=2)

# ------------------------------------------------------------
# 🧠 Function Scope
# ------------------------------------------------------------
# Variables defined inside a function are *local* to that function.
# They cannot be accessed outside.

def local_example():
    message = "This is local to the function"
    print(message)

local_example()
# print(message)  # ❌ Error: message is not defined

# ------------------------------------------------------------
# 🌍 Global Variables
# ------------------------------------------------------------
# If you declare a variable outside the function, 
# it can be accessed inside using the global keyword.

x = "Masala Tea"

def global_example():
    global x
    x = "Green Tea"
    print("Inside function:", x)

global_example()
print("Outside function:", x)

# ------------------------------------------------------------
# 🪄 Lambda Functions (Anonymous Functions)
# ------------------------------------------------------------
# These are small one-line functions without a name.
# Commonly used for short operations.

square = lambda n: n ** 2
print("Square of 5:", square(5))

add_nums = lambda a, b: a + b
print("Sum using lambda:", add_nums(3, 4))

# ------------------------------------------------------------
# ✅ Summary
# ------------------------------------------------------------
# ✔ 'def' keyword is used to define a function
# ✔ Parameters allow passing data to a function
# ✔ 'return' sends back data from a function
# ✔ Default, keyword, *args, **kwargs handle flexible inputs
# ✔ Local variables live only inside functions
# ✔ Lambda functions provide concise one-liners
