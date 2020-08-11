import redis
import time
import telnetlib
import json

client = redis.StrictRedis(host='127.0.0.1', port=6379)


def verify_ip_pool():
    proxy_item_all = client.smembers('ip_pool2')
    for proxy_item in proxy_item_all:
        proxy_item_dict = json.loads(proxy_item)
        ip = proxy_item_dict['host']
        port = proxy_item_dict['port']
        expire_time = proxy_item_dict['expire_time']
        if expire_time < int(time.time()):
            print('expired and delete')
            client.srem('ip_pool2', proxy_item)
        else:
            print('still available')

            try:
                telnetlib.Telnet(ip, port=port, timeout=1)
                print('success', ip ,port)
            except:
                print('==>fail and delete<==', ip, port)
                client.srem('ip_pool2', proxy_item)


if __name__ == '__main__':
    try:
        print('='*20)
        verify_ip_pool()
    except Exception as e:
        print(e)
