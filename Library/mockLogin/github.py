import requests
import time
from lxml import etree


class GithubMockLogin(object):
    def __init__(self):
        self.post_url = 'https://github.com/session'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.105 Safari/537.36',
            'Referer': 'https://github.com/login',
            'Host': 'github.com',
            'Origin': 'https://github.com'
        }
        self.login_url = 'https://github.com/login'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div[@class="auth-form px-3"]//input[1]/@value')[0]
        ga_id = selector.xpath('//div[@class="auth-form px-3"]//input[2]/@value')[0]
        print('authenticity_token =', token)
        return token, ga_id

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'authenticity_token': self.token()[0],
            'ga_id': self.token()[1],
            'login': email,
            'password': password,
            'timestamp': time.time()
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        print('Login status code is:', response.status_code)
        print(response.cookies.get_dict())

        print('response header:', response.requst.headers)
        if response.status_code == 200:
            self.repositories_name(response.text)

    def repositories_name(self, html):
        selector = etree.HTML(html)
        repositories_name = selector.xpath('//')

    def main(self):
        self.token()


GithubMockLogin().main()
