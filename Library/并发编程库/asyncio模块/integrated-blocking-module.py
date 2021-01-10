"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/7
"""
# 在线程中集成阻塞io，例如：pymysql，requests，等
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def blocking_io():
    with open('gather-usage.py', 'r') as f:
        return f.read(100)


def cpu_bound():
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()
    # 1
    result = await loop.run_in_executor(
        None, blocking_io)
    print('default thread pool', result)
    # 2
    with ThreadPoolExecutor() as thread_pool:
        result = await loop.run_in_executor(
            thread_pool, blocking_io)
        print('custom thread pool', result)
    # 3
    with ProcessPoolExecutor() as process_pool:
        result = await loop.run_in_executor(
            process_pool, cpu_bound)
        print('custom process pool', result)


if __name__ == '__main__':
    asyncio.run(main())
