from proxyPool.free_proxies.untils import get_page, get_context
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        # print(name)  # 输出是Crawler
        # print(bases)  # 使出的是(<class 'object'>,)
        # print(attrs)  # 输出打印attrs,查看字典中的值
        count = 0
        attrs['__CrawlFunc__'] = []  # 给子类添加了一个__CrawlFunc__()方法
        for k, v in attrs.items():
            if 'crawl__' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count  # 给子类添加了一个__CrawlFuncCount__()方法
        return type.__new__(mcs, name, bases, attrs)


# 类Crawler的创建时，必须通过ProxyMetaclass的__new__()函数来创建
class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        # 进行动态加载函数名
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_89dl(self, page_count=5):
        """
        获取某代理
        :param page_count: 页码
        :return: 代理
        """
        urls = ['http://www.89ip.cn/index_{}.html'.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_page(url)
            if html:
                doc = pq(html)
                tds = doc('tr:gt(0)').items()
                for td in tds:
                    ip = td.find('td:nth-child(1)').text()
                    port = td.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_goubanjia(self, page_count=6):
        urls = ['https://ip.jiangxianli.com/?page={}'.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_context(url)
            if html:
                doc = pq(html)
                tds = doc('tr:gt(1)').items()
                for td in tds:
                    ip = td.find('td:nth-child(1)').text()
                    port = td.find('td:nth-child(2)').text()
                    yield ":".join([ip, port])

    def crawl_kuaidaili(self, page_count=6):
        urls = ['https://www.kuaidaili.com/free/inha/{}/'.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_page(url)
            if html:
                doc = pq(html)
                tds = doc('tr:gt(0)').items()
                for td in tds:
                    ip = td.find('td:nth-child(1)').text()
                    port = td.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_fengdie(self, page_count=6):
        urls = ['https://www.dieniao.com/FreeProxy/{}.html'.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_context(url)
            if html:
                doc = pq(html)
                tds = doc('div.container div:nth_child(2) ul li:gt(0)').items()
                for td in tds:
                    ip = td.find('span:nth-child(1)').text()
                    port = td.find('span:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_66dl(self, page_count=5):
        urls = ['http://www.66ip.cn/{}.html'.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            html = get_page(url)
            if html:
                doc = pq(html)
                tds = doc('tr:gt(1)').items()
                for td in tds:
                    ip = td.find('td:nth-child(1)').text()
                    port = td.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_eqie(self):
        urls = ['http://ip.yqie.com/ipproxy.htm']
        for url in urls:
            html = get_page(url)
            if html:
                doc = pq(html)
                tds = doc('tr:gt(1)').items()
                for td in tds:
                    ip = td.find('td:nth-child(1)').text()
                    port = td.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_three_one(self):
        urls = ['http://31f.cn/{}-proxy/'.format(page) for page in ['http', 'https', 'socks']]
        for url in urls:
            html = get_context(url)
            if html:
                doc = pq(html)
                tds = doc('tr:gt(0)').items()
                for td in tds:
                    ip = td.find('td:nth-child(2)').text()
                    port = td.find('td:nth-child(3)').text()
                    yield ":".join([ip, port])
