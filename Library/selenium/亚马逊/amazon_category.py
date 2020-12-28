"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/23
"""
import requests
from lxml import etree
from urllib.parse import urljoin
import json

url = 'https://www.amazon.cn/gp/site-directory?ie=UTF8&ref_=nav_shopall_btn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
resp = requests.get(url, headers=headers).text
html = etree.HTML(resp)
category_list = html.xpath(
    '//div[starts-with(@id,"cat")][@id!="cat1"][@id!="cat2"]//div[@class="a-row a-spacing-small"]')
category_dict = {}
items = []
for i in category_list:
    category_dict['main_category'] = i.xpath('./span/a/text()')[0]
    category_dict['main_category_link'] = urljoin(url, i.xpath('./span/a/@href')[0])
    category_dict['categories'] = []
    for j in i.xpath('.//li[@class="a-spacing-small"]/span/span'):
        small_category = {
            'category': j.xpath('./a/text()')[0],
            'category_link': urljoin(url, j.xpath('./a/@href')[0])
        }
        category_dict['categories'].append(small_category)

    items.append(category_dict)

data = json.dumps(items)
with open('category_list.json', 'w') as f:
    f.write(data)
