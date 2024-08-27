# asyncio is a library in python that allows us to run multiple tasks concurrently which helps in improving performance of applications
'''
key concepts:

1. Coroutine : functions defined with async def. building blocks of async programs
2. Tasks : Wrappers around coroutines that can be scheduled to run on the event loop
3. Event loop : starting point of asyncio which runs coroutine until it completes

'''
import asyncio

import my_asyncio

async def fetch_data(delay, name):
    print(f"Start fetching {name}...")
    await asyncio.sleep(delay)
    print(f"Finished fetching {name} after {delay} seconds")
    return f"Data from {name}"

async def main():
    task1 = asyncio.create_task(fetch_data(4, "Site 1"))
    task2 = asyncio.create_task(fetch_data(2, "Site 2"))

    print("Waiting for tasks to complete...")

    # asyncio will fetch task2 first even though we created task1 first
    result1 = await task1
    result2 = await task2

    print("All tasks completed")
    print(result1)
    print(result2)

# Running the event loop
asyncio.run(main())