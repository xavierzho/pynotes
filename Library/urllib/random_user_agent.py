import urllib.request
import random


def random_user_agent():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
                       ]

    # 随机选择请求的浏览器
    choice_user_agent = random.choice(user_agent_list)
    return choice_user_agent


def random_proxy():
    proxy_list = [
        {"http": "59.62.4.251:9000"},
        {"http": "118.113.247.0:9999"},
        {"http": "223.243.4.2:3000"},
        {"http": "59.33.53.222:9999"},
        {"http": "58.253.153.92:9999"}
    ]
    choice_proxy = random.choice(proxy_list)
    return choice_proxy
