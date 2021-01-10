from collections import deque

# # 单向队列
# q = deque([1, 2, 3], 5)  # 自动创建队列，第二个参数表示队列满了，自动出队列
# q.append(1)  # 队尾进队
# print(q.popleft())  # 队首出队
#
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队


def tail(n):
    with open(file='../geckodriver.log', mode='r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')
