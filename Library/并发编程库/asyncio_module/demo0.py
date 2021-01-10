"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/9
"""
import asyncio
import re
import aiohttp
import aiomysql
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.116Safari/537.36'
}

base_url = "https://www.cnblogs.com/sitehome/p/{}"

seen_urls = set()
queue = []


async def fetch(url, session):
    async with session.get(url) as resp:
        print(resp.url)
        return await resp.text()


async def extract_urls(url, session):
    html = await fetch(url, session)
    if isinstance(html, str):
        doc = etree.HTML(html)
        links = doc.xpath('//a/@href')
        for link in links:
            if re.match(r'^h.*cnblogs\.com/.*/p/\d+\.html$', link):
                if link not in seen_urls:
                    queue.append(link)
                    # print(link)
                else:
                    pass


async def article_handler(session, pool):
    while len(queue) > 0:
        url = queue.pop()
        html = await fetch(url, session)
        doc = etree.HTML(html)
        title = doc.xpath('//div[@class="postTitle"]//text()')[0]
        print(title)
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                insert_sql = "insert into article(title) values('{}') ".format(title)
                await cur.execute(insert_sql)
                seen_urls.add(url)


async def main():
    pool = await aiomysql.create_pool(host="localhost", port=3306,
                                      user='root', password='1997',
                                      db='aiomysql_test', loop=asyncio.get_event_loop(),
                                      charset="utf8", autocommit=True
                                      )

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [asyncio.create_task(extract_urls(base_url.format(page), session)) for page in range(10, 0, -1)]
        tasks2 = asyncio.create_task(article_handler(session, pool))
        await asyncio.gather(*tasks)
        await tasks2
    # print(pending_url)

if __name__ == '__main__':
    asyncio.run(main())
