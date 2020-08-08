# Traceback（追跟溯源），most recent call last（最后一次使用）


def a():
    num = 1/0


def b():
    a()


def c():
    b()


c()
