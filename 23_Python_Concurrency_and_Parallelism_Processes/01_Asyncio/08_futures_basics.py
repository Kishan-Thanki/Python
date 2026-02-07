"""
================================================================================
FUTURES — PROMISE OF A RESULT
================================================================================
"""

import asyncio


async def set_future(future: asyncio.Future) -> None:
    await asyncio.sleep(2)
    future.set_result("Future Result")


async def main() -> None:
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.create_task(set_future(future))

    result = await future
    print(result)


asyncio.run(main())

# Usually used by libraries, not user code