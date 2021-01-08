import urllib.request  # 请求模块
import urllib.parse  # url转译模块
import urllib.robotparser  # robots.txt解析模块
import urllib.error  # 异常处理模块
import string


def get_method_params(keywords):
    url = 'http://www.baidu.com/s?wd=' + keywords
    # 将包含汉字的网址进行转译
    encode_url = urllib.parse.quote(url, safe=string.printable)
    # 返回http响应的对象
    response = urllib.request.urlopen(encode_url)

    # 将文件获取的内容转换成字符串
    # str_data = data.decode('utf-8')

    # 读取内容 bytes类型
    html_text = response.read().decode("utf-8")
    # print(html_text)

    return html_text


def download(data):
    # 数据写入文件
    with open("baidu.html", 'w', encoding='utf-8') as f:
        f.write(data)


download(get_method_params('字节'))

# 将字符串转换成bytes
str_name = '钟锡权'
bytes_name = str_name.encode('utf-8')



