from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.101.130', 8881))
while True:
    data = s.recvfrom(1024)
    print(data[0].decode())
    s.sendto(data[0], data[1])

s.close()
