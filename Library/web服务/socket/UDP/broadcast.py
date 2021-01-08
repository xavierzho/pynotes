from socket import *


broadcast = ('192.168.101.255', 7788)
s = socket(AF_INET, SOCK_DGRAM)
s.bind(broadcast)
# 重新设置套接字选项
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # 允许发送广播数据
print('等待回复')
s.sendto(b'1231929123', broadcast)
while True:
    buf, address = s.recvfrom(2048)
    print(address, buf.decode())
