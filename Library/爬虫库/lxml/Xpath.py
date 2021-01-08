from lxml import etree
import requests


url = 'http://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


data = requests.get(url, headers=headers).content.decode()
# 1.转解析类型
xpath_data = etree.HTML(data)

# 2.调用xpath方法
news_tag = xpath_data.xpath('//a[@target]/text()')
url_list = xpath_data.xpath('//a[@target]/@href')

data_list = []

for index, tag in enumerate(news_tag):
    news_dict = {tag: url_list[index]}
    # news_tuple = (tag, url_list[index])
    data_list.append(news_dict)
print(data_list)
