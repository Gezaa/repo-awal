import asyncio
import time

async def count():
    print("Pertama")
    await asyncio.sleep(1)
    print("Kedua")
    await asyncio.sleep(2)
    print("Ketiga")
    await asyncio.sleep(3)
    print("Keempat")
    await asyncio.sleep(4)
    print("Kelima")
async def main():
    await asyncio.gather(count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
