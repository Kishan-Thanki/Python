"""
Python Standard Library (Must-Know)

This file provides a clean, professional, and structured overview of
essential Python standard library modules that every Python developer
must understand.

The focus is on:
- Core system and utility modules
- Data and algorithm utilities
- Serialization and data exchange

Examples are practical and illustrative.
"""

# ============================================================
# Python Standard Library (Must-Know)
# ============================================================


# ============================================================
# 1. Core Modules
# ============================================================

# ------------------------------------------------------------
# sys
# ------------------------------------------------------------
#
# Provides access to Python runtime environment and interpreter internals.

import sys

print(sys.version)          # Python version
print(sys.platform)         # Platform information
print(sys.argv)             # Command-line arguments
print(sys.path)             # Module search paths
print(sys.getsizeof(10))    # Memory size of object


# ------------------------------------------------------------
# os
# ------------------------------------------------------------
#
# Provides operating system level functionality.

import os

print(os.getcwd())          # Current working directory
print(os.listdir("."))      # List directory contents
print(os.environ.get("HOME"))

# File and directory operations
# os.mkdir("example_dir")
# os.remove("file.txt")


# ------------------------------------------------------------
# pathlib
# ------------------------------------------------------------
#
# Modern, object-oriented filesystem paths (recommended over os.path).

from pathlib import Path

path = Path("example.txt")
path.write_text("Hello from pathlib")
print(path.read_text())
print(path.exists())
print(path.absolute())


# ------------------------------------------------------------
# time
# ------------------------------------------------------------
#
# Provides low-level time-related functions.

import time

start = time.time()
time.sleep(1)
end = time.time()

print("Elapsed time:", end - start)
print(time.ctime())         # Human-readable time


# ------------------------------------------------------------
# datetime
# ------------------------------------------------------------
#
# High-level date and time handling.

from datetime import datetime, date, timedelta

now = datetime.now()
print(now)

today = date.today()
print(today)

future = today + timedelta(days=7)
print(future)


# ------------------------------------------------------------
# math
# ------------------------------------------------------------
#
# Mathematical functions and constants.

import math

print(math.sqrt(16))
print(math.factorial(5))
print(math.pi)
print(math.ceil(4.2))
print(math.floor(4.8))


# ------------------------------------------------------------
# random
# ------------------------------------------------------------
#
# Random number generation.

import random

print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.random())


# ============================================================
# 2. Data and Utilities
# ============================================================

# ------------------------------------------------------------
# itertools
# ------------------------------------------------------------
#
# Efficient looping and iterator building tools.

import itertools

nums = [1, 2, 3]

print(list(itertools.permutations(nums)))
print(list(itertools.combinations(nums, 2)))
print(list(itertools.accumulate(nums)))


# ------------------------------------------------------------
# functools
# ------------------------------------------------------------
#
# Higher-order functions and function tools.

from functools import reduce, lru_cache

print(reduce(lambda a, b: a + b, nums))

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))


# ------------------------------------------------------------
# collections
# ------------------------------------------------------------
#
# Specialized container data types.

from collections import Counter, defaultdict, deque

counter = Counter("mississippi")
print(counter)

default_dict = defaultdict(int)
default_dict["a"] += 1
print(default_dict)

queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
print(queue)


# ------------------------------------------------------------
# heapq
# ------------------------------------------------------------
#
# Heap queue (priority queue) algorithms.

import heapq

heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)
print(heapq.heappop(heap))
heapq.heappush(heap, 2)
print(heap)


# ------------------------------------------------------------
# bisect
# ------------------------------------------------------------
#
# Binary search and sorted list insertion.

import bisect

sorted_list = [1, 3, 4, 7]
bisect.insort(sorted_list, 5)
print(sorted_list)

index = bisect.bisect_left(sorted_list, 4)
print(index)


# ============================================================
# 3. Serialization Modules
# ============================================================

# ------------------------------------------------------------
# json
# ------------------------------------------------------------
#
# Used for data interchange (human-readable).

import json

data = {"name": "Alice", "age": 30}

json_str = json.dumps(data)
print(json_str)

parsed = json.loads(json_str)
print(parsed)


# ------------------------------------------------------------
# pickle
# ------------------------------------------------------------
#
# Python-specific object serialization (not human-readable).

import pickle

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)

# Warning:
# - pickle is unsafe with untrusted data
# - Use only in trusted environments


# ------------------------------------------------------------
# csv
# ------------------------------------------------------------
#
# Reading and writing CSV files.

import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Bob", 25])

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# ============================================================
# 4. Summary
# ============================================================
#
# Core:
# - sys, os, pathlib control environment and filesystem
# - time and datetime manage time and dates
# - math and random support numerical operations
#
# Data and Utilities:
# - itertools for iteration tools
# - functools for functional utilities
# - collections for specialized data structures
# - heapq and bisect for algorithmic efficiency
#
# Serialization:
# - json for interoperable data exchange
# - pickle for Python object persistence
# - csv for tabular data
#
# Mastery of these modules is essential for real-world Python development.
