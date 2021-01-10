class Animal:
    def __eat(self):
        print('吃东西')

    def run(self):
        self.__eat()
        print('飞快的跑')

    pass


class Bird(Animal):
    pass


b1 = Bird()
b1.run()
# b1.eat()

