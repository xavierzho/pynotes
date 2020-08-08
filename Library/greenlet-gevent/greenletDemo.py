from greenlet import greenlet


def eat():
    for i in range(5):
        print('zxq喜欢吃肉饼。。。')
        g2.switch()


def listen_music():
    for i in range(5):
        print('坤坤喜欢听麻婆豆腐。。', i)
        g1.switch()


if __name__ == '__main__':
    g1 = greenlet(eat)
    g2 = greenlet(listen_music)

    g1.switch()

