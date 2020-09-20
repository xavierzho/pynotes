import random


def captcha(length):
    li = [chr(c) for c in range(ord('a'), ord('a')+26)]
    li.extend([chr(c) for c in range(ord('A'), ord('A')+26)])
    li.extend((str(i) for i in range(10)))
    print(li)
    return ''.join(random.choices(li, k=length))


print(captcha(4))


