"""
================================================================================
SYNCHRONOUS (BLOCKING) EXECUTION — I/O WAIT PROBLEM DEMONSTRATION
================================================================================

This example demonstrates **synchronous (blocking) execution** in Python and
explains WHY it becomes inefficient for **I/O-bound tasks**.

IMPORTANT:
- This code is NOT wrong
- This code is NOT inefficient for CPU work
- This code becomes inefficient when the program spends time WAITING

This file should be READ line-by-line, not just executed.

================================================================================
WHAT THIS EXAMPLE TEACHES
================================================================================

1. What "blocking" means
2. Why time.sleep() blocks the program
3. How I/O wait wastes CPU time
4. Why total execution time increases linearly
5. The motivation behind threading and AsyncIO

================================================================================
"""

import time


# ------------------------------------------------------------------------------
# START A HIGH-PRECISION TIMER
# ------------------------------------------------------------------------------
# time.perf_counter() gives the most accurate timer available
# for measuring short durations.
#
# We capture the start time BEFORE any work begins.
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# A SIMPLE SYNCHRONOUS (BLOCKING) FUNCTION
# ------------------------------------------------------------------------------
def do_something(t: int) -> None:
    """
    Simulates an I/O-bound operation using time.sleep().

    Parameters:
        t (int): Number of seconds to "wait"

    IMPORTANT CONCEPT:
    ------------------
    time.sleep() BLOCKS the current thread.

    While sleeping:
    - The CPU is NOT doing useful work
    - The program CANNOT execute anything else
    - The thread is stuck waiting

    This is a perfect simulation of:
    - Network calls
    - File I/O
    - Database queries
    """
    print(f"Sleeping {t} second(s)...")

    # --------------------------------------------------------------------------
    # BLOCKING CALL
    # --------------------------------------------------------------------------
    # During this sleep:
    # - The CPU is idle
    # - The program is paused
    # - No other work can happen
    # --------------------------------------------------------------------------
    time.sleep(t)

    print("Done...")


# ==============================================================================
# PROGRAM EXECUTION FLOW (STEP-BY-STEP)
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: First function call
# ------------------------------------------------------------------------------
# What happens:
# 1. Program enters do_something(2)
# 2. It sleeps for 2 seconds
# 3. NOTHING else runs during this time
# 4. After waking up, execution continues
# ------------------------------------------------------------------------------
do_something(2)


# ------------------------------------------------------------------------------
# STEP 2: Second function call
# ------------------------------------------------------------------------------
# This call DOES NOT overlap with the first one.
#
# The program:
# - Waited 2 seconds already
# - Now waits ANOTHER 2 seconds
#
# Total waiting time so far = 4 seconds
# ------------------------------------------------------------------------------
do_something(2)


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
Why is this called SYNCHRONOUS execution?

- Each function call must COMPLETE before the next one starts
- Execution happens strictly TOP to BOTTOM
- No overlap
- No concurrency
- No multitasking

This is also called:
- Blocking execution
- Sequential execution
- Single-threaded execution
"""

"""
CPU vs I/O BOUND TASKS
---------------------

CPU-bound tasks:
- Heavy computation
- Math
- Data processing
- Image processing
- Encryption

I/O-bound tasks:
- Waiting for network responses
- Reading/writing files
- Database queries
- Sleeping (like this example)

KEY PROBLEM:
------------
During I/O-bound tasks, the CPU is doing NOTHING.
It is idle, wasted, and underutilized.
"""

"""
TOTAL EXECUTION TIME ANALYSIS
----------------------------

do_something(2)  -> 2 seconds
do_something(2)  -> 2 seconds
--------------------------------
Total time       -> ~4 seconds

This is EXPECTED behavior.
Nothing is technically wrong here.

But it is NOT optimal for I/O-bound workloads.
"""


# ------------------------------------------------------------------------------
# STOP THE TIMER
# ------------------------------------------------------------------------------
finish = time.perf_counter()


# ------------------------------------------------------------------------------
# PRINT TOTAL EXECUTION TIME
# ------------------------------------------------------------------------------
print(f"Finished in: {round(finish - start, 2)} seconds")


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ Synchronous code blocks the program during I/O waits
✔ time.sleep() simulates real-world I/O blocking
✔ CPU stays idle during blocking calls
✔ Total execution time increases linearly
✔ This model does NOT scale for I/O-heavy applications

This exact problem is what:
- Threading tries to improve
- AsyncIO solves more efficiently
"""
