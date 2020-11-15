def func(x):
    if x > 0:
        print(x)
        func(x - 1)


def func2(x):
    if x > 0:
        func(x - 1)
        print(x)


func(3)
func2(3)
