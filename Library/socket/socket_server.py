"""
创建socket服务器
"""
from socket import socket, AF_INET, SOCK_STREAM

# 创建socket对象
server = socket(AF_INET, SOCK_STREAM)
# 绑定端口号
server.bind(('192.168.101.102', 10010))

# 开启监听状态（LISTENING）
server.listen(5)  # 传入参数为积压值

while True:
    socket, addr_info = server.accept()  # 阻塞的
    print(socket, addr_info)
    data = socket.recv(1024).decode('utf-8')
    print('{}发过来的消息事：{}'.format(addr_info[0], data))

    socket.close()
    print(addr_info, '已离开')

