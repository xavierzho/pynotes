import wordcloud
import jieba
from scipy.misc import imread
mk = imread("pic.png")
f.open("", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=700, \
                        font_path="msyh.ttc", \
                        background_color="white")

w.generate(txt)
w.to_file("pywcloud3.png")

