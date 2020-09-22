import time
import os
from multiprocessing import Process

number = 100


def program():
    global number
    for i in range(1, 6):
        print('写代码第{}行'.format(i), os.getpid(), os.getppid())
        time.sleep(0.5)
    number -= 10
    print('写代码的number：', number)


def listen_music():
    global number
    musics = ['逆战1', '凉凉2', '麻婆豆腐3', '大碗宽面4']
    for music in musics:
        print('正在听{}歌'.format(music), os.getpid(), os.getppid())
        time.sleep(0.5)
    number -= 20
    print('听音乐的number：', number)


def wechat(user):
    global number
    name = 'james'
    for i in range(5):
        print('{}正在跟{}聊天'.format(user, name), os.getpid(), os.getppid())
        time.sleep(0.5)
    number -= 30
    print('聊微信的number：', number)


print('number', 100)

if __name__ == '__main__':

    p1 = Process(target=program)
    p2 = Process(target=listen_music)
    p3 = Process(target=wechat, args=('zxq', ))
    # target表示可调用对象,args表示调用对象的位置参数元组
    # (注意:元组中只有一个元素时末尾要加,)

    # 启动线程
    p1.start()
    p2.start()
    p3.start()
    # 阻塞主线程
    p1.join()
    p2.join()
    p3.join()
    #
    # p1.run()
    # p2.run()
    # p3.run()

    # print('main:', os.getpid())
    # for i in range(5):
    #     if i == 3:
    #         p1.terminate()  # 终止进程
    #     elif i == 5:
    #         p2.terminate()
    #
    #     time.sleep(0.3)
    #     print('main:', i)
    #
    # p2.close()

    # print('p1是否活着：', p1.is_alive())
    # print('p2是否活着：', p2.is_alive())
