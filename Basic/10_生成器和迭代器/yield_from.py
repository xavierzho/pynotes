"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/8
"""
# python3.3新语法yield from
from itertools import chain

my_list = [1, 2, 3]
my_dict = {'jones': 'http://www.project.com',
           'jonescy': 'http://www.project.com'}


# def gen_1(iterable):
#     yield iterable
#
#
# def gen_2(iterable):
#     # 可以将迭代对象逐个迭代出来，可以解决协程嵌套的问题
#     yield from iterable
# for val in gen_1(range(10)):
#     print(val)
# print('-'*20)
# for val in gen_2(range(10)):
#     print(val)

# # 协程也是iterable对象
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         # 可以使用yield from iterable对象
#         yield from my_iterable
#         # for value in my_iterable:
#         #     yield value
#
#
# for val in my_chain(my_dict, my_list, range(5, 10)):
#     print(val)


def g1(gen):
    yield from gen


def main():
    g = g1(range(10))
    g.send(None)


# 三个概念：1.main()是调用方，2.g1是委托生成器，3.gen是子生成器
# yield from 在子生成器和调用方之间建立双向通道
if __name__ == '__main__':
    main()
