"""
================================================================================
INTRODUCTION TO MULTIPROCESSING — multiprocessing.Process
================================================================================

This example demonstrates WHY multiprocessing exists and HOW it differs from
threading.

Key idea:
---------
✔ Threads share the same process (limited by GIL for CPU-bound work)
✔ Processes run in separate memory spaces
✔ Multiprocessing enables TRUE parallelism on multiple CPU cores

================================================================================
WHY USE MULTIPROCESSING?
================================================================================

We use multiprocessing when:

✔ Tasks are CPU-bound (heavy computation)
✔ We want real parallel execution
✔ GIL becomes a bottleneck
✔ Performance must scale across cores

This example intentionally starts SIMPLE:
- Just sleeping
- Just two processes
- Focus on *process lifecycle*, not performance yet

================================================================================
"""

import time
import multiprocessing


# ------------------------------------------------------------------------------
# GLOBAL TIMER (PARENT PROCESS ONLY)
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# TASK FUNCTION (RUNS IN CHILD PROCESSES)
# ------------------------------------------------------------------------------
def do_something(t: int, process: int) -> None:
    """
    Simulates work by sleeping.

    IMPORTANT:
    ----------
    This function runs in a *separate OS process*,
    NOT in the main Python process.
    """
    print(f"Process {process}: Sleeping {t} second(s)...")
    time.sleep(t)
    print(f"Process {process}: Done...")


# ------------------------------------------------------------------------------
# MAIN ENTRY POINT
# ------------------------------------------------------------------------------
def main():
    """
    Parent process logic.

    Responsible for:
    ✔ Creating child processes
    ✔ Starting them
    ✔ Optionally waiting for them
    """

    # --------------------------------------------------------------------------
    # CREATE PROCESSES (NOT STARTED YET)
    # --------------------------------------------------------------------------
    p1 = multiprocessing.Process(target=do_something, args=(1, 1))
    p2 = multiprocessing.Process(target=do_something, args=(1, 2))

    # --------------------------------------------------------------------------
    # START PROCESSES
    # --------------------------------------------------------------------------
    # At this point:
    # - Child processes are spawned
    # - Parent continues immediately
    # - No waiting happens yet
    # --------------------------------------------------------------------------
    p1.start()
    p2.start()

    # --------------------------------------------------------------------------
    # ❗ IMPORTANT: WITHOUT join()
    # --------------------------------------------------------------------------
    # If we measure time *here*, the parent process:
    # - Does NOT wait for children
    # - Finishes almost instantly
    #
    # This explains output like:
    # Finished in: 0.01 seconds
    #
    # Even though children are STILL running.
    # --------------------------------------------------------------------------
    finished = time.perf_counter()
    print(f"Finished in: {round(finished - start, 2)} seconds")


# ------------------------------------------------------------------------------
# REQUIRED GUARD FOR MULTIPROCESSING
# ------------------------------------------------------------------------------
# On Windows & macOS (spawn mode):
# - Prevents infinite child process spawning
# - MUST be used with multiprocessing
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
WHY DID THE PROGRAM FINISH IN ~0.01 SECONDS?

Because:
✔ Parent process does NOT wait by default
✔ Child processes run independently
✔ Timing measured ONLY the parent
"""


"""
WHY DID do_something() STILL RUN?

Because:
✔ Child processes were started correctly
✔ OS scheduled them independently
✔ Output appears after parent timing
"""


"""
WHAT FIXES THIS?

Calling:
✔ p1.join()
✔ p2.join()

This forces the parent to WAIT.
"""


"""
THREADING VS MULTIPROCESSING (CORE DIFFERENCE)

Threading:
✔ Shared memory
✔ Same process
✔ Limited by GIL (CPU-bound)

Multiprocessing:
✔ Separate memory
✔ Separate processes
✔ True parallelism
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ multiprocessing.Process creates OS-level processes
✔ start() launches child execution
✔ join() is REQUIRED for correct synchronization
✔ Parent and child lifecycles are independent
✔ This model enables real CPU parallelism
"""
