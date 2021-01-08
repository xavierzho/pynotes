import aiohttp
import asyncio


async def a(t):
    print('-->', t)
    await asyncio.sleep(0.5)
    print('<--', t)
    return t * 10


def main():
    futs = [a(t) for t in range(10)]
    print(futs)
    ret = asyncio.gather(*futs)
    print(ret)

    loop = asyncio.get_event_loop()
    ret1 = loop.run_until_complete(ret)
    print(ret1)


main()
