import asyncio

"""自定义异步迭代器（同时也是异步可迭代对象）"""


class Reader(object):
    def __init__(self):
        self.count = 0

    async def readline(self):

        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


# 使用async for 语句前提必须在异步函数里面
async def func():
    obj = Reader()

    async for item in obj:
        print(item)


asyncio.run(func())
