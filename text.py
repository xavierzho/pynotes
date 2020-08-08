import requests
from lxml import etree
import re


class AreaCodesSpider(object):
    def __init__(self):
        self.url_list = []
        self.data_list = []

    def send_requset(self, url):
        try:
            headers = {
                'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
            }
            # proxy = {"http": 'http://121.232.148.167:9000'}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return response.content.decode()

        except requests.RequestException as e:
            print(e)

    def parse_province(self, data):
        parse_data = etree.HTML(data)
        province_list = parse_data.xpath('//*[@id="main_content"]/table//tr/td[1]/a/@href')
        length = len(province_list)-1
        print(length)
        for i in range(length):
            province = {'area': parse_data.xpath('//*[@id="main_content"]/table//tr/td[1]/a/text()')[i+1],
                        "area_code":
                            parse_data.xpath('//*[@id="main_content"]/table//tr/td[2]/a/text()')[i]
                        }
            self.data_list.append(province)
        return self.data_list

    def parse_city(self, data):
        parse_data = etree.HTML(data)
        city_list = parse_data.xpath('//*[@id="main_content"]/table//tr/td[1]/a/@href')
        length = len(city_list) - 2
        for i in range(length):
            city = {'city': parse_data.xpath('//*[@id="main_content"]/table//tr[4]/td[1]/a/text()'),
                    "city_code": parse_data.xpath('//*[@id="main_content"]/table//tr[4]/td[2]/a/text()')
                    }
        print(city)


    def get_url(self, data_code):
        codes = [item["area_code"] for item in data_code]
        for code in codes:
            url_str = "https://xingzhengquhua.51240.com/"+code+'__xingzhengquhua/'
            self.url_list.append(url_str)
        return self.url_list

    def main(self):
        base_url = "https://xingzhengquhua.51240.com/"
        data_code = self.parse_province(self.send_requset(base_url))
        self.parse_city(self.send_requset(self.get_url(data_code)))



AreaCodesSpider().main()
