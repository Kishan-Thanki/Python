"""
================================================================================
MULTIPROCESSING WITH PROCESSPOOLEXECUTOR.map — concurrent.futures
================================================================================

This example demonstrates using Python's `ProcessPoolExecutor.map()` to run
multiple CPU-bound or I/O-bound tasks in parallel.

Key points:
-----------
✔ map() automatically distributes tasks across processes
✔ Blocks until all results are ready
✔ Returns results in submission order
✔ Simplifies code compared to manually submitting futures
"""

import time
import concurrent.futures


# ------------------------------------------------------------------------------
# GLOBAL TIMER
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# TASK FUNCTION
# ------------------------------------------------------------------------------
def do_something(t: int) -> str:
    """
    Simulates a task by sleeping for `t` seconds.

    Arguments:
    ----------
    t : int : number of seconds to sleep

    Returns:
    --------
    str : completion message
    """
    print(f"Sleeping {t} second(s)...")
    time.sleep(t)
    return "Done..."


# ------------------------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------------------------
def main():
    """
    Demonstrates using ProcessPoolExecutor.map:
    - Automatically schedules multiple tasks
    - Collects results in submission order
    - Blocks until all tasks are complete
    """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit multiple tasks with map()
        results = executor.map(do_something, [1, 2, 3, 4, 5])

        # Print results as they are returned (in order of submission)
        for result in results:
            print(result)

    # Stop timer
    finished = time.perf_counter()
    print(f"Finished in: {round(finished - start, 2)} seconds")


# ------------------------------------------------------------------------------
# REQUIRED GUARD FOR MULTIPROCESSING
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


# ==============================================================================
# OBSERVED OUTPUT EXAMPLE
# ==============================================================================

"""
Sleeping 1 second(s)...
Sleeping 2 second(s)...
Sleeping 3 second(s)...
Sleeping 4 second(s)...
Sleeping 5 second(s)...
Done...
Done...
Done...
Done...
Done...
Finished in: ~5.12 seconds
"""


# ==============================================================================
# KEY OBSERVATIONS
# ==============================================================================

"""
1. map() vs submit():
   - map() is simpler for multiple tasks
   - Returns results in the order tasks were submitted
   - submit() + as_completed() allows handling results as soon as they finish

2. Concurrency:
   - Tasks run in parallel, reducing wall-clock time
   - Total time ≈ longest task among simultaneously running tasks

3. ProcessPoolExecutor:
   - Automatically manages the number of processes
   - Optimizes usage of CPU cores
"""
