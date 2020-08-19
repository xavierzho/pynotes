"""
西门吹雪和叶孤城
属性:
    name:玩家姓名
    blood：玩家血量
方法:
    tong() 捅一刀对方掉10滴血
    kan() 砍一刀对方掉15滴血
    chiyao() 吃一颗药，补10滴血
    __str__() 打印玩家状态
"""
import time


class Hero(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def tong(self, enemy):
        enemy.hp -= 10
        info = '【%s】捅了【%s】一刀' % (self.name, enemy.name)
        print(info)

    def kan(self, enemy):
        enemy.hp -= 15
        info = '【%s】捅了【%s】一刀' % (self.name, enemy.name)
        print(info)

    def chiyao(self, enemy):
        self.hp += 10
        info = '【%s】吃了一颗补血药' % self.name
        print(info)

    def __str__(self):
        return '%s 剩下 %s 的血量' % (self.name, self.hp)


xmcx = Hero('西门吹雪', 100)
ygc = Hero('叶孤城', 100)
while 1:
    if xmcx.hp <= 0 or ygc.hp <= 0:
        # 满足条件就退出循环
        break

    xmcx.tong(ygc)
    print(xmcx)  # 打印对象的状态
    print(ygc)  # 打印对象的状态
    print("-" * 50)
    ygc.tong(xmcx)
    print(xmcx)
    print(ygc)
    xmcx.chiyao(xmcx)
    time.sleep(1)

print('对战结束...')