"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/5
"""
# 该爬虫使用的是广度优先策略
import aiohttp
import asyncio
import re
import aiomysql
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.116Safari/537.36'
}

base_url = "https://www.cnblogs.com/"

sem = asyncio.Semaphore(5)
seen_urls = set()
queue = asyncio.Queue()
stopping = False


async def fetch(session, url):
    async with sem:
        async with session.get(url, headers=headers) as resp:
            suffix = resp.url.path.split('.')[-1]
            if suffix.lower() in ['jpg', 'gif', 'png', 'jpeg', 'pdf']:
                return await resp.content.read()
            else:
                return await resp.text()


async def extract_url(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session=session, url=url)
        doc = etree.HTML(html)
        links = doc.xpath('//a/@href')
        for link in links:
            if re.match(r'.*cnblogs\.com/.*/p/\d+\.html', link):
                print(queue.put_nowait(link))


def parse_article(html):
    doc = etree.HTML(html)
    title = doc.xpath('//h1[@class="postTitle"]/a/span/text()')
    return title


async def article_handler(url, session, pool):
    # 获取文章详情，并解析入库
    html = await fetch(url, session)

    title = parse_article(html)
    print(title)

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into article(title) values('{}') ".format(title)
            await cur.execute(insert_sql)
    seen_urls.add(url)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:

        while not stopping:
            if not queue.empty():
                url = queue.get_nowait()
                if url not in seen_urls:
                    loop.create_task(article_handler(url, session, pool))


async def main():
    global stopping
    page = 10
    # 等待mysql链接建立
    pool = await aiomysql.create_pool(host="127.0.0.1", port=3306,
                                      user='root', password='1997',
                                      db='aiomysql_test', loop=loop,
                                      # charset="utf-8", autocommit=True
                                      )
    url = base_url + 'sitehome/p/{}'
    tasks = [loop.create_task(extract_url(url.format(i))) for i in range(page, 1, -1)]
    await asyncio.gather(*tasks)
    # print('爬取完成：', url)

    loop.create_task(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
