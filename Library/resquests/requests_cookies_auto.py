import requests

# 请求数据的url
from requests.models import Response

login_url = 'https://www.yaozh.com/login/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
# 登录表单
login_form_data = {
    "username": "TinsQua",
    "pwd": "Snq1997.",
    "formhash": "F9F2B7C72B",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
}
# 创建session对象 自动保存cookies == cookiesjar
session = requests.session()
login_response = session.post(login_url, data=login_form_data, headers=headers)
member_url = 'https://www.yaozh.com/member/'
html_text = session.get(member_url, headers=headers).content.decode()

with open('cookies.html', 'w', encoding='utf-8') as f:
    f.write(html_text)
