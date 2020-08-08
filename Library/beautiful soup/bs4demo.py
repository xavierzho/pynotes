from bs4 import BeautifulSoup

html_doc = """
<html><head><title id='one'><b>The Dormouse's story</b></title></head>
<body>
<p class="story"><!----></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 1.转类型 bs4.BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Tag标签对象 bs4.element.Tag
result = soup.head
result1 = soup.a
result2 = soup.p
print('Tag标签对象:{}'.format(result1))
print('Tag标签对象类型:{}'.format(type(result1)))

# 内容 bs4.element.NavigableString
result3 = soup.a.string
print('内容:{}'.format(result3))
print('内容对象类型:{}'.format(type(result3)))

# 属性 str
result4 = soup.a['class']
print('属性:{}'.format(result4))
print('属性对象的类型:{}'.format(type(result4)))

# 注释内容 bs4.element.comment
result5 = soup.p.string
print('注释内容:{}'.format(result5))
print('注释内容对象的类型:{}'.format(type(result5)))

# 2.通用解析方法

# find 返回符合查询条件的第一个标签
result6 = soup.find(name='a')
result7 = soup.find(attrs={'class': "title"})
result8 = soup.find(name='p', attrs={'class': "story"})
print("a标签中的第一个:{}".format(result6))
print("查询条件中的第一个:{}".format(result8))

# find_all list[标签对象]
result9 = soup.find_all('a')
result10 = soup.find_all('a', attrs={'class': "sister"})
print('查询标签列表:{}'.format(result9))

# select_one --css选择器
result11 = soup.select_one('.sister')
# select--css选择器
result12 = soup.select('.sister')  # 类选择器
result13 = soup.select('#one')  # id选择器
result14 = soup.select('head title')  # 后代选择器
result15 = soup.select('title,.title')  # 主选择器
result16 = soup.select('a[id="link3"]')  # 属性选择器

# 获取标签下的文本内容
result17 = soup.select('b')[0].get_text()

# 标签的属性
result18 = soup.select('#link1')[0].get('href')
print(result18)
