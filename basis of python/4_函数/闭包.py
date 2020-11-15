#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
"""


def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum1


f = lazy_sum(1,3,5,7,9)
print(f)
print(f())


def wrapper(func):
    def inner(*args, **kwargs):
        # 代码
        res = func(*args, **kwargs)
        # 代码
        return res
    return inner


@wrapper
def a():
    print('aaa')
# a = wrapper(a)
# a()

