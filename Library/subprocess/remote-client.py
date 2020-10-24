from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(('192.168.101.103', 10010))

while True:
    ip = input('远程执行的命令！')
    s.send(ip.encode())
    data = s.recv(1024).decode()
    print(data)

