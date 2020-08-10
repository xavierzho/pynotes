import random as rd
computer = rd.randint(0, 100)
guess = int(input('input your guess'))
count = 1
while True:
    if computer == guess:
        print('you are right.you guess {}times'.format(count))
        continue
    elif computer < guess:
        print('wrong!too big')
    else:
        print('wrong!too small')
    guess = int(input('input you guess'))
    count = count+1
    if count > 10:
        break
