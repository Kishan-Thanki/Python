"""
================================================================================
MULTIPROCESSING POOL — multiprocessing.Pool
================================================================================

This example demonstrates how to use `multiprocessing.Pool` to distribute
CPU-bound work across multiple processes.

A Pool:
✔ Manages a fixed number of worker processes
✔ Reuses processes instead of spawning new ones
✔ Simplifies parallel execution with map / apply APIs

This is the **original multiprocessing abstraction** in Python and forms
the conceptual foundation for higher-level executors like:
- concurrent.futures.ProcessPoolExecutor

================================================================================
WHEN TO USE multiprocessing.Pool
================================================================================

Use Pool when:
✔ You need simple parallel mapping of functions
✔ Tasks are CPU-bound
✔ Work can be evenly distributed
✔ You want explicit control over worker count
✔ Backward compatibility matters

================================================================================
IMPORTANT CONCEPTS INTRODUCED
================================================================================

1. Worker process pool
2. CPU core awareness (cpu_count)
3. map() for parallel execution
4. Automatic process lifecycle management
5. GIL avoidance via multiprocessing

================================================================================
"""

from multiprocessing import Pool, cpu_count


# ------------------------------------------------------------------------------
# WORKER FUNCTION (EXECUTED IN CHILD PROCESSES)
# ------------------------------------------------------------------------------
def cube(n: int) -> int:
    """
    Computes the cube of a number.

    This function runs in a SEPARATE PROCESS
    when executed via multiprocessing.Pool.

    Arguments:
    ----------
    n : int

    Returns:
    --------
    int
    """
    return n ** 3


# ------------------------------------------------------------------------------
# MAIN EXECUTION BLOCK
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    """
    Entry point is REQUIRED for multiprocessing.

    On Windows and macOS (spawn mode), child processes
    re-import the main module — without this guard,
    infinite process spawning would occur.
    """

    # --------------------------------------------------------------------------
    # CREATE A PROCESS POOL
    # --------------------------------------------------------------------------
    # cpu_count() returns the number of logical CPU cores
    # Pool(cpu_count()) creates one worker per core
    # --------------------------------------------------------------------------
    with Pool(cpu_count()) as pool:

        # ----------------------------------------------------------------------
        # DISTRIBUTE WORK USING map()
        # ----------------------------------------------------------------------
        # map():
        # ✔ Splits iterable across workers
        # ✔ Executes cube(n) in parallel
        # ✔ Collects results in INPUT ORDER
        # ✔ Blocks until all tasks complete
        # ----------------------------------------------------------------------
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(cube, numbers)

        print(results)


# ==============================================================================
# OBSERVED OUTPUT
# ==============================================================================

"""
[1, 8, 27, 64, 125]
"""


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
WHY USE Pool INSTEAD OF multiprocessing.Process?

✔ No manual process creation
✔ No manual start/join handling
✔ Processes are reused
✔ Cleaner and safer API
"""


"""
HOW MANY PROCESSES SHOULD YOU USE?

✔ cpu_count() is usually optimal for CPU-bound work
✔ Too many processes increase context-switching
✔ Too few underutilize hardware
"""


"""
HOW IS Pool DIFFERENT FROM ProcessPoolExecutor?

✔ Pool is older, lower-level API
✔ ProcessPoolExecutor is higher-level & safer
✔ Executor integrates with Futures
✔ Pool exposes more primitive controls
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ multiprocessing.Pool enables parallel CPU execution
✔ Bypasses the Global Interpreter Lock (GIL)
✔ Best for uniform, CPU-bound workloads
✔ map() preserves order and blocks until completion
✔ Forms the conceptual base of modern executors
"""
