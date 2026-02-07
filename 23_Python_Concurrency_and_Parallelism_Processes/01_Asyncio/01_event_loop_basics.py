"""
================================================================================
EVENT LOOP — THE HEART OF ASYNCIO
================================================================================

The event loop:
- Schedules tasks
- Pauses tasks at `await`
- Resumes tasks when I/O completes
"""

import asyncio


async def demo_task(name: str, delay: int) -> None:
    print(f"[{name}] started")
    await asyncio.sleep(delay)
    print(f"[{name}] finished")


async def main() -> None:
    print("Event loop started")
    await demo_task("A", 2)
    await demo_task("B", 1)
    print("Event loop finished")


if __name__ == "__main__":
    asyncio.run(main())

# Still sequential — important to notice