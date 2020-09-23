from socket import *


s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.101.103', 7788))


data = s.recvfrom(1024)
print(data)


