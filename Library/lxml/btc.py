import re
import requests


class BtcSpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        self.base_url = "https://webapi.8btc.com/forum/portal-article-title/list?"

    # 发请求
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode()

        return data

    # 解析数据
    def parse_data(self):
        pass
# "https://webapi.8btc.com/forum/portal-article-title/list?page_size=28&"+ page+"&order_by=new"

    # 保存数据
    def save_data(self, data):
        with open('8btc.json', 'w', encoding='utf-8') as f:
            f.write(data)

    # 启动
    def main(self):
        # 1.拼接完整url
        url = self.base_url + 'page=1'
        # 2.发请求
        data = self.get_data(url)
        # 3.做解析

        # 4.保存
        self.save_data(data)


BtcSpider().main()
