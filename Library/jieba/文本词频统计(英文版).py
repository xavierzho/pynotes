"""
1.jieba.lcut(s)
# 精确模式，返回一个列表类型的分词结果
jieba.lcut("中国是一个伟大的国家")

2.jieba.lcut(s, cut_all=True)
# 全模式，返回一个列表类型的分词结果，纯在冗余
jieba.lcut("中国是一个伟大的国家",cut_all=True)

3.jieba.lcut_for_search(s)
# 搜索引擎模式，返回一个列表类型的分词结果，存在冗余
jieba.lcut_for_search("中华人民共和国是伟大的")

4.jieba.add_word(w)
# 向分词词典增加新词w
jieba.add_word("蟒蛇语言")

"""


def getText():
    txt = open("../../mooc/python.txt", "r", encoding="utf-8").read()
    txt = txt.lower()
    for ch in '!"#$%^&*<>?:{}[];,./`~':
        txt = txt.replace(ch, " ")
    return txt


pythonTxt = getText()
words = pythonTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
