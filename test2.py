import ssl
import time
from selenium import webdriver
import os
import urllib.request
import re
from bs4 import BeautifulSoup
import requests
import copy

# url = 'https://www.cnblogs.com/Dominic-Ji/p/9234099.html'
# headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
#                          'likeGecko)Chrome/83.0.4103.116Safari/537.36'}
#
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, 'html.parser')
# html = soup.find_all()
# for tag in html:
#     # print(tag.name)
#     # 针对script标签直接删除
#     if tag.name == 'script':
#         # 删除标签
#         tag.decompose()
#
#
# print(soup.text)

# print(hash('age1'))
# print(hash('age'))

a = 10


def foo(a):
    a += 1
    print(a)


foo(a)
print(a)

l = [1, 2, 3]


def foo2(l):
    l.append(6)
    print(l)


foo2(l)
print(l)
