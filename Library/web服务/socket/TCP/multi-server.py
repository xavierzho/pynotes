from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from multiprocessing import Process


def deal_client(new_socket, dest_addr):
    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data) > 0:
            print(f'来自{dest_addr}的消息是：{recv_data.decode("utf-8")}')
        else:
            print(f'{dest_addr}已关闭连接！')
            break

    new_socket.close()


def main():
    server = socket(AF_INET, SOCK_STREAM)
    #
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(('192.168.101.103', 10010))
    server.listen(5)
    try:
        while True:
            print('-----主进程开启，等待客户端的连接！------')
            new_socket, dest_addr = server.accept()
            print('-----主进程创建一个子进程来负责一个客户端！----')
            client = Process(target=deal_client, args=(new_socket, dest_addr))
            client.start()
            new_socket.close()
    finally:
        # 无论如何服务都会关闭
        server.close()


if __name__ == '__main__':
    main()
