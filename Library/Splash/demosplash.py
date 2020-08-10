# http://localhost:8050/info?wait=0.5&images=1&expand=1&timeout=90.0&url=http%3A%2F%2Fwww.baidu.com&lua_source=function+main%28splash%2C+args%29%0D%0A++assert%28splash%3Ago%28args.url%29%29%0D%0A++assert%28splash%3Await%280.5%29%29%0D%0A++return+%7B%0D%0A++++html+%3D+splash%3Ahtml%28%29%2C%0D%0A++++png+%3D+splash%3Apng%28%29%2C%0D%0A++++har+%3D+splash%3Ahar%28%29%2C%0D%0A++%7D%0D%0Aend
# curl 'http://localhost:8050/render.html?url=http://www.toutiao.com&timeout=30&wait=0.5'
# splash启动命令
# sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
import time
import requests
import csv
from lxml import etree

fw = open('douban_comments.csv', 'w')
writer = csv.writer(fw)
writer.writerow(['comment_time', 'comment_content'])

try:
    for i in range(2):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        url = 'http://localhost:8050/render.html?url=https://movie.douban.com/subject/26608230/comments?start={}&limit=20&sort=new_score&status=P'.format(i*20)

        response = requests.get(url, headers=headers)
        # print(response.text)
        tree = etree.HTML(response.text)

        comments = tree.xpath('//div[@class="comment"]/')

        for item in comments:
            comment_time = item.xpath('./h3/span[3]/span[contains(@class,"comment-time")]/@title')[0]
            comment_time = int(time.mktime(time.strptime(comment_time, '%Y-%m-%d %H:%M:%S')))
            comment_content = item.xpath('./p/span/text()')[0].strip()
            print(comment_time)
            print(comment_content)
            # writer.writerow([comment_time, comment_content])
except Exception as e:
    print(e)
