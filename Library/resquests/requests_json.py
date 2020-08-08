import json

import requests

url = 'https://api.github.com/user'

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }

# 这个网址返回的内容不是html,而是标准的json
response = requests.get(url, headers=headers)

# str
data = response.content.decode()
# str->json
# data_dict = json.loads(data)
data = response.json()

print(data)
