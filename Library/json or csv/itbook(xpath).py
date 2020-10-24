
import pymysql
import numpy as np
from aiohttp import ClientSession
import asyncio
import ssl
from pyquery import PyQuery as pq


class BookSpider(object):
    def __init__(self):
        self.base_url = 'http://www.allitebooks.org/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }

    async def fetch(self, url):
        async with ClientSession() as session:
            async with session.get(url, ssl=ssl.SSLContext()) as response:
                return await response.text()

    async def get_book_url(self, url):
        async with ClientSession().get(url, ssl=ssl.SSLContext()) as response:
            html = await response.text()
        doc = pq(html)
        book_list = doc('article').items()

        # 解析出总页数
        pages = doc('.pages').text().split(' ')
        total = int(pages[2])
        current = int(pages[0])
        # 解析出每本书的url
        for book in book_list:
            book_url = book('.entry-title a').attr('href')
            yield book_url, total, current

    async def parse_detail(self, html):
        doc = pq(html)
        table = doc('.book-detail')
        info_dict = {}
        book_name = doc('.entry-header h1').text()
        info_dict['book_name'] = book_name
        # 处理dl列表标签内的文本
        book_info = table.text().split('\n')
        title = np.array(book_info[::2])
        value = np.array(book_info[1::2])
        str_join = list(np.char.add(title, value))
        for item in str_join:
            k = item.split(':')[0]
            v = item.split(':')[-1]
            info_dict[k] = v

        # 处理书本描述的文本
        book_des = doc('.entry-content').text()
        info_dict['book_des'] = book_des

        yield info_dict

    async def main(self):

        tasks = [asyncio.ensure_future(self.fetch(url)) for url in self.get_book_url(self.base_url)]
        page = 0
        while True:
            page += 1
            url = self.base_url.format(str(page))
            start_html = await self.fetch(url)
            parse = self.get_book_url(start_html)
            print(f'爬取完成：{url}')
            for i in parse:
                book_url = i[0]
                self.parse_detail(book_url)

                total_pages = i[1]
                current_pages = i[2]
                if total_pages >= current_pages:
                    continue
                else:
                    print('全部爬取完成')
                    break


if __name__ == '__main__':
    asyncio.run(BookSpider().main())



