from bs4 import BeautifulSoup
import requests
import re
import bs4

r = requests.get("https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306")
r.raise_for_status()
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text, "html.parser")

"""
1.<>.find_all(name,attrs,recursive,string,**kwargs)
# 返回一个列表类型，存储查找的结果
name：对标签名称的检索字符串
attrs：对标签属性值得检索字符串，可标注属性检索
recursive：是否对子孙全部检索，默认True
string：<>...</>中字符串进行检索
**kwargs:参考requests库方法手册

2.<>.find()
# 搜索且只返回一个结果，字符串类型，同.find_all()参数

3.<>.find_parents()
# 在先辈节点中搜索，返回列表类型，同.find_all()参数

4.<>.find_parent()
# 在先辈节点中返回一个结果，返回字符串类型，同.find_all()参数

5.<>.find_next_siblings()
# 在后续平行节点中搜索，返回列表类型，同.find_all()参数

6.<>.find_next_sibling()
# 在后续平行节点中返回一个结果，返回字符串类型，同.find_all()参数

7.<>.find_previous_siblings()
# 在前序平行节点中搜，返回列表类型，同.find_all()参数

8.<>.find_previous_sibling()
# 在前序平行节点中返回一个结果，返回字符串类型，同.find_all()参数

"""


# print(soup.find_all(['a', 'b']))
# print(soup.find_all('p', 'course'))  # 返回p标签，course字符串的列表


# for tag in soup.find_all(re.compile('b')):  # 所有包含b标签的内容
#     print(tag)


# print(soup.find_all(id=re.compile('link')))  # 返回所有有关link字符串的列表
# print(soup.find_all('a', recursive=False))   # 返回[]表示儿子层面字符串没有’a'标签

# print(soup.find_all(string=re.compile('Python')))



