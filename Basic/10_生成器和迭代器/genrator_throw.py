"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/8
"""


def gen_func():
    yield "http://www.baidu.com"

    yield 2
    yield 3
    return 'jones'


if __name__ == '__main__':
    gen = gen_func()

    # throw，主动抛出异常
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))
    gen.throw(Exception, "download error")
