"""
================================================================================
TASKS — TRUE CONCURRENCY BEGINS HERE
================================================================================
"""

import asyncio


async def fetch(id: int, delay: int) -> None:
    print(f"Fetching {id}")
    await asyncio.sleep(delay)
    print(f"Fetched {id}")


async def main() -> None:
    t1 = asyncio.create_task(fetch(1, 2))
    t2 = asyncio.create_task(fetch(2, 2))

    await t1
    await t2


asyncio.run(main())

"""
Total time ≈ 2 seconds
Tasks start immediately when scheduled.
"""
