"""
Error Handling and Exceptions in Python

This file provides a clean, professional, and complete explanation of
error handling and exceptions in Python, using runnable examples and
well-structured comments.

The goal is to show how Python handles runtime errors safely and clearly.
"""

# ============================================================
# Error Handling and Exceptions in Python
# ============================================================
#
# Error handling allows a program to deal with runtime errors gracefully
# instead of crashing. Python uses exceptions to signal and handle errors.


# ============================================================
# 1. What Is an Exception?
# ============================================================
#
# An exception is an event that occurs during program execution and
# disrupts the normal flow of instructions.
#
# Examples:
# - Division by zero
# - Accessing a missing key
# - Invalid type operations
# - File not found


# ============================================================
# 2. Error Handling Without try-except
# ============================================================

def division_1(a, b):
    return a // b

print(division_1(10, 30))
print(division_1(0, 30))

# The following line raises ZeroDivisionError
# and stops the program immediately
# print(division_1(10, 0))


# Behavior:
# - The first two calls work
# - The last call raises ZeroDivisionError
# - Program terminates immediately
# - Remaining code does not execute
#
# This approach is unsafe in real applications.


# ============================================================
# 3. Basic Error Handling: try and except
# ============================================================

def division_2(a, b):
    try:
        result = a // b
        return result
    except ZeroDivisionError as e:
        return f"Exception: {e}"

print(division_2(10, 30))
print(division_2(0, 30))
print(division_2(10, 0))

# Explanation:
# - try contains code that may fail
# - except handles a specific exception
# - Program continues running after the error


# ============================================================
# 4. try, except, else, finally
# ============================================================

def division_3(a, b):
    try:
        result = a // b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        # Executes only if no exception occurred
        return result
    finally:
        # Always executes
        print("Execution completed")

print(division_3(10, 2))
print(division_3(10, 0))

# Key points:
# - else runs only if no exception occurs
# - finally runs regardless of success or failure
# - finally is commonly used for cleanup


# ============================================================
# 5. Built-in Exceptions (Common Ones)
# ============================================================
#
# Some commonly used built-in exceptions:
# - ZeroDivisionError
# - ValueError
# - TypeError
# - IndexError
# - KeyError
# - FileNotFoundError
# - AttributeError
# - ImportError

try:
    int("abc")
except ValueError as e:
    print("Built-in exception example:", e)


# ============================================================
# 6. Catching Multiple Exceptions
# ============================================================

try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print("Multiple exceptions caught:", e)

try:
    x = int("abc")
except ValueError:
    print("Invalid value")
except TypeError:
    print("Wrong type")


# ============================================================
# 7. Custom Exceptions
# ============================================================

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

try:
    check_age(-5)
except InvalidAgeError as e:
    print("Custom exception:", e)

# Custom exceptions improve readability and
# domain-specific error handling.


# ============================================================
# 8. raise Keyword
# ============================================================

try:
    raise ValueError("Invalid input")
except ValueError as e:
    print("Raised manually:", e)

# Re-raising an exception preserves the original traceback
try:
    result = 10 // 0
except ZeroDivisionError:
    print("Logging error before re-raise")
    # raise


# ============================================================
# 9. Exception Chaining
# ============================================================

# Implicit chaining
try:
    int("abc")
except ValueError:
    try:
        raise RuntimeError("Conversion failed")
    except RuntimeError as e:
        print("Implicit chaining:", e)

# Explicit chaining (recommended)
try:
    int("abc")
except ValueError as e:
    try:
        raise RuntimeError("Conversion failed") from e
    except RuntimeError as err:
        print("Explicit chaining:", err)


# ============================================================
# 10. Contextual Exceptions
# ============================================================

# Bad example (loses context)
try:
    raise Exception("Something went wrong")
except Exception as e:
    print("Generic exception:", e)

# Good example (preserves context)
try:
    open("data.txt")
except FileNotFoundError as e:
    try:
        raise FileNotFoundError("Required configuration file missing") from e
    except FileNotFoundError as err:
        print("Contextual exception:", err)


# ============================================================
# 11. Best Practices
# ============================================================
#
# - Catch only specific exceptions
# - Avoid bare except:
# - Do not suppress errors silently
# - Use custom exceptions for business logic
# - Use exception chaining for clarity
# - Use finally for cleanup, not logic


# ============================================================
# 12. Summary
# ============================================================
#
# - Exceptions signal runtime errors
# - try-except prevents program crashes
# - else runs only on success
# - finally always runs
# - Built-in exceptions cover common errors
# - Custom exceptions improve design
# - raise allows manual error signaling
# - Exception chaining preserves context
# - Contextual exceptions improve debuggability
