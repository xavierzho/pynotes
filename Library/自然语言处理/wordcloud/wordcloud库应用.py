"""
w = wordcloud.WordCloud(<参数>)
width ： 指定词云对象生成图片的宽度，默认像素400
heigt : 指定词云对象生成图像的高度，默认200像素
min_font_size : 指定词云中字体的最小字号，默认4号
max_font_size : 指定词云中字体的最大字号，根据高度自动调节
font_step : 指定词云中字体字号的步进间隔，默认1
font_path : 指定词云中问价难得路径，默认None（font_path="msyh.ttc"）
max_words : 指定词云显示最大单词数量，默认200
stop_words : 指定词云废除词列表，即不显示的单词列表
mask : 指定词云形状，默认长方形，需要引用imread（）函数
# from scipy.misc import imread
# mk = imread("pic.png")
# w = wordcloud.WordCloud(mask=mk)
background_color : 指定词云图片的背景颜色，默认为黑色
1.w.generate(txt)
# 向WordCloud对象w中加载文本txt

2.w.to_file(filename.jpg/png)
# 将词云输出为图像文件，.png或.jpg格式

"""

import wordcloud
import jieba

txt = "人们总爱追问人生的意义，其实人生本无所谓意\
义，因为存在先于本质，本质之前的存在是禁绝思考的。\
人生的无意义赋予了人的自由，倘若人生有一个注定的意义，\
那么人人都如同一具机器。"
w = wordcloud.WordCloud(width=1000, height=700, \
                        font_path="msyh.ttc", \
                        background_color="white")

w.generate("".join(jieba.lcut(txt)))
w.to_file("pywcloud2.png")
