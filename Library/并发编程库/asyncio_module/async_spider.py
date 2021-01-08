"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import asyncio
import aiohttp

from lxml import etree

urls = [f'https://www.cnblogs.com/#p{i}' for i in range(1, 51)]


class BlogSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        self.url = None
        self.pending_queue = asyncio.Queue()
        asyncio.Semaphore(5)

    async def session(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            return session

    async def fetch(self, url, session):
        try:
            async with session.get(url) as response:
                if response.status in [200, 201, 301, 302]:
                    html = await response.text()
                return html
        except Exception as e:
            print(e)

    async def extract_url(self, html):
        """
        生产者，生成待爬取的url
        :param html:
        :return:
        """
        doc = etree.HTML(html.result())
        items = doc.xpath('//div[@class="post-item-text"]/a')
        for item in items:
            link = item.xpath('./@href')[0]
            self.pending_set.add(link)

    async def parse_detail(self):
        """
        消费者,消费待爬取的url
        :return:
        """
        ...

    async def main(self):
        asyncio.gather()
        pass


if __name__ == '__main__':
    spider = BlogSpider()

    spider.url = urls
    asyncio.run(spider.main())
