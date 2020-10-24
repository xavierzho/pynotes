"""
创建socket服务器
"""
from socket import socket, AF_INET, SOCK_STREAM

# 创建socket对象
server = socket(AF_INET, SOCK_STREAM)
# 绑定端口号
server.bind(('192.168.101.103', 10010))

# 开启监听状态（LISTENING）
server.listen(5)  # 传入参数为积压值

while True:
    #
    s, addr_info = server.accept()  # s是新的socket对象，后面的发送和接收都是用这个新的socket对象进行的
    print(s, addr_info)
    data = s.recv(1024).decode('utf-8')
    print(f'来自{addr_info[0]}发过来的消息事：{data}')

    s.close()
    print(addr_info, '已离开')

