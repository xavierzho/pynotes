from socket import AF_INET, SOCK_STREAM, socket

"""
HTTP请求格式

b'GET / HTTP/1.1\r\n  请求首行
Host: 192.168.101.103\r\n  请求头
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Accept-Encoding: gzip, deflate\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n
Connection: close\r\n
请求头\r\n
'

"""
server = socket(AF_INET, SOCK_STREAM)
server.bind(('192.168.101.103', 80))
server.listen(5)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    with open('index.html', 'rb') as f:
        conn.send(f.read())
    conn.close()



