# 非小号的行情走势数据
import requests
import json

header = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

url = 'https://dncapi.bqiapp.com/api/coin/web-charts?code=bitcoin&type=w&webp=1'
response = requests.get(url, headers=header, timeout=5)


result = json.loads(response.text)
print(result)
print(result.keys())
