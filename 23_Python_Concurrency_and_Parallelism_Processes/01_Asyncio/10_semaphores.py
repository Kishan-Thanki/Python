"""
================================================================================
SEMAPHORES — LIMIT CONCURRENCY
================================================================================
"""

import asyncio


async def access(sem: asyncio.Semaphore, i: int) -> None:
    async with sem:
        print(f"Accessing {i}")
        await asyncio.sleep(1)


async def main() -> None:
    sem = asyncio.Semaphore(2)
    await asyncio.gather(*(access(sem, i) for i in range(5)))


asyncio.run(main())
