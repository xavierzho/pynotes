

class A:
    def __hash__(self):
        return hash(10)


a = A()
hash(a)
