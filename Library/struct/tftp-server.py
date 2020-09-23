import struct
from socket import *

filename = r'c:/users/jonescy/OneDrive/文档'

data = struct.pack(f'H{len(filename.encode("gb2312"))}sb5sb', 2, filename.encode('gb2312'), 0, b'octet', 0)
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(data, ('127.0.0.1', 69))
f = open(filename, 'rb')
while True:
    ret = s.recvfrom(1024)
    port = ret[1]
    data1, data2 = struct.unpack('!HH', ret[0][:4])
    if data1 == 4:
        data = f.read(512)
        pack = struct.pack(f'!HH{len(data)}s', 3, data2+1,data)
        s.sendto(pack, port)
        if len(data) < 512:
            break
