# 客户端例子

import ssl
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(
        url,
        ssl=ssl.SSLContext()
    ) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://www.sina.com')
        print(html)

# 创建事件循环
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
