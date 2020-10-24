import asyncio
import requests
from aiohttp import ClientSession
import ssl
from pyquery import PyQuery as pq


headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                         'likeGecko)Chrome/83.0.4103.116Safari/537.36'}


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def parse(html):

    doc = pq(html)
    for i in doc('article').items():
        title = i('.entry-title').text()
        author = i('.entry-author').text()
        book_url = i('.entry-title a').attr('href')
        print(title, author, book_url)


async def download(url):
    async with ClientSession() as session:
        html = await fetch(session, url)
        await parse(html)


if __name__ == '__main__':

    urls = ['http://www.allitebooks.com/page/{}/'.format(i) for i in range(1, 10)]
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(download(url)) for url in urls]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)


