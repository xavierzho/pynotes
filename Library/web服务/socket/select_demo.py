"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/7
"""

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()

urls = ['http://www.baidu.com']
stop = False

class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            'GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(self.path, self.host).encode('utf-8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        selector.unregister(key.fd)
        d = self.client.recv(1024)
        if d:
            # print(d)
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode('utf-8')
            html = data.split('\r\n\r\n')[1]
            print(html)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        self.data = b''
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == '':
            self.path = "/"

        # 建立socket连接

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)  # 设置非阻塞IO
        try:
            self.client.connect((self.host, 80))  # 如果使用了非阻塞IO这行代码会报异常BlockingIOError
        except BlockingIOError as e:
            pass

        # 注册到select中
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环，不停请求socket的状态并调用对用的回调函数
    # 1.select本身不支持register模式
    # 2.socket状态变化后的回调是由自己完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    # 事件循环+回调+select(poll\epoll)


if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url('http://www.baidu.com')
    loop()
