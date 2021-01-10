import re
import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return url.status_code


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except Exception as e:
        print(e)


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0]), g[1])


def main():
    goods = '笔记本电脑'
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    info_list = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48 * i)
            html = getHTMLText(url)
            parsePage(info_list, html)
        except:
            continue
    printGoodsList(info_list)


main()
