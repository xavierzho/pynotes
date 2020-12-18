"""
迭代模式：对外提供一个接口，实现顺序访问聚合数据，但是不显示该数据的内部机制。这就是Python中大名鼎鼎的迭代器。
实现迭代模式对于Python来说没有多余的代码，寥寥几行代码足可以实现迭代模式。
应用场景：常应用场景是在只提供接口而不暴露内部机制的场景中

迭代器、生成器、可迭代对象概念
生成器：对于一个数据集合，生成器并不记住每个元素值，但在循环中记录元素位置并根据元素生成规则推算出数值，这种边循环边计算的形式是生成器。
迭代器：是一种访问集合的方式，记住遍历位置，从第一个元素开始访问，直到最后一个元素，并且只能前进不能后退。
可迭代对象：像list、set、str这种可以通过for遍历的类型是可迭代对象，这种遍历顺序可以从尾到头。
yield、yield form、send、next()、__next__()、iter()具体作用：
yield：创建一个生成器
yield form：创建一个嵌套的生成器，form后面跟一个生成器，每次执行到yield form 会先把后面的生成器执行完
next()：访问迭代器的内部元素
send(n)：访问迭代器的内部元素,可指定访问索引为n的元素
__next__()：next()实质上就是调用__next__()
iter()：将可迭代对象转换为生成器

"""


def FibonacciSequence(n):
    x = 0
    y = 1
    i = 1
    while True:
        yield y
        if i == n:
            break
        x, y = y, x+y
        i += 1


if __name__ == '__main__':
    test = FibonacciSequence(7)
    # next(test)
    for i in test:
        print(i)
