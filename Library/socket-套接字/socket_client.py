"""

网络各层
端口号：netstat -an 查看端口号
IP地址:电脑在互联网的标识



套接字（socket-套接字）是一个抽象层，应用程序可以通过它发送或接
收数据，可对其进行像对文件一样的打开、读写和关闭等操作。
套接字允许应用程序将I/O插入到网络中，并与网络中的其他应用
程序进行通信。网络套接字是IP地址与端口的组合。

TCP：SOCK_STREAM
UDP：SOCK_DGRAM

"""

from socket import socket, AF_INET, SOCK_STREAM

# 创建客户端的socket
client = socket(AF_INET, SOCK_STREAM)

con_address = ('192.168.101.1', 10010)  # 连接的目标服务器


# 告诉客户端要链接的服务器的地址和端口号
client.connect(con_address)

client.send('zxq来了，小心！'.encode('utf-8'))
client.close()
