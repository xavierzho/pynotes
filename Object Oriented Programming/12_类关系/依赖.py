
class Person:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def fire(self, ak, obj):
        ak.fire(obj)


class Police(Person):

    call = '警察'

    def __init__(self, name, hp, job):
        self.job = job
        super().__init__(name, hp)


class Bandit(Person):

    call = '土匪'

    def __init__(self, name, hp, job):
        self.job = job
        super().__init__(name, hp)


class AK:
    def __init__(self):
        self.ak = 90

    def fire(self, obj, obj1):
        print(f'{obj.name}使用AK打了一下{obj1.name},{obj1.name}掉了90滴血')


p = Police('海报突击队', 100, '警察')
ak = AK()
b = Bandit('山雕', 100, '土匪')
p.fire(ak, b)
