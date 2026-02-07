"""
================================================================================
THREAD POOL EXECUTOR — IMPLICIT JOIN & GRACEFUL SHUTDOWN
================================================================================

This example demonstrates an IMPORTANT but often overlooked behavior of
`ThreadPoolExecutor`:

👉 You do NOT need to manually join threads.

The executor automatically waits for all submitted tasks to complete
before shutting down.

This file should be READ carefully, not just executed.

================================================================================
WHAT THIS EXAMPLE TEACHES
================================================================================

1. Why ThreadPoolExecutor does NOT need join()
2. How the executor context manager works
3. What "graceful shutdown" means
4. Why results are still completed correctly
5. How this concept maps to AsyncIO later

================================================================================
"""

import time
import concurrent.futures


# ------------------------------------------------------------------------------
# START A HIGH-PRECISION TIMER
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# I/O-BOUND TASK (SIMULATED USING sleep)
# ------------------------------------------------------------------------------
def do_something(t: int, thread: int) -> str:
    """
    Simulates an I/O-bound operation.

    Parameters:
        t (int)      : Number of seconds to sleep
        thread (int) : Logical task identifier

    Returns:
        str: Completion message

    IMPORTANT:
    ----------
    This function BLOCKS the worker thread,
    but NOT the main thread or other workers.
    """
    print(f"Thread {thread}: Sleeping {t} second(s)...")
    time.sleep(t)
    return f"Thread {thread}: Done..."


# ------------------------------------------------------------------------------
# THREAD POOL EXECUTION (NO EXPLICIT JOIN)
# ------------------------------------------------------------------------------
# The ThreadPoolExecutor is used as a CONTEXT MANAGER.
#
# This is CRITICAL:
# -----------------
# When execution exits the `with` block:
# ✔ The executor STOPS accepting new tasks
# ✔ The executor WAITS for all submitted tasks to finish
# ✔ All worker threads are cleaned up safely
#
# This behavior acts like an IMPLICIT join().
# ------------------------------------------------------------------------------
with concurrent.futures.ThreadPoolExecutor() as executor:

    # --------------------------------------------------------------------------
    # SUBMIT TASKS
    # --------------------------------------------------------------------------
    futures = [
        executor.submit(do_something, 1, i)
        for i in range(1, 10 + 1)
    ]

    # --------------------------------------------------------------------------
    # PROCESS RESULTS AS THEY COMPLETE
    # --------------------------------------------------------------------------
    # Note:
    # -----
    # Even if we REMOVE this loop entirely,
    # the executor will STILL wait for all tasks
    # before exiting the context manager.
    #
    # This is why the program "gracefully completes"
    # without manual synchronization.
    # --------------------------------------------------------------------------
    for future in concurrent.futures.as_completed(futures):
        print(future.result())


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
Example output:

Thread 1: Sleeping 1 second(s)...
Thread 2: Sleeping 1 second(s)...
...
Thread 10: Sleeping 1 second(s)...

Thread 4: Done...
Thread 6: Done...
Thread 1: Done...
Thread 3: Done...
Thread 8: Done...
Thread 7: Done...
Thread 9: Done...
Thread 5: Done...
Thread 2: Done...
Thread 10: Done...

Finished in: ~1.0 seconds
"""


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
WHY DOES THIS WORK WITHOUT join()?

Because:
✔ The ThreadPoolExecutor manages thread lifecycle
✔ Exiting the `with` block triggers a graceful shutdown
✔ shutdown(wait=True) is called internally
✔ The main thread waits automatically

This is STRUCTURED concurrency.
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ ThreadPoolExecutor removes manual join()
✔ Context manager guarantees task completion
✔ Futures still represent pending results
✔ This model is safer than raw threading
✔ This idea directly maps to:
  - asyncio.TaskGroup
  - structured concurrency in AsyncIO
"""
