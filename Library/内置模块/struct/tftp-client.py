# 模拟TFTP客户端
import struct
from socket import *

filename = ''
server_ip = '192.168.101.103'
send_data = struct.pack(f'!H{len(filename)}sb5sb', 1, filename.encode(), 0, b'octet', 0)
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(send_data, (server_ip, 69))
f = open('A0101a.xls', 'ab')
while True:
    recv_data = s.recvfrom(1024)
    caozuoma, ack_num = struct.unpack('!HH', recv_data[0][:4])
    rand_port = recv_data[1][1]  # 获取服务器的随机端口
    if int(caozuoma) == 5:
        print('文件不存在！')
        break

    print(f'操作码：{caozuoma},ACK:{ack_num},服务器随机端口：{rand_port}，数据长度：{len(recv_data[0])}')
    f.write(recv_data[0][4:])  # 将数据写入
    if len(recv_data[0]) < 516:
        break
    ack_data = struct.pack('!HH', 4, ack_num)
    s.sendto(ack_data, (server_ip, rand_port))

f.close()


