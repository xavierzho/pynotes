"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import asyncio


async def get_html(url):
    print(f"start get url:{url}")
    await asyncio.sleep(2)
    print(f"end get url:{url}")


if __name__ == '__main__':
    url = 'www.baidu.com'
    loop = asyncio.get_event_loop()
    tasks = [get_html(url) for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))

