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
    # 生成器的两个重要的方法
    # throw，主动抛出异常
    print(next(gen))
    # close，关闭生成器
    gen.close()  # 抛出StopIteration
    next(gen)

