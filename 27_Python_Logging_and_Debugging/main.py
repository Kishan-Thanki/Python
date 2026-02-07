"""
Logging and Debugging in Python

This file provides a clean, professional, and structured overview of
logging and debugging in Python.

Topics covered:
- logging module
- Log levels
- Debuggers (pdb)
- Tracebacks
- Stack inspection
"""

# ============================================================
# 1. Why Logging and Debugging Matter
# ============================================================
#
# Logging and debugging help you:
# - Understand program behavior
# - Diagnose failures in production
# - Trace execution flow
# - Investigate unexpected states
#
# Debugging is usually interactive and temporary.
# Logging is permanent and should exist in production code.


# ============================================================
# 2. logging Module
# ============================================================
#
# The logging module is Python’s standard way to record events.
# It is preferred over print statements for real applications.

import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("This is a warning")
logger.error("This is an error message")


# ============================================================
# 3. Log Levels
# ============================================================
#
# Logging levels (from lowest to highest severity):
#
# DEBUG     Detailed diagnostic information
# INFO      General operational messages
# WARNING   Something unexpected, but program continues
# ERROR     Serious issue, operation failed
# CRITICAL  Application may not continue running

logger.debug("Debug-level message (may not appear)")
logger.info("Info-level message")
logger.warning("Warning-level message")
logger.error("Error-level message")
logger.critical("Critical-level message")

# Best practices:
# - Use DEBUG for development
# - Use INFO for normal operations
# - Use WARNING and above sparingly
# - Never log sensitive information


# ============================================================
# 4. Logging Exceptions
# ============================================================
#
# Use logger.exception inside except blocks.
# It automatically logs the traceback.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("Division by zero occurred")
        return None

divide(10, 0)


# ============================================================
# 5. Debuggers (pdb)
# ============================================================
#
# pdb is Python’s built-in interactive debugger.
# It allows step-by-step execution and inspection.

# Common pdb commands:
#
# l   -> list source code
# n   -> next line
# s   -> step into function
# c   -> continue execution
# q   -> quit debugger
# p x -> print variable x

def calculate_total(price, tax):
    import pdb
    pdb.set_trace()  # Execution pauses here
    return price + tax

# Uncomment to test:
# calculate_total(100, 18)


# ============================================================
# 6. Tracebacks
# ============================================================
#
# A traceback shows the call stack at the point an exception occurs.
# It is essential for debugging errors.

def level_one():
    level_two()

def level_two():
    level_three()

def level_three():
    raise ValueError("Something went wrong")

try:
    level_one()
except ValueError as e:
    logger.error("Caught an exception", exc_info=True)


# ============================================================
# 7. Traceback Module
# ============================================================
#
# The traceback module allows programmatic access to tracebacks.

import traceback

try:
    int("abc")
except ValueError:
    traceback.print_exc()


# ============================================================
# 8. Stack Inspection
# ============================================================
#
# Stack inspection lets you examine the call stack at runtime.
# Useful for debugging complex flows and frameworks.

import inspect

def outer_function():
    inner_function()

def inner_function():
    stack = inspect.stack()
    for frame in stack:
        print(f"Function: {frame.function}, Line: {frame.lineno}")

# Uncomment to test:
# outer_function()


# ============================================================
# 9. Common Debugging Techniques
# ============================================================
#
# - Use logging instead of print
# - Log inputs and outputs at boundaries
# - Use pdb for interactive debugging
# - Read tracebacks from bottom to top
# - Isolate failures with minimal reproducible examples
# - Avoid swallowing exceptions silently


# ============================================================
# 10. Logging vs Debugging
# ============================================================
#
# Logging:
# - Persistent
# - Used in production
# - Helps post-mortem analysis
#
# Debugging:
# - Interactive
# - Used during development
# - Helps understand control flow


# ============================================================
# 11. Summary
# ============================================================
#
# - logging module is the standard logging solution
# - Log levels control message severity
# - logger.exception captures tracebacks automatically
# - pdb enables step-by-step debugging
# - Tracebacks explain error origins
# - Stack inspection reveals execution flow
#
# Mastering logging and debugging is essential for
# building reliable and maintainable Python systems.
