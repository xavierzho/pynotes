import time
import asyncio
import concurrent.futures


def func1():
    # 某个耗时操作
    time.sleep(2)
    return 'sb'


async def main():
    loop = asyncio.get_running_loop()

    fut = loop.run_in_executor(None, func1)
    result = await fut
    print('default thread pool', result)
