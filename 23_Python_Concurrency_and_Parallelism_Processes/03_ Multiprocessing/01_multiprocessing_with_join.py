"""
================================================================================
BASIC MULTIPROCESSING WITH JOIN — multiprocessing.Process
================================================================================

This example demonstrates how to use Python's multiprocessing module
to run tasks in separate OS-level processes and correctly synchronize
them with the `join()` method.

Key ideas:
----------
✔ Processes run independently from the parent
✔ Parent does not wait unless explicitly told
✔ join() ensures parent waits for children to finish
✔ Useful for CPU-bound or long-running tasks
"""

import time
import multiprocessing


# ------------------------------------------------------------------------------
# GLOBAL TIMER
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# TASK FUNCTION (RUNS IN CHILD PROCESSES)
# ------------------------------------------------------------------------------
def do_something(t: int, process: int) -> None:
    """
    Simulates a task by sleeping for `t` seconds.
    
    Arguments:
    ----------
    t       : int : number of seconds to sleep
    process : int : process ID (for printing)
    
    Notes:
    -----
    Each invocation runs in a separate process.
    """
    print(f"Process {process}: Sleeping {t} second(s)...")
    time.sleep(t)
    print(f"Process {process}: Done...")


# ------------------------------------------------------------------------------
# MAIN ENTRY POINT
# ------------------------------------------------------------------------------
def main():
    """
    Parent process logic:
    - Create child processes
    - Start them
    - Wait for them to complete using join()
    """
    
    # --------------------------------------------------------------------------
    # CREATE PROCESS INSTANCES (NOT STARTED YET)
    # --------------------------------------------------------------------------
    p1 = multiprocessing.Process(target=do_something, args=(1, 1))
    p2 = multiprocessing.Process(target=do_something, args=(1, 2))

    # --------------------------------------------------------------------------
    # START PROCESSES
    # --------------------------------------------------------------------------
    p1.start()
    p2.start()

    # --------------------------------------------------------------------------
    # WAIT FOR CHILD PROCESSES TO FINISH
    # --------------------------------------------------------------------------
    # join() ensures the parent process waits until the child completes.
    p1.join()
    p2.join()

    # --------------------------------------------------------------------------
    # STOP TIMER
    # --------------------------------------------------------------------------
    finished = time.perf_counter()
    print(f"Finished in: {round(finished - start, 2)} seconds")


# ------------------------------------------------------------------------------
# REQUIRED GUARD FOR MULTIPROCESSING
# ------------------------------------------------------------------------------
# Prevents unintended child spawning on Windows/macOS
# --------------------------------------------------------------------------
if __name__ == "__main__":
    main()


# ==============================================================================
# OBSERVED OUTPUT
# ==============================================================================

"""
Process 1: Sleeping 1 second(s)...
Process 2: Sleeping 1 second(s)...
Process 1: Done...
Process 2: Done...
Finished in: ~1.06 seconds
"""


# ==============================================================================
# KEY OBSERVATIONS
# ==============================================================================

"""
1. Without join():
   - Parent finishes almost instantly
   - Child processes still run asynchronously
   - Timing appears wrong (e.g., 0.01 seconds)

2. With join():
   - Parent waits until all child processes finish
   - Timing reflects actual task duration

3. Multiprocessing vs Threading:
   - Threads share memory, limited by GIL for CPU tasks
   - Processes are independent, true parallelism
"""
