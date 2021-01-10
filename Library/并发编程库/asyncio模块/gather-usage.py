import asyncio


async def a(t):
    print('-->', t)
    await asyncio.sleep(0.5)
    print(t, '<--')
    return t * 10


async def main():
    tasks = [asyncio.create_task(a(t)) for t in range(10)]
    ret = await asyncio.gather(*tasks)
    print(ret)  # 返回的是结果列表


if __name__ == '__main__':
    asyncio.run(main())
