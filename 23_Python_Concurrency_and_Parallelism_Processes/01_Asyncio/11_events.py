"""
================================================================================
EVENTS — SIMPLE COORDINATION SIGNAL
================================================================================
"""

import asyncio


async def waiter(event: asyncio.Event) -> None:
    print("Waiting...")
    await event.wait()
    print("Event received!")


async def setter(event: asyncio.Event) -> None:
    await asyncio.sleep(2)
    event.set()


async def main() -> None:
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


asyncio.run(main())
