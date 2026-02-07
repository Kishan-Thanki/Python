# ============================================================
# 🔁 Python Loops and Iteration
# ============================================================

# In Python, looping is not as complicated as in some other languages.
# Under the hood, Python uses an *iterator protocol* to handle loops.
# Let's break it down step by step.

# ------------------------------------------------------------
# 🧠 What is Iteration?
# ------------------------------------------------------------
# Iteration is just a fancy word for “doing something repeatedly”.
# Python provides iteration tools such as:
#   1️⃣ for loop
#   2️⃣ comprehensions (like list comprehensions)

# But these tools work only if the object is *iterable* — i.e., it supports iteration.
# Examples of iterable objects:
#   - Lists
#   - Strings
#   - Files
#   - Tuples
#   - Dictionaries, etc.

# ------------------------------------------------------------
# ⚙️ How Iteration Works Internally
# ------------------------------------------------------------
# 1️⃣ The iteration tool (like a for loop) requests data from the iterable.
# 2️⃣ The iterable returns an *iterator* object when we call iter().
# 3️⃣ Then, the iterator gives elements one by one when we call next().
# 4️⃣ When there are no more items, it raises a StopIteration exception.

# In short:
#   iterable → iter() → iterator → next() → values → StopIteration (end)

# ------------------------------------------------------------
# 🧩 Example: Understanding __next__ and iter()
# ------------------------------------------------------------
myList = [1, 2, 3, 4]

# Create an iterator from the list
i = iter(myList)
print(i)

# Retrieve elements one by one
print(i.__next__())  # 1
print(i.__next__())  # 2
print(i.__next__())  # 3
print(i.__next__())  # 4

# Now, if we call next() again, it will raise StopIteration
# print(i.__next__())  # ❌ StopIteration

# ------------------------------------------------------------
# 🧾 Why doesn’t the loop go out of bounds?
# ------------------------------------------------------------
# When you loop over a list like [1, 2, 3, 4],
# Python internally keeps track of the iterator’s position.
# It calls __next__() until the StopIteration signal tells it to stop.
# That’s how it knows where to start and when to stop — no explicit indexing!

# ------------------------------------------------------------
# 📂 Iteration on Files
# ------------------------------------------------------------
# Files are special — they are *already iterable*.
# Let’s see how this works.

"""
Example REPL output (for understanding):

>>> f = open('chai.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'username = "hitesh"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''   # Empty string means end of file

>>> f = open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username = "hitesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  StopIteration
"""

# So when Python encounters an empty line ('') in a file, it knows to stop looping.

# ------------------------------------------------------------
# 🪄 File Iteration in Action
# ------------------------------------------------------------
# Instead of manually calling next(), we usually just write:
for line in open('script.py'):
    print(line)

# Under the hood, this for-loop is calling iter(f) and next(f) automatically.

# ------------------------------------------------------------
# 🧩 Summary:
# ------------------------------------------------------------
# ✅ Any object that supports iter() is iterable.
# ✅ iter() returns an iterator object that remembers its position.
# ✅ Each next() call fetches the next element.
# ✅ When no more data is available, StopIteration is raised.
# ✅ Files are inherently iterable — no need to call iter() explicitly.
