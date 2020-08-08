from bs4 import BeautifulSoup
import re
import requests
import bs4
import json


def getHTMLText(url):  # 获取HTML页面
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


start_url = "https://www.huya.com/g"


# 将板块地址存入字典
def gameCard_link(gameName):
    soup = BeautifulSoup(getHTMLText(start_url), 'html.parser')
    nameList = []
    urlList = []
    gameDict = dict()

    # 板块列表
    tagName = soup.find_all('li', class_="g-gameCard-item")
    for tagName in tagName:
        nameList.append(tagName['title'])
    # 板块url列表
    tagUrl = soup.find_all('a', class_="g-gameCard-link")
    for tagUrl in tagUrl:
        urlList.append(tagUrl['href'])
    # 合并板块对应的url形成字典
    for gameName, gameUrl in zip(nameList, urlList):
        gameDict[gameName] = gameUrl

    return gameDict[gameName]


# # 获取该板块可翻业数
# def getPage():
live_url = requests.get(gameCard_link(input('请输入要查看的板块：')))
live_url.json()
# page = soup.find_all('div', class_='list-page')
# print(page)




