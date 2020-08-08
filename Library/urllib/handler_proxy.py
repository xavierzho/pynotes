import urllib.request


def create_proxy_handler():
    url = 'https://blog.csdn.net/lzf601/article/details/106068866/'

    # 添加代理
    proxy = {
        # 免费的写法
        "http": "http://58.246.3.178:53281",
        # "http": "58.246.3.178:53281"
        # 付费ip
        # "http": "username:pwd@192.168.12.1:8080"
    }

    # 代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    # 创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)
    # 拿着代理ip去发送请求
    html_text = opener.open(url).read().decode("utf-8")

    print(html_text)


def create_paid_proxy():
    # 另外一种方式发送付费ip地址
    url = 'https://blog.csdn.net/lzf601/article/details/106068866/'
    user_name = 'avcname'
    pwd = "123456"
    proxy_name = 'http://123.123.68.130:8080'
    # 创建密码管理器，添加用户名和密码
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    # uri定位 uri>url
    # url 资源定位符
    password_manager.add_password(None, proxy_name, user_name, pwd)
    # 创建验证代理IP的处理器
    handler_auth_proxy = urllib.request.HTTPBasicAuthHandler(password_manager)
    # 创建opener
    opener_auth = urllib.request.build_opener(handler_auth_proxy)
    # 发送请求
    response = opener_auth.open(url)
    html_text = response.read().decode("utf-8")
    return html_text


create_proxy_handler()
