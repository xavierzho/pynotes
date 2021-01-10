# 更请求头
def request(flow):
    flow.request.headers['User-Agent'] = 'Mitmproxy'
    print(flow.request.headers)