import asyncio


class AsyncContextManger:
    def __init__(self, conn):
        self.conn = conn

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(1)
        # 异步关闭数据库链接


async def main():
    async with AsyncContextManger() as f:
        result = await f.do_something()
        print(result)

asyncio.run(main())
