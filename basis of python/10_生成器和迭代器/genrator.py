"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/8
"""


def gen_func():
    html = yield "http://www.baidu.com"
    print(html)  # '<html>...</html>'
    yield 2
    yield 3
    return 'jones'


if __name__ == '__main__':
    gen = gen_func()
    # 启动生成器的方式一：
    gen.send(None)  # 这里必须为None，不然报TypeError: can't send non-None value to a just-started generator
    # 启动生成器的方式二：
    # url = next(gen)
    # 获取url
    html = '<html>...</html>'
    # send将值传递进生成器内部，还可以重启生成器，执行到下一个生成器的位置
    print(gen.send(html))  # 2
