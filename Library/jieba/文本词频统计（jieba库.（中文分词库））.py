import jieba
txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
excludes = {""}  # 将排名较高，但符合要求的词去除
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":  # 将同一类人事物归类统计
        rword = "孔明"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x: x[1], reversed=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
