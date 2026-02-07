"""
================================================================================
MULTIPLE PROCESSES IN A LOOP — multiprocessing.Process
================================================================================

This example demonstrates how to run **multiple tasks concurrently** using
Python's multiprocessing module in a loop.

Key ideas:
----------
✔ Multiple processes can run in parallel
✔ Speedup is visible for I/O-bound or sleep-simulated CPU-bound tasks
✔ join() ensures the parent waits for all child processes
✔ Operating system manages process scheduling across available cores
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
    - Create multiple child processes in a loop
    - Start each process
    - Append to a list for later join
    - Wait for all child processes to complete
    """
    
    processes = []

    # --------------------------------------------------------------------------
    # CREATE AND START PROCESSES
    # --------------------------------------------------------------------------
    for i in range(1, 10 + 1):
        p = multiprocessing.Process(target=do_something, args=(1, i))
        p.start()
        processes.append(p)

    # --------------------------------------------------------------------------
    # WAIT FOR CHILD PROCESSES TO FINISH
    # --------------------------------------------------------------------------
    for process in processes:
        process.join()

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
Process 2: Sleeping 1 second(s)...
Process 1: Sleeping 1 second(s)...
Process 3: Sleeping 1 second(s)...
...
Process 1: Done...
Process 2: Done...
Process 3: Done...
Finished in: ~1.11 seconds
"""


# ==============================================================================
# KEY OBSERVATIONS
# ==============================================================================

"""
1. Speedup:
   - Instead of 10 seconds sequentially (10 tasks × 1s each)
   - Total time ≈ 1 second due to concurrent execution

2. OS-level process scheduling:
   - Even if the machine has fewer cores than processes
   - OS switches between processes efficiently

3. join() is critical:
   - Without join(), parent may finish before children
   - Timing and proper synchronization would be wrong
"""
