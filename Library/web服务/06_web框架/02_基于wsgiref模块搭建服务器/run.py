from wsgiref.simple_server import make_server
from views import *
from urls import urls


def run(env, response):
    """

    :param env: 请求相关的所有数据
    :param response: 响应相关的所有数据
    :return: 返回给浏览器的数据
    """
    # print(env)  # 请求相关的字典 wsgiref模块处理好http格式的数据，封装成字典形式，方便操作
    response('200 OK', [])  # 响应首行 和响应头
    # 从env中获取当前地址
    current_path = env.get('PATH_INFO')
    # if current_path == '/index':
    #     return [b'index']
    # elif current_path == '/login':
    #     return [b'login']
    # else:
    #     return [b'404 error']

    # 提前定义一个变量， 存储匹配到的函数名
    func = None
    for url in urls:
        if current_path == url[0]:
            # 将url对应的函数赋值给func
            func = url[1]
            break  # 匹配到之后，应该立即结束for循环
    # 判断func是否有值
    if func:
        res = func(env)
    else:
        res = error(env)
    return [res.encode('utf-8')]


if __name__ == '__main__':
    server = make_server('192.168.101.103', 8888, run)  # 监听192.168.101.103:8888,有客户端来到交给run函数处理
    """
    
    """
    server.serve_forever()  # 相当于while True启动服务端
