"""
================================================================================
MULTIPROCESSING WITH PROCESSPOOLEXECUTOR — concurrent.futures
================================================================================

This example demonstrates how to use Python's
`concurrent.futures.ProcessPoolExecutor` to run tasks in parallel.

Key ideas:
----------
✔ Automatically manages a pool of processes
✔ Suitable for CPU-bound tasks
✔ Futures represent asynchronous results
✔ as_completed() allows iterating results as they finish
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
def do_something(t: int, process: int) -> str:
    """
    Simulates a task by sleeping for `t` seconds.

    Arguments:
    ----------
    t       : int : number of seconds to sleep
    process : int : process ID (for printing)

    Returns:
    --------
    str : completion message
    """
    print(f"Process {process}: Sleeping {t} second(s)...")
    time.sleep(t)
    return f"Process {process}: Done..."


# ------------------------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------------------------
def main():
    """
    Demonstrates using ProcessPoolExecutor:
    - Submits multiple tasks to the process pool
    - Automatically manages pool size based on system hardware
    - Uses as_completed() to print results as they finish
    """

    # Create a process pool and submit tasks
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1, i) for i in range(1, 10 + 1)]

        # Print results as each process finishes
        for future in concurrent.futures.as_completed(results):
            print(future.result())

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
Process 1: Sleeping 1 second(s)...
Process 2: Sleeping 1 second(s)...
Process 3: Sleeping 1 second(s)...
...
Process 1: Done...
Process 2: Done...
...
Finished in: ~2.13 seconds
"""


# ==============================================================================
# KEY OBSERVATIONS
# ==============================================================================

"""
1. Automatic Pool Management:
   - ProcessPoolExecutor decides how many processes to run
   - Prevents oversubscription of CPU cores

2. Speedup:
   - Multiple tasks run in parallel, reducing wall-clock time
   - Total time ≈ number of seconds for the longest batch of simultaneous tasks

3. Futures:
   - Each submitted task returns a Future
   - as_completed() allows handling results as soon as they finish
"""
