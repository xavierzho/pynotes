"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/5
"""
import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                         'likeGecko)Chrome/83.0.4103.116Safari/537.36'}

urls = [f'https://www.cnblogs.com/#p{i}' for i in range(1, 51)]


def craw(url):
    r = requests.get(url, headers=headers)
    # print(url, len(r.text))
    return r.text


def parse(html):
    # class="post-item-text"
    doc = etree.HTML(html)
    titles = doc.xpath('//a[@class="post-item-title"]')
    # print(titles)
    for title in titles:
        text = title.xpath("./text()")[0]
        link = title.xpath("./@href")[0]
        return text, link


if __name__ == '__main__':

    html = craw(urls[1])
    parse(html)