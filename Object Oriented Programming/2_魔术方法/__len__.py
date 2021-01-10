class A:
    def __init__(self, name):
        self.name = name
        print("实例化的时候执行我")

    def __len__(self):
        print('执行len触发我')
        return len(self.name)


a = A('jones')
print(len(a))
# a.__len__()
