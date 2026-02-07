"""
================================================================================
COROUTINES — WHAT `async def` REALLY MEANS
================================================================================
"""

import asyncio


async def my_coroutine() -> None:
    print("Coroutine executing")
    await asyncio.sleep(1)
    print("Coroutine done")


# Calling does NOT execute
coro = my_coroutine()
print("Coroutine object:", coro)

# Execution only happens when awaited
asyncio.run(my_coroutine())
