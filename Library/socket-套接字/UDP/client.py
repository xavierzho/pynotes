from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.101.103', 8882))
addr = ('192.168.101.103', 8881)
while True:

    da = input('请输入消息!')
    s.sendto(da.encode('gb2312'), addr)

