import asyncio


async def func():
    print('来玩游戏啊')
    # 网络IO请求：下载一张图片
    response1 = await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    print("IO 结束", response1)
    response2 = await  asyncio.sleep(2)
    print("IO 结束", response2)


async def main():
    print('start')
    # 网络IO请求：下载一张图片
    response = await func()

    print('end', response)
    # 创建 Task 对象，将当前执行func函数任务添加到事件循环
    task1 = asyncio.create_task(func())

    task2 = asyncio.create_task(func())

    return '返回值'


# 协程对象
# tasks = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]


# # 生成或获取一个时间循环
loop = asyncio.get_event_loop()
# 将任务放到任务列表
loop.run_until_complete(asyncio.wait(main()))  # wait+ 可等待的对象（协程对象，Future，Tsak对象->IO等待）
# asyncio.run(main())  # python3.7up
