import requests


class RequestSpider(object):
    def __init__(self):
        url = 'https://www.baidu.com/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        self.response = requests.get(url, headers=headers)

    def run(self):
        data = self.response.content
        # 1.获取请求头
        request_headers = self.response.request.headers
        print('请求头信息：{}'.format(request_headers))
        # 2.获取响应头
        response_headers = self.response.headers
        print('响应头信息：{}'.format(response_headers))

        # 3.响应状态码
        response_code = self.response.status_code
        print('状态码：{}'.format(response_code))

        # 4.请求的cookies
        request_cookie = self.response.request._cookies
        print('请求的cookies信息：{}'.format(request_cookie))

        # 5.响应的cookies
        response_cookie = self.response.cookies
        print('响应的cookies信息：{}'.format(response_cookie))


RequestSpider().run()
