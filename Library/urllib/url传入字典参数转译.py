import string
import urllib.parse
import urllib.request


def get_params():
    url = "http://www.baidu.com/s?"

    params = {
        "wd": "字节",
        "key": "zhang",
        "value": "san"
    }
    # 将字典类型的参数转译
    str_params = urllib.parse.urlencode(params)
    final_url = url + str_params
    # 将拼接后的url能让机器读取
    end_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(end_url)
    html_text = response.read().decode('utf-8')
    print(html_text)


get_params()


