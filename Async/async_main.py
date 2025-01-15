import asyncio
from time import sleep


async def firstFunc():
    print("First Function Running")
    await asyncio.sleep(5); # none blocking delay sim
    print("First Function Finished");
    return 5;

async def secondFunc():
    print("second Function Running")
    await  asyncio.sleep(5);
    print("Second Function Finished");
    return 10;

async def main():
    task1 = asyncio.create_task(firstFunc());
    task2 = asyncio.create_task(secondFunc());
    x = await task1;
    y = await task2;
    print(x);
    print(y);


if __name__ == "__main__":
    asyncio.run(main());


