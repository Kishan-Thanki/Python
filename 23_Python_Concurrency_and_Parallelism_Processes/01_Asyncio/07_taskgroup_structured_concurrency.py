"""
================================================================================
TASKGROUP — STRUCTURED CONCURRENCY (Python 3.11+)
================================================================================
"""

import asyncio


async def fetch(id: int, delay: int) -> str:
    await asyncio.sleep(delay)
    return f"Data-{id}"


async def main() -> None:
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, d in [(1, 2), (2, 1), (3, 3)]:
            tasks.append(tg.create_task(fetch(i, d)))

    for task in tasks:
        print(task.result())


asyncio.run(main())

# ✔ Automatic cancellation
# ✔ Clean error propagation