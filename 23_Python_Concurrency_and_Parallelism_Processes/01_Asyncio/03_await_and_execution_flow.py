"""
================================================================================
`await` — PAUSING EXECUTION
================================================================================
"""

import asyncio


async def fetch_data() -> str:
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched")
    return "DATA"


async def main() -> None:
    print("Start main")
    result = await fetch_data()
    print("Result:", result)
    print("End main")


asyncio.run(main())
