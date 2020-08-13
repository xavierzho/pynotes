from proxyPool.free_proxies.db import RedisClient

conn = RedisClient()


def set(proxy):
    result = conn.add(proxy)
    print(proxy)
    print('录入成功' if result else '录入失败')


def s_con():
    print('请输入代理，输出exit退出读入')
    while True:
        proxy = input()
        if proxy == 'exit':
            break
        set(proxy)


if __name__ == '__main__':
    scon()
