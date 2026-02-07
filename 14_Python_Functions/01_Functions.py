# ============================================================
# 🧩 Basic Function Syntax
# ============================================================

# Let's start simple — write a function to calculate and return the square of a number.

# In Python, we call this a *function definition*.
# Because in other languages like JavaScript or Go, we use keywords like `function` or `func`,
# but in Python, we define functions using the keyword: `def`.

# ------------------------------------------------------------
# ⚙️ Defining a Function
# ------------------------------------------------------------

# 1️⃣ Every function should have a name — something meaningful.
# Example: square, square_of_num, get_square, etc.

# ❌ Wrong
# def square

# ✅ Correct function header syntax:
def square():
    pass   # 'pass' means "do nothing" — placeholder to avoid syntax error


# ------------------------------------------------------------
# 2️⃣ Parameters (Placeholders for Values)
# ------------------------------------------------------------
# Parentheses () can hold parameters — values that are passed into the function.
# These are like input variables that the function can use inside its body.

def square(number):
    # Inside the function, we write our operation logic.
    print(number ** 2)       # Prints the square
    return number ** 2       # Returns the square back to the caller


# ------------------------------------------------------------
# 🧪 Calling a Function
# ------------------------------------------------------------
# Defining a function doesn't run it. To execute, we must CALL it using parentheses ().

# ❌ This won’t work — because no value is passed:
# square()

# ✅ Pass a value that the function expects:
square(4)


# ------------------------------------------------------------
# 💾 Storing Function Output
# ------------------------------------------------------------
# When a function returns something using 'return',
# we can store that output in a variable.

result = square(4)
print(result)    # This prints the returned value


# ------------------------------------------------------------
# 🧠 Notes:
# ------------------------------------------------------------
# ✔ `def` → defines a function
# ✔ Parentheses () → hold parameters (optional)
# ✔ `:` → marks the start of function block
# ✔ Indentation → defines the function body
# ✔ `return` → sends a value back to where the function was called
# ✔ If no `return` → function returns None by default
