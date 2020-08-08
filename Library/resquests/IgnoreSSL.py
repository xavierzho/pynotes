import requests

# 1.请求的url
url = 'https://www.12306.cn/index/index.html'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
# 代理设置
proxy = {'http': '115.221.242.112:9999'}
# ssl认证
# https 是有第三方 CA 证书认证
# 但是 12306 虽然是https但是是自己的认证的
# 解决方法 是:告诉web 忽略证书访问verify=False

response = requests.get(url=url, headers=headers, proxies=proxy, verify=False)

data = response.content.decode()

with open('12306ssl.html', 'w', encoding='utf-8') as f:
    f.write(data)
