from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# 创建socket对象
server = socket(AF_INET, SOCK_STREAM)
# 绑定端口号
server.bind(('192.168.101.102', 10010))

# 开启监听状态（LISTENING）
server.listen(5)  # 传入参数为积压值


# 任务
def send_msg(sock):
    while True:
        msg = input('输入发送的消息：')
        sock.send(msg.encode('utf-8'))


def recv_msg(sock):
    while True:
        data = sock.recv(512).decode('utf-8')
        if len(data) == 0:
            break
        print('收到客户端的消息事：', data)


while True:
    sock, addr_info = server.accept()  # 阻塞的
    # 创建线程
    t1 = Thread(target=send_msg(), args=(sock,))
    t2 = Thread(target=recv_msg(), args=(sock,))
#     while True:
#         data = socket-套接字.recv(1024).decode('utf-8')
#         print('{}客户端说的话：{}'.format(addr_info[0], data))
#         if data == 'byebye':
#             break
#         msg = input('服务器端说的话:')
#         socket-套接字.send(msg.encode('utf-8'))
#         if msg == 'byebye':
#             break
    # 启动线程
    t1.start()
    t2.start()

    # print(addr_info, '已离开')

