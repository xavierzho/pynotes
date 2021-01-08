"""
百度的关键词接口：
http：//www.baidu.com/s?wd=keyword

350的关键词接口：
http：//www.so.com/s?q=keyword
"""

import requests

url = "https://www.baidu.com/"
proxy = {'http': '202.109.168.190:45131',
         'https': '202.109.168.190:45131'
         }
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

kv = {'wd': 'python'}
r = requests.get(url, params=kv, headers=headers, proxies=proxy, timeout=30)
r.raise_for_status()

print(r.status_code)
