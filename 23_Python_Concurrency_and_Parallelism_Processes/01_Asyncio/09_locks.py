"""
================================================================================
LOCKS — PROTECT SHARED STATE
================================================================================
"""

import asyncio

counter = 0
lock = asyncio.Lock()


async def increment() -> None:
    global counter
    async with lock:
        temp = counter
        await asyncio.sleep(1)
        counter = temp + 1
        print(counter)


async def main() -> None:
    await asyncio.gather(*(increment() for _ in range(5)))


asyncio.run(main())
