# 打印12星座符号

for i in range(12):
    print(chr(9800 + i), end="")
"""
1.str.lower() or str.upper()
# 返回字符串的副本，全部字符小写/大写
"AbCdEfGh".lower()结果为"abcdefg"

2.str.split(sep=None)
# 返回一个列表，由str根据sep被分隔的部分组成
"A,B,C".split(",")结果为['A','B','C']

3.str.count(sub)
# 返回子串sub在str中出现的次数
"an apple a day".count('a')结果为4

4.str.replace(old,new)
# 返回字符串str副本，所有old字符串被替换为new
"python".replace("n","n123.io")结果为(python.io)

5.str.center(width[,fillchar])
# 字符串str根据宽度width居中，fillchar可选
"python".centert(20,"=")结果为'=======python======='

6.str.strip(chars)
# 从str中去掉在其左侧和右侧chars中列出的字符
"= python= ".strip("=np") 结果为"ytho"

7.str.join(iter)
# 在iter变量除了最后元素外每个元素后增加一个str
",".join("12345")结果为"1,2,3,4,5" 
主要用于字符串分隔等

"""
