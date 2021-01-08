import aiohttp
import asyncio


async def a(t):
    print('-->', t)
    await asyncio.sleep(2)
    print('<--', t)
    return t * 10


async def b():
    cnt = 0
    while 1:
        cnt += 1
        cor = a(cnt)
        resp = loop.create_task(cor)
        await asyncio.sleep(1)
        print(resp)

loop = asyncio.get_event_loop()
loop.run_until_complete(b())

