"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import asyncio


async def get_html(url):
    print(f"start get url:{url}")
    await asyncio.sleep(2)
    print(f"end get url:{url}")


async def main():
    url = 'www.baidu.com'
    tasks = [get_html(url) for _ in range(10)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
