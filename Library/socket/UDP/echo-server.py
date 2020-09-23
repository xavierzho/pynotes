from socket import *


s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 8881))

num = 0
while True:
    if num > 19:
        data = s.recvfrom(1024)
        s.sendto(data[0], data[1])
        num += 1
    else:
        break
s.close()
