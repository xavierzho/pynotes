import urllib.request
import urllib.parse


def load_baidu():
    url = 'https://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    # 创建请求对象
    request = urllib.request.Request(url, headers=headers)
    # 动态的添加headers信息
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
    # 请求网络数据
    response = urllib.request.urlopen(request)
    html_text = response.read().decode('utf-8')

    # # 获取完整的url
    # print(request.get_full_url())
    # # 响应头信息
    # print(response.headers)
    # # 请求头信息
    # print(request.headers)
    # # 下面方法注意只有首字母大写其他小写，否则返回None
    # print(request.get_header('User-agent'))
    return html_text


def download(data):
    # 数据写入文件
    with open("baidu.html", 'w', encoding='utf-8') as f:
        f.write(data)


download(load_baidu())

