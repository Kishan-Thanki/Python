"""
================================================================================
THREAD SAFETY — USING threading.Lock
================================================================================

Thread safety ensures that shared mutable data is accessed in a controlled
and predictable way when multiple threads run concurrently.

This example demonstrates:
✔ What race conditions are
✔ Why shared state becomes unsafe
✔ How threading.Lock prevents data corruption
✔ Why the GIL does NOT protect logical correctness

================================================================================
WHEN THREAD SAFETY IS REQUIRED
================================================================================

You MUST consider thread safety when:
✔ Multiple threads modify shared variables
✔ Operations are not atomic
✔ Read-modify-write cycles exist
✔ Data consistency matters

================================================================================
IMPORTANT CONCEPTS INTRODUCED
================================================================================

1. Race conditions
2. Critical sections
3. Mutual exclusion (mutex)
4. threading.Lock
5. Context-manager based locking

================================================================================
"""

import threading


# ------------------------------------------------------------------------------
# SHARED STATE (GLOBAL VARIABLE)
# ------------------------------------------------------------------------------
counter = 0


# ------------------------------------------------------------------------------
# LOCK (MUTUAL EXCLUSION MECHANISM)
# ------------------------------------------------------------------------------
# A Lock ensures that only ONE thread can enter
# the critical section at a time.
# ------------------------------------------------------------------------------
lock = threading.Lock()


# ------------------------------------------------------------------------------
# WORKER FUNCTION
# ------------------------------------------------------------------------------
def increment() -> None:
    """
    Safely increments a shared counter.

    Without the lock:
    ✔ Threads interleave operations
    ✔ counter += 1 is NOT atomic
    ✔ Final result becomes unpredictable

    With the lock:
    ✔ Only one thread updates counter at a time
    ✔ Data integrity is preserved
    """
    global counter

    for _ in range(100_000):
        # ----------------------------------------------------------------------
        # CRITICAL SECTION
        # ----------------------------------------------------------------------
        # The code inside this block is protected.
        # Other threads MUST wait until the lock is released.
        # ----------------------------------------------------------------------
        with lock:
            counter += 1


# ------------------------------------------------------------------------------
# THREAD CREATION
# ------------------------------------------------------------------------------
threads = [
    threading.Thread(target=increment),
    threading.Thread(target=increment),
]


# ------------------------------------------------------------------------------
# START THREADS
# ------------------------------------------------------------------------------
for t in threads:
    t.start()


# ------------------------------------------------------------------------------
# WAIT FOR THREADS TO COMPLETE
# ------------------------------------------------------------------------------
for t in threads:
    t.join()


# ------------------------------------------------------------------------------
# FINAL RESULT
# ------------------------------------------------------------------------------
print("Counter value:", counter)


# ==============================================================================
# EXPECTED OUTPUT
# ==============================================================================

"""
Counter value: 200000
"""


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
WHY IS counter += 1 NOT THREAD-SAFE?

Because it expands into:
1. Read counter
2. Increment value
3. Write back result

Threads can interleave between these steps.
"""


"""
WHY DOESN'T THE GIL SAVE US?

Because:
✔ The GIL prevents memory corruption
✔ The GIL does NOT prevent race conditions
✔ Logical correctness is your responsibility
"""


"""
WHAT IS A CRITICAL SECTION?

✔ A block of code accessing shared state
✔ Must be protected by a lock
✔ Only one thread allowed at a time
"""


# ==============================================================================
# WHAT HAPPENS WITHOUT THE LOCK?
# ==============================================================================

"""
If you remove the lock:
✔ Final value varies every run
✔ Lost updates occur
✔ Behavior becomes nondeterministic
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ Thread safety is about correctness, not speed
✔ Locks protect shared mutable state
✔ Use minimal critical sections
✔ The GIL is NOT a substitute for locks
✔ Thread safety is essential in real systems
"""
