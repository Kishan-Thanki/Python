"""
================================================================================
PROBLEM: ASYNC ≠ CONCURRENT BY DEFAULT
================================================================================
"""

import asyncio


async def fetch(id: int, delay: int) -> None:
    print(f"Fetching {id}")
    await asyncio.sleep(delay)
    print(f"Fetched {id}")


async def main() -> None:
    await fetch(1, 2)
    await fetch(2, 2)


asyncio.run(main())

"""
Total time ≈ 4 seconds
WHY? Each coroutine is awaited sequentially.
"""
