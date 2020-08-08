import urllib.request
from http import cookiejar
import urllib.parse


# 1.代码登录
# 1.1登录网址
url = "https://www.yaozh.com/login/"
# 1.2登录的参数
login_form_data = {
    "username": "TinsQua",
    "pwd": "Snq1997.",
    "formhash": "BA3E6402D5",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
}

# 1.3发送登录请求
cook_jar = cookiejar.CookieJar()

# 定义有添加cookies功能的处理器
cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)

# 根据处理器生成opener
opener = urllib.request.build_opener(cook_handler)

# 带着参数发送post请求
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
}

# 参数转译，post请求的类型types
login_str = urllib.parse.urlencode(login_form_data).encode('utf-8')
login_request = urllib.request.Request(url, headers=headers, data=login_str)

# 如果登录成功，cookjar自动保存cookie
opener.open(login_request)

# 2.代码带着cookie去访问个人中心
center_url = 'https://www.yaozh.com/member/'
center_request = urllib.request.Request(center_url, headers=headers)
response = opener.open(center_url)

data = response.read().decode("utf-8")

with open("yaozh.html", "w", encoding='utf-8') as f:
    f.write(data)

