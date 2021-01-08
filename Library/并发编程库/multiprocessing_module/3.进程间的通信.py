"""
进程间通信与信号量
队列：
    FIFO

    put():队列中存放，如果满了则阻塞
    get():从队列中取值，如果空了则阻塞
"""

from multiprocessing import Process, Queue

queue = Queue(3)

queue.put('馒头1')
queue.put('馒头2')
queue.put('馒头3')
print(queue.full())  # 判断是否满了
print(queue)  # 打印queue对象
print(queue.qsize())

try:
    queue.put('馒头4', timeout=3)
    queue.put('馒头5', timeout=3)

except:
    print('存放馒头4失败')
    print('存放馒头5失败')

while True:
    try:
        print(queue.get(timeout=1))
    except:
        print('队列为空，取不出东西')
        break





