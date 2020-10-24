class MSG(object):
    def __init__(self):
        pass  # 发送微信需要做的前期的准备工作

    def send(self, content):
        print(f'短信通知：{content}')