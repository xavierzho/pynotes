"""
使用正则表达式将headers转换成python 字典格式的工具函数
"""

headers = '''
Accept: */*
Origin: https://www.op.gg
Referer: https://www.op.gg/statistics/champion/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
'''
header = ''
for i in headers:
    if i == ':':
        i = "':'"
    if i == '\n':
        i = "',\n'"
    header += i
print(header[2:].replace(' ', '')+'\'')

