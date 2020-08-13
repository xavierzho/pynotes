import telnetlib
import redis
import urllib.request

from lxml import etree


r = redis.StrictRedis(host='127.0.0.1', port=6379)

scrapeUrls = ['http://www.89ip.cn/index_{}.html'.format(i) for i in range(1, 3)]
for url in scrapeUrls:
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    tree = etree.HTML(html)
    # bsObj = BeautifulSoup(html, 'html.parser')
    data = tree.xpath('//table[@class="layui-table"]/tbody/tr')
    for item in data:
        ip = item.xpath('./td/text()')[0].strip()
        port = item.xpath('./td[2]/text()')[0].strip()
        ip_address = 'http://' + ip + ':' + port

        # 对ip进行验证
        try:
            telnetlib.Telnet(host=ip, port=port, timeout=3)
        except Exception as e:
            print('fail', e)
        else:
            print('success:' + ip_address)
            r.sadd('ippool', ip_address)
