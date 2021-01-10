import asyncio


# 协程函数
async def print_hello():
    while True:
        print("hello world")
        await asyncio.sleep(1)


async def print_goodbye():
    while True:
        print('goodbye world')
        await asyncio.sleep(2)


# 创建协程对象
co1 = print_hello()
co2 = print_goodbye()
# 获取事件循环
loop = asyncio.get_event_loop()
# 监听时间循环
loop.run_until_complete(asyncio.gather(co1, co2))  # gather将多个协程对象放到一个新的协程函数中交给loop调度
