"""
@Author: Jonescyna
@Created: 2020/12/28
"""

import re
import time

import requests
from bs4 import BeautifulSoup
from lxml import etree
from pyquery import PyQuery as pq


def cal_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f'{func.__name__}:{time.time() - start}s')
        return ret

    return inner


base_url = 'https://www.amazon.cn/b/ref=s9_acss_bw_cg_pccateg_2a1_w?node=106200071&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=PQNKPPABQXAWCTZSNFXA&pf_rd_t=101&pf_rd_p=cdcd9a0d-d7cf-4dab-80db-2b7d63266973&pf_rd_i=42689071'


def get(url):
    headers = {
        "User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    }

    resp = requests.get(url, headers=headers)
    return resp.text


@cal_time
def parse_by_pq(html):
    for _ in range(50):
        doc = pq(html)

        h2_list = doc('h2').items()
        for h2 in h2_list:
            h2.text()


@cal_time
def parse_by_xpath(html):
    for _ in range(50):
        parser = etree.HTMLParser(recover=True)
        doc = etree.HTML(html, parser)
        h2_list = doc.xpath('//h2')
        for h2 in h2_list:
            title = h2.xpath('./text()')[0]


@cal_time
def parse_by_bs4(html):
    for _ in range(50):
        soup = BeautifulSoup(html, 'lxml')
        h2_list = soup.find_all('h2')
        for h2 in h2_list:
            title = h2.text


@cal_time
def parse_by_re(html):
    for _ in range(50):
        h2_list = re.findall(r'<h2 .*>\n(.*)\n<', html)
        for h2 in h2_list:
            title = h2


if __name__ == '__main__':
    resp = get(base_url)
    parse_by_pq(resp)
    parse_by_xpath(resp)
    parse_by_bs4(resp)
    parse_by_re(resp)
