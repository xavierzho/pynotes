"""
client:浏览器客服端
server端：

浏览器 request
    request 行 :GET HTTP/1.1
    请求头： key:value
    请求体： POST

server端response
    response 行 :HTTP/1.1 Status Code
    响应头： key:value
    响应体: 数据
"""
# from socket-套接字 import socket-套接字, AF_INET, SOCK_STREAM
from gevent import monkey, socket
import gevent
monkey.patch_all()


# 创建socket对象
server = socket.socket()
# 绑定端口号
server.bind(('192.168.101.102', 10011))

# 开启监听状态（LISTENING）
server.listen(5)  # 传入参数为积压值


def handle_client(sock):
    recv_data = sock.recv(1024).decode('utf-8')
    print(recv_data)

    response_line = 'HTTP/1.1 200 OK\r\n'
    response_header = 'Content-Type:text/html;charset=utf-8\r\nserver:pythonServer\r\n'
    msg = '<h1>哈哈你来了！</h1><div style="color:red;">欢迎你来了！</div>'
    response = response_line+response_header+'\r\n'+msg
    sock.send(response.encode('utf-8'))
    sock.close()


while True:
    sock, addr_info = server.accept()  # 阻塞的
    print(addr_info, "来啦！")
    gevent.spawn(handle_client, sock)
