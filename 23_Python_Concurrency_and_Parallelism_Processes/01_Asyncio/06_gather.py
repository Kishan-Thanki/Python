"""
================================================================================
GATHER — CONCURRENT EXECUTION + RESULT COLLECTION
================================================================================
"""

import asyncio


async def fetch(id: int, delay: int) -> str:
    await asyncio.sleep(delay)
    return f"Data-{id}"


async def main() -> None:
    results = await asyncio.gather(
        fetch(1, 2),
        fetch(2, 1),
        fetch(3, 3),
    )

    print(results)


asyncio.run(main())


# ⚠️ Note: gather has weak error handling