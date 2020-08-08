import time

import gevent
from gevent import monkey

monkey.patch_all()


def eat():
    for i in range(5):
        print('zxq喜欢吃肉饼。。。')
        time.sleep(0.1)


def listen_music():
    for i in range(5):
        print('坤坤喜欢听麻婆豆腐。。', i)
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(eat)
    g2 = gevent.spawn(listen_music)

    g1.join()
    g2.join()
    print('----->over')

