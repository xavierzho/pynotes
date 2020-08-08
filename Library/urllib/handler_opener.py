import urllib.request


def handler_opener():
    # 系统的urlopen没有添加代理的功能，所以要自定义这个功能
    # https->s指的是security 套接层 ssl第三方的CA数字证书
    # 端口->http:80  https->443
    url = 'https://blog.csdn.net/lzf601/article/details/106068866/'

    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的opener
    opener = urllib.request.build_opener(handler)
    # 用自己创建的opener调用open方法
    response = opener.open(url)
    html_text = response.read().decode("utf-8")
    print(response)
    print(html_text)


handler_opener()
