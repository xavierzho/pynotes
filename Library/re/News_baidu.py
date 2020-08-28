import requests
import re

url = 'http://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
response = requests.get(url, headers=headers)
data = response.content.decode()
"""
 <a href="http://cpc.people.com.cn/xuexi/n1/2020/0719/c385474-31788748.html" target="_blank" class="a3 
md-opjjpmhoiojifppkkcdabiobhakljdgm_doc" mon="ct=1&amp;a=1&amp;c=top&amp;pn=0">治国理政，习近平为何强调运用辩证思维</a> 
"""
pattern = re.compile('<a href="(.*?)" target="_blank".*?mon=".*?">(.*)</a>')
result = pattern.findall(data)
for new in result:
    print(new)

