import requests


# 通用爬虫框架


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常

        return r.text
    except:
        return "产生异常"


if __name__ == '__main__':
    url = ""
    print(getHTMLText(url))
