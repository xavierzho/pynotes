class Person:

    def work(self):
        print("努力上班!")


def play_game(a):
    print("{0}在玩游戏".format(a))


Person.play = play_game
p = Person()
p.work()
p.play()
