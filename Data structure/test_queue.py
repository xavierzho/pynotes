class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.rear = 0  # 队尾进队列
        self.front = 0  # 队首出队列
        self.size = size

    def push(self, elem):
        if not self.is_full():
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = elem
        else:
            raise IndexError('Queue is full')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty.')

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
for i in range(4):
    q.push(i)

print(q.pop())
q.push(4)
