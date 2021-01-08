"""
BeaytifulSoup库解析器
bs4的HTML解析器      BeautifulSoup(mk,'html.parser')      pip install bs4
lxml的HTML解析器     BeautifulSoup(mk，’lxml‘)            pip install lxml
lxml的XML解析器      BeautifulSoup(mk,'xml')              pip install lxml
html5lib的解析器     BeautifulSoup(mk,"html5lib")         pip install html5lib

BeautifulSoup 类的基本元素
Tag             标签，最基本的信息组织单元，分别用<></>标明开头和结尾
Name            标签的名字，<p>...</p>的名字是’p‘，格式：<tag>.name
Attributes      标签的属性，字典形式组织，格式：<tag>.attrs
NavigableString 标签内非属性字符串，<>...</>中字符串，格式：<tag>.string
Comment         标签内字符串的注释部分，一种特殊的Comment类型

标签树的下行遍历
.contents：子节点的列表，将<tag>所有儿子节点存入列表
.children：子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
.descendants：子孙节点的迭代类型，包含所有子孙节点，用于循环遍历

标签树的上行遍历
.parent：节点的父亲标签
.parents：节点先辈标签的迭代类型，用于循环遍历先辈节点

标签树的平行遍历
.next_sibling：返回按照HTML文本顺序的下一个平行节点标签
.previous_sibling：返回按照HTML文本顺序的上一个平行节点标签
.next_siblings：迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings：迭代类型，返回按照HTML文本顺序的前续所有平行节点标签

"""
from bs4 import BeautifulSoup  # 解析html信息库
import requests
r = requests.get("http://python123.io/ws/demo.html")
# print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# soup1 = BeautifulSoup("<html>data</html>", 'html.parser')
# soup2 = BeautifulSoup(open("D://"), 'html.parser')

# print(soup.title)  # 返回文本第一个title标签
tag = soup.a
# print(tag.parent.parent.name)  # 父标签的名字
# print(tag.attrs['href'])  # 标签的属性
# print(type(tag.attrs))  # 标签属性类型
# print(type(tag))    # 标签类型
# print(soup.a.string)  # 非属性字符串
# print(soup.p.string)
# print(type(soup.p.string))

"""下行遍历
print(soup.head)
print(soup.head.contents)

print(len(soup.body.contents))
print(soup.body.contents[1])

for child in soup.body.children:  # 遍历儿子节点
    print(child)

for child in soup.body.descendants:  # 遍历子孙节点
    print(child)

"""

# 下行遍历
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)


"""平行遍历"""
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.previous_sibling.previous_sibling)
# print(soup.a.parent)

# for sibling in soup.a.next_siblings:  # 遍历后续节点
#     print(sibling)

# for sibling in soup.a.previous_sibling:  # 遍历谦虚节点
#     print(sibling)

print(soup.a.prettify())  # 使HTML文本更好的展示
