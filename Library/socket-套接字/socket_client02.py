from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# 创建客户端的socket
client = socket(AF_INET, SOCK_STREAM)

con_address = ('192.168.101.102', 10010)  # 连接的目标服务器


# 告诉客户端要链接的服务器的地址和端口号
client.connect(con_address)


def send_msg(sock):
    while True:
        msg = input('客户端输入发送的消息：')
        sock.send(msg.encode('utf-8'))


def recv_msg(sock):
    while True:
        data = sock.recv(512).decode('utf-8')
        if len(data) == 0:
            break
        print('收到服务器的消息事：', data)


# 创建线程
Thread(target=send_msg, args=(client,)).start()
Thread(target=recv_msg, args=(client,)).start()

# while True:
#     msg = input('客户端输入：')
#     client.send(msg.encode('utf-8'))
#     if msg == 'byebye':
#         break
#     # 接受服务器端的消息
#     reve_msg = client.recv(512).decode('utf-8')
#     print('服务器回话：', reve_msg)
#     if reve_msg == 'byebye':
#         break


