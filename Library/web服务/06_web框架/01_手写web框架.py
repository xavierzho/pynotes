from socket import socket, AF_INET, SOCK_STREAM

"""
b'GET / HTTP/1.1\r\n
Host: 192.168.101.103\r\n
Cache-Control: max-age=0\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Accept-Encoding: gzip, deflate\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n
Connection: close\r\n\r\n'

"""
server = socket(AF_INET, SOCK_STREAM)  # 三次握手四次挥手，osi七层模型
server.bind(('192.168.101.103', 8080))  # IP协议，以太网协议，arp协议
server.listen(5)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)  # 二进制数据
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    # print(data)
    data2 = data.decode()
    current_path = data2.split(' ')[1]
    # print(current_path)
    if current_path == '/index':
        # conn.send(b'index hahahahaha')
        with open('.index.html', 'rb') as f:
            conn.send(f.read())
    elif current_path == '/login':
        conn.send(b'login')
    else:
        conn.send(b' hello web')
    conn.close()
