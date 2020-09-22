from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.bind(('192.168.101.103', 8881))
addr = ('192.168.101.103', 8882)

while True:
    data = s.recvfrom(1024)
    if data[0].decode('gb2312') == '886':
        s.close()
    else:
        print(data[0].decode('gb2312'))


