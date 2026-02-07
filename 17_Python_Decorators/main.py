# ============================================================
# Decorators in Python
# ============================================================

# Decorators are:
#   - Functions that modify other functions or methods
#   - Used to add behavior WITHOUT changing original code
#   - A direct application of higher-order functions
#
# In simple terms:
# Decorators wrap a function with extra functionality.

# ------------------------------------------------------------
# How Decorators Work (Concept)
# ------------------------------------------------------------

# @decorator
# def my_function():
#     pass
#
# is equivalent to:
# my_function = decorator(my_function)

# ============================================================
# Example 1: Timing Decorator
# ============================================================

import time


def timer(func):
    # Wrapper function wraps the original function
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.2f} seconds")
        return result
    return wrapper


@timer
def example(t: int):
    time.sleep(t)


example(5)

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - timer receives a function
# - wrapper adds timing logic
# - *args, **kwargs allow any arguments
# - Original function behavior remains unchanged
#
# ✔ Common use: profiling, logging, monitoring

# ============================================================
# Example 2: Debug / Logging Decorator
# ============================================================

def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(
            f"{key}={value}" for key, value in kwargs.items()
        )
        print(
            f"calling: {func.__name__} "
            f"with args: {args_values} "
            f"and kwargs: {kwargs_values}"
        )
        return func(*args, **kwargs)
    return wrapper


@debug
def greeting(name, greets="Hello"):
    print(f"{greets}, {name}")


greeting("John")

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Adds logging without touching greeting()
# - Useful for debugging, tracing, auditing
# - Widely used in frameworks (Flask, Django)

# ============================================================
# Example 3: Caching Decorator (Memoization)
# ============================================================

def cache(func):
    cache_value = {}

    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]

        result = func(*args, **kwargs)
        cache_value[args] = result
        return result

    return wrapper


@cache
def heavy_processing_function(a, b):
    time.sleep(4)
    return a + b


print(heavy_processing_function(30, 60))  # slow
print(heavy_processing_function(40, 20))  # slow
print(heavy_processing_function(30, 60))  # fast (cached)

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - Stores results of expensive function calls
# - Reuses cached results for same inputs
# - Improves performance dramatically
#
# ✔ Python provides functools.lru_cache for production use

# ============================================================
# Important Best Practice: functools.wraps
# ============================================================

# Without wraps:
# - func.__name__ is lost
# - docstring is lost
# - metadata is overwritten

from functools import wraps


def better_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.2f} seconds")
        return result
    return wrapper

# ============================================================
# Decorators with Arguments (Preview)
# ============================================================

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi!")

# ============================================================
# Where Decorators Are Used
# ============================================================

# ✔ Logging
# ✔ Authentication & authorization
# ✔ Caching
# ✔ Validation
# ✔ Rate limiting
# ✔ Performance measurement
# ✔ Framework internals

# ============================================================
# Summary
# ============================================================

# - Decorators modify functions without changing them
# - They rely on functions being first-class objects
# - @syntax is just syntactic sugar
# - wrapper() adds extra behavior
# - *args, **kwargs ensure flexibility
# - functools.wraps preserves metadata
