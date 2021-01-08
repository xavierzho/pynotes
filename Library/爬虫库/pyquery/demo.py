import requests
from pyquery import PyQuery as pq

headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                         'likeGecko)Chrome/83.0.4103.116Safari/537.36'}

url = 'http://news.baidu.com/'
r = requests.get(url, headers=headers)
if r.status_code == 200:
    doc = pq(r.text)
    # 1.id 选择器# id值
    # print(doc('#pane-news'))
    # 2.类选择器 tag.class="?"
    # 3.通过text()获取文本，attr('类名')获取属性
    # 4.需要遍历则用items()方法
    # 5.通过一个空格缩进来表示子孙节点  类似与xpath 里面的//
    # 6.注意类名不能有空格，有空格
    # lis = doc('div.hotnews').items()
    # 7. parents():相当于从头开始到该节点的内容 parent()： siblings():兄弟节点（同级节点），但是不包括自己
    # 8.伪类选择器 nth-child() first-child() last-child() lt() gt()
    #
    lis = doc('div.hotnews li:lt(2)')
    print(lis)

    # for li in lis:
    #     print(li.text())
