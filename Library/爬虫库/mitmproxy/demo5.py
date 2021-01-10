import json


def response(flow):
    url = 'https://36kr.com/lapi/info-flow/newsflash_colums/newsflashes'
    if flow.request.url.startswith(url):
        data_list = json.loads(flow.response.text)['data']['items']
        for data in data_list:
            title = data['title']
            content = data['description']
            print(title)
            print(content)