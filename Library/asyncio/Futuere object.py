# asyncio.Future() 对象
# concurrent.futures.Future() 对象（使用线程池、进程池实现异步操作用到的对象）
# task类继承于Future对象，他是一个底层的类，task对象内部await 结果的处理基于Future对象来的
import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('666')


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务（Future对象），这个任务什么都不干
    fut = loop.create_future()
    # 等待任务最终结果（Future对象），没有结果则会一直等下去
    await loop.create_task(set_after(fut))
    data = await fut
    print(data)


asyncio.run(main())
