import requests
from lxml import etree

session = requests.Session()
phone_number = 15913101814
password = 'Snq1997.'
data = {'passport': phone_number, 'password': password}
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.105 Safari/537.36'
}
response = session.post('https://passport.mafengwo.cn/login/', headers=header, data=data)
print(response.status_code)
# print(response.text)

url = 'http://www.mafengwo.cn/gonglve/'
r = session.get(url, headers=header)
tree = etree.HTML(r.text)

items = tree.xpath('//div[@class="feed-item _j_feed_item"]')
# print(items)
for item in items:
    title = item.xpath('//div[@class="bar clearfix"]/div[@class="title"]/text()')
    info = item.xpath("//dic[@class='txt']/div[@class='info']/text()")
print(title, info)

