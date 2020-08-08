import re
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        response = requests.get(url, timeout=30)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>fraction">(.*?)</i>.*?</dd>',re.S)
#     items = re.findall(pattern, html)
#     print(items)
#


if __name__ == '__main__':
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    # parse_one_page(html)
    print(html)

