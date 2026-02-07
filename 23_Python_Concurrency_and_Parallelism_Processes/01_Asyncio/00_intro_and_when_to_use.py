"""
================================================================================
ASYNCIO — INTRODUCTION & WHEN TO USE IT
================================================================================

AsyncIO is about handling WAITING efficiently.

It does NOT:
❌ Make CPU-heavy tasks faster
❌ Use multiple CPU cores

It DOES:
✔ Eliminate idle waiting
✔ Handle thousands of I/O tasks efficiently
✔ Improve responsiveness
"""

"""
WHEN TO USE ASYNCIO
-------------------
✔ Network calls
✔ Disk I/O
✔ Database queries
✔ Timers / sleep
✔ High-concurrency servers

WHEN NOT TO USE
---------------
❌ CPU-bound computation
❌ Heavy numerical processing
"""

print("AsyncIO is about efficient waiting, not raw speed.")
