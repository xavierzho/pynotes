# 远程命令执行
import subprocess
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.101.103', 10010))
s.listen(5)

while True:
    new_socket, dest_addr = s.accept()
    while True:
        data = new_socket.recv(1024)

        obj = subprocess.Popen(data.decode(),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               )
        # s.send(obj)
        data1 = obj.stdout.read().decode('gbk') + obj.stderr.read().decode('gbk')

        new_socket.send(data1.encode())
