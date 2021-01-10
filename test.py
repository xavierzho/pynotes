
import requests
import execjs
import random
from pyquery import PyQuery as pq


headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                         'likeGecko)Chrome/83.0.4103.116Safari/537.36'}
base_url = 'http://roll.caijing.com.cn/ajax_lists.php?modelid=0&time={random.random()}'

r = requests.get(base_url, headers=headers)
for i in r.json():
    print(i)




