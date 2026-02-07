# ============================================================
# Generators in Python
# ============================================================

# Generators are:
#   - Functions that return an iterator
#   - Produce values one at a time using `yield`
#   - Pause execution and resume later
#
# In simple terms:
# Generators generate values lazily, not all at once.

# ------------------------------------------------------------
# Why Generators Exist
# ------------------------------------------------------------

# Lists store all values in memory
# Generators produce values on demand
# Ideal for large data or infinite sequences

# ============================================================
# Generator Function (yield)
# ============================================================

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


# Generator object created (no execution yet)
gen = count_up_to(5)

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Remaining values
for value in gen:
    print(value)

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - yield pauses function execution
# - State is preserved between calls
# - next() resumes execution
# - StopIteration is raised automatically

# ============================================================
# Generator vs Regular Function
# ============================================================

def list_numbers(n):
    return [i for i in range(1, n + 1)]


def generator_numbers(n):
    for i in range(1, n + 1):
        yield i


print(list_numbers(5))           # [1, 2, 3, 4, 5]
print(generator_numbers(5))      # <generator object>

# ------------------------------------------------------------
# Memory Difference:
# ------------------------------------------------------------
# list_numbers → stores all values
# generator_numbers → produces one value at a time

# ============================================================
# Generator Expression
# ============================================================

# Similar to list comprehensions, but lazy
squares = (x * x for x in range(5))

print(next(squares))  # 0
print(next(squares))  # 1

for value in squares:
    print(value)

# ============================================================
# Infinite Generators
# ============================================================

def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1


counter = infinite_counter()

print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# ⚠️ Must be consumed carefully

# ============================================================
# Generator with send()
# ============================================================

def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


acc = accumulator()
print(next(acc))        # Initialize generator
print(acc.send(10))     # 10
print(acc.send(20))     # 30

# ------------------------------------------------------------
# Explanation:
# ------------------------------------------------------------
# - send() sends a value INTO the generator
# - next() is equivalent to send(None)

# ============================================================
# Generator Close & throw()
# ============================================================

def safe_generator():
    try:
        while True:
            yield "Running"
    except GeneratorExit:
        print("Generator closed")


gen = safe_generator()
print(next(gen))
gen.close()   # Triggers GeneratorExit

# ============================================================
# yield from (Delegating Generators)
# ============================================================

def sub_generator():
    yield 1
    yield 2


def main_generator():
    yield from sub_generator()
    yield 3


for value in main_generator():
    print(value)

# ============================================================
# Generators & Iteration Protocol
# ============================================================

# Generators automatically implement:
#   __iter__()
#   __next__()

# This is why they work in:
#   - for loops
#   - next()
#   - list(), sum(), any(), all()

# ============================================================
# Real-World Use Cases
# ============================================================

# Streaming large files
# Processing big datasets
# Infinite sequences
# Pipelines & data processing
# Event-driven systems

# ============================================================
# Generators vs Iterators vs Iterables
# ============================================================

# Iterable:
#   - Can return an iterator (__iter__)
#
# Iterator:
#   - Has __next__
#
# Generator:
#   - Iterator created via yield

# ============================================================
# Common Pitfalls
# ============================================================

# Exhausting a generator and reusing it
# Forgetting next() before send()
# Converting generator to list accidentally

# ============================================================
# Summary
# ============================================================

# - Generators produce values lazily
# - yield pauses and resumes execution
# - Memory-efficient and powerful
# - Support send(), throw(), close()
# - Built on Python's iterator protocol
# - Essential for performance-critical code
