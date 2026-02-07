"""
================================================================================
THREADING — I/O-BOUND CONCURRENCY USING MULTIPLE THREADS
================================================================================

This example demonstrates how **threading** helps with **I/O-bound tasks**
by allowing multiple blocking operations to overlap.

IMPORTANT:
- This example does NOT make CPU-heavy code faster
- This example DOES improve I/O-bound performance
- This example explains WHY threading exists

This file should be READ carefully, not just executed.

================================================================================
WHAT THIS EXAMPLE TEACHES
================================================================================

1. How threads run concurrently
2. Why time.sleep() blocks a thread (not the whole program)
3. What happens WITHOUT join()
4. What join() actually does
5. How threading solves the I/O wait problem (partially)

================================================================================
"""

import time
import threading


# ------------------------------------------------------------------------------
# START A HIGH-PRECISION TIMER
# ------------------------------------------------------------------------------
# We measure the total runtime of the program.
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# A BLOCKING I/O SIMULATION FUNCTION
# ------------------------------------------------------------------------------
def do_something(t: int, thread: str) -> None:
    """
    Simulates an I/O-bound operation.

    Parameters:
        t (int)     : Number of seconds to sleep
        thread (str): Human-readable thread identifier

    IMPORTANT CONCEPT:
    ------------------
    time.sleep() BLOCKS the CURRENT THREAD, not the entire process.

    While sleeping:
    - This thread is waiting
    - Other threads CAN run
    - The CPU can switch between threads
    """
    print(f"{thread} Sleeping {t} second(s)...")
    time.sleep(t)
    print(f"{thread} Done...")


# ------------------------------------------------------------------------------
# CREATE THREAD OBJECTS
# ------------------------------------------------------------------------------
# Threads are created but NOT started yet.
#
# At this point:
# - No code inside do_something() has run
# - Threads are just configured
# ------------------------------------------------------------------------------
t1 = threading.Thread(
    target=do_something,
    name="First Thread calling do_something",
    args=(2, "Thread-1"),
)

t2 = threading.Thread(
    target=do_something,
    name="Second Thread calling do_something",
    args=(2, "Thread-2"),
)


# ------------------------------------------------------------------------------
# START THREAD EXECUTION
# ------------------------------------------------------------------------------
# start() tells the OS:
# "Schedule this thread to run"
#
# Both threads begin execution ALMOST at the same time.
# ------------------------------------------------------------------------------
t1.start()
t2.start()


# ------------------------------------------------------------------------------
# WHAT HAPPENS WITHOUT join()
# ------------------------------------------------------------------------------
"""
If we DO NOT call join():

- The main thread continues immediately
- It does NOT wait for worker threads
- The program may finish before threads complete
- This can lead to incorrect timing and premature exit

Example output WITHOUT join():

Thread-1 Sleeping 2 second(s)...
Thread-2 Sleeping 2 second(s)...
Finished in: 0.0 seconds
Thread-1 Done...
Thread-2 Done...
"""


# ------------------------------------------------------------------------------
# WAIT FOR THREADS TO COMPLETE (JOIN)
# ------------------------------------------------------------------------------
# join() BLOCKS the main thread until the target thread finishes.
#
# This ensures:
# - Accurate timing
# - Correct program completion
# ------------------------------------------------------------------------------
t1.join()
t2.join()


# ------------------------------------------------------------------------------
# STOP THE TIMER
# ------------------------------------------------------------------------------
finished = time.perf_counter()


# ------------------------------------------------------------------------------
# PRINT TOTAL EXECUTION TIME
# ------------------------------------------------------------------------------
print(f"Finished in: {round(finished - start, 2)} seconds")


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
EXPECTED OUTPUT WITH join():

Thread-1 Sleeping 2 second(s)...
Thread-2 Sleeping 2 second(s)...
Thread-1 Done...
Thread-2 Done...
Finished in: ~2.0 seconds

WHY ~2 seconds AND NOT ~4 seconds?

Because:
✔ Both threads slept at the SAME TIME
✔ I/O waits overlapped
✔ CPU switched between threads
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ Threading allows overlapping I/O waits
✔ time.sleep() blocks only the calling thread
✔ join() is REQUIRED for correct synchronization
✔ Threading helps I/O-bound tasks
✔ Threading does NOT bypass the GIL for CPU-bound work
"""
