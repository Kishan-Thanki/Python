"""
Context Managers in Python

This file provides a clean, professional, and complete explanation of
context managers in Python.

Topics covered:
- with statement
- __enter__ and __exit__
- contextlib
- asynccontextmanager
"""

# ============================================================
# Context Managers in Python
# ============================================================
#
# Context managers allow you to allocate and release resources
# precisely when needed.
#
# Common use cases:
# - File handling
# - Database connections
# - Network sockets
# - Locks and synchronization
# - Resource cleanup


# ============================================================
# 1. with Statement
# ============================================================
#
# The with statement simplifies resource management.
# It ensures setup and cleanup logic is always executed.

with open("example.txt", "w") as f:
    f.write("Context manager example")

# Internally, Python does:
#
# manager = open("example.txt", "w")
# manager.__enter__()
# try:
#     f.write(...)
# finally:
#     manager.__exit__()


# ============================================================
# 2. __enter__ and __exit__ Methods
# ============================================================
#
# Any object that implements __enter__ and __exit__
# can be used as a context manager.

class CustomContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        # Returning False propagates exceptions
        return False

with CustomContext():
    print("Inside context block")


# ============================================================
# 3. Exception Handling in __exit__
# ============================================================
#
# __exit__ receives exception details:
# - exc_type
# - exc_value
# - traceback
#
# If __exit__ returns True, the exception is suppressed.

class SuppressExceptionContext:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")
        return True

with SuppressExceptionContext():
    1 / 0  # ZeroDivisionError is suppressed

print("Program continues after suppressed exception")


# ============================================================
# 4. contextlib.contextmanager
# ============================================================
#
# contextlib allows defining context managers using generators.
# This is cleaner and more readable for simple cases.

from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring resource: {name}")
    try:
        yield name
    finally:
        print(f"Releasing resource: {name}")

with managed_resource("Database Connection") as resource:
    print("Using resource:", resource)


# ============================================================
# 5. Nested Context Managers
# ============================================================

@contextmanager
def first():
    print("Enter first")
    yield
    print("Exit first")

@contextmanager
def second():
    print("Enter second")
    yield
    print("Exit second")

with first(), second():
    print("Inside nested contexts")


# ============================================================
# 6. asynccontextmanager
# ============================================================
#
# Used for asynchronous resource management.
# Works with async/await and async with.

from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def async_resource():
    print("Async acquire resource")
    await asyncio.sleep(1)
    try:
        yield "Async Resource"
    finally:
        print("Async release resource")

async def main():
    async with async_resource() as resource:
        print("Using:", resource)

asyncio.run(main())


# ============================================================
# 7. When to Use Which Approach
# ============================================================
#
# Use with + __enter__/__exit__:
# - When building reusable, stateful context managers
#
# Use @contextmanager:
# - For simple setup/teardown logic
#
# Use @asynccontextmanager:
# - For async I/O resources


# ============================================================
# 8. Summary
# ============================================================
#
# - Context managers manage resources safely
# - with statement ensures cleanup
# - __enter__ sets up context
# - __exit__ handles cleanup and exceptions
# - contextlib simplifies context manager creation
# - asynccontextmanager supports asynchronous contexts
#
# Context managers are essential for safe and clean Python code.
