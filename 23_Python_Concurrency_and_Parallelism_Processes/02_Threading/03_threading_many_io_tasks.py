"""
================================================================================
THREADING — SCALING I/O-BOUND WORK WITH MULTIPLE THREADS
================================================================================

This example demonstrates how **threading scales I/O-bound workloads**
by running MANY blocking operations concurrently.

We intentionally create MULTIPLE threads to show:
- How I/O waits overlap
- Why execution time does NOT grow linearly
- Why output order becomes NON-DETERMINISTIC

This file should be READ carefully, not just executed.

================================================================================
WHAT THIS EXAMPLE TEACHES
================================================================================

1. Creating many threads dynamically
2. Why threads finish in unpredictable order
3. How join() ensures correctness
4. Why total runtime ≈ longest I/O wait
5. The scalability limits of threading

================================================================================
"""

import time
import threading


# ------------------------------------------------------------------------------
# START A HIGH-PRECISION TIMER
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# I/O-BOUND TASK (SIMULATED USING sleep)
# ------------------------------------------------------------------------------
def do_something(t: int, thread: int) -> None:
    """
    Simulates an I/O-bound operation.

    Parameters:
        t (int)      : Number of seconds to sleep
        thread (int) : Logical thread identifier

    IMPORTANT CONCEPT:
    ------------------
    - time.sleep() blocks ONLY the current thread
    - Other threads are free to run
    - Output order is NOT guaranteed
    """
    print(f"{thread} Sleeping {t} second(s)...")
    time.sleep(t)
    print(f"{thread} Done...")


# ------------------------------------------------------------------------------
# CREATE AND START MULTIPLE THREADS
# ------------------------------------------------------------------------------
# We will create 10 threads, each performing an I/O wait of 1 second.
#
# Key idea:
# - All threads start almost immediately
# - All threads sleep at the SAME TIME
# ------------------------------------------------------------------------------
threads = []

for i in range(1, 10 + 1):
    t = threading.Thread(
        target=do_something,
        name=f"Thread-{i}",
        args=(1, i),
    )
    t.start()
    threads.append(t)


# ------------------------------------------------------------------------------
# WAIT FOR ALL THREADS TO COMPLETE
# ------------------------------------------------------------------------------
# join() ensures:
# - The main thread waits
# - Execution time is measured correctly
# - The program does NOT exit early
# ------------------------------------------------------------------------------
for thread in threads:
    thread.join()


# ------------------------------------------------------------------------------
# STOP THE TIMER
# ------------------------------------------------------------------------------
finished = time.perf_counter()


# ------------------------------------------------------------------------------
# PRINT TOTAL EXECUTION TIME
# ------------------------------------------------------------------------------
print(f"Finished in: {round(finished - start, 2)} seconds")


# ==============================================================================
# EXPECTED OUTPUT (ORDER MAY VARY)
# ==============================================================================

"""
Example output (order NOT guaranteed):

1 Sleeping 1 second(s)...
2 Sleeping 1 second(s)...
3 Sleeping 1 second(s)...
...
10 Sleeping 1 second(s)...

1 Done...
3 Done...
2 Done...
7 Done...
10 Done...
6 Done...
5 Done...
4 Done...
9 Done...
8 Done...

Finished in: ~1.0 seconds
"""


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
WHY DOES THIS FINISH IN ~1 SECOND AND NOT ~10 SECONDS?

Because:
✔ All threads sleep concurrently
✔ I/O waits overlap
✔ CPU switches between threads
✔ Only the LONGEST sleep matters

WHY IS THE OUTPUT ORDER RANDOM?

Because:
✔ Threads are scheduled by the OS
✔ No guarantee which thread resumes first
✔ Concurrency ≠ deterministic order
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ Threading scales well for I/O-bound workloads
✔ Output order becomes non-deterministic
✔ join() is REQUIRED for correctness
✔ Threads overlap waiting time, not CPU work
✔ Creating too many threads has overhead
"""
