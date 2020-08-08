"""
线程间通信
生产者和消费者：
    生产者：线程
    消费者：线程

"""
import time
import random
from threading import Thread, current_thread
from queue import Queue


def producer(queue):
    print('{}开门了！'.format(current_thread().name))
    foods = ['包子', '馒头', '香肠', '蒸饺', '肠粉']
    for i in range(1, 21):
        food = random.choice(foods)
        print('{}正在制作中。。。。'.format(food))
        time.sleep(1)
        print("加工完成，可以出品！")
        queue.put(food)
    queue.put(None)


def consumer(queue):
    print('{}来吃饭了！'.format(current_thread().name))
    while True:
        food = queue.get()
        if food:
            print(' 正在享用中{}！'.format(food))
            time.sleep(0.5)
        else:
            print('{}把饭店吃光了！走人！'.format(current_thread().name))
            break


if __name__ == '__main__':
    queue = Queue(8)
    t1 = Thread(target=producer, name='老家肉饼', args=(queue,))
    t2 = Thread(target=consumer, name='zxq', args=(queue,))

    t1.start()
    t2.start()

