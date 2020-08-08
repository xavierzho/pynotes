"""
百度的关键词接口：
http：//www.baidu.com/s?wd=keyword

350的关键词接口：
http：//www.so.com/s?q=keyword
"""

import requests


url = "https://www.baidu.com/"
try:
    kv = {'wd': 'python'}
    r = requests.get(url, params=kv)
    r.raise_for_status()
# print(r.status_code)
# print(r.request.url)  # 发送给百度的url
    print(len(r.text))
except:
    print("爬取失败")
