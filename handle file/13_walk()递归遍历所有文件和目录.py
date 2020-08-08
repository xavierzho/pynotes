"""
os.walk()方法：
返回一个 3个元素的元组，(dirpath, dirnames, filenames),
dirpath：要列出指定目录的路径
dirnames：目录下的所有文件夹
filenames：目录下的所有文
"""

import os

all_files = []
path = os.getcwd()
list_files = os.walk(path)


for dirpath, dirnames, filenames in list_files:
    for dir in dirnames:
        print(os.path.join(dirpath, dir))

    for file in filenames:
        print(os.path.join(dirpath, file))

# 打印所有的子目录和子文件
for file in all_files:
    print(file)
