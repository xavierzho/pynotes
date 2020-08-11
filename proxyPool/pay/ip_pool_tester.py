# 代理池2
import time
import telnetlib
import redis
import json

r = redis.StrictRedis(host='127.0.0.1', port=6379)


def verify_ip_pool():
    # 读代理池1
    proxy_item_all = r.smembers('ip_pool1')
    # print(proxy_item_all)
    for proxy_item in proxy_item_all:
        proxy_item_dict = eval(proxy_item)
        # print(proxy_item_dict)
        ip = proxy_item_dict['host']
        port = proxy_item_dict['port']
        expire_time = proxy_item_dict['expire_time']
        # print(expire_time)
        current_time = int(time.time())
        if expire_time < current_time:
            print('expire and delete')
            # 从代理池1 中删除
            r.srem('ip_pool1', proxy_item)
        else:
            print('still available')

            ip_list_formal = []
            # 读代理池1
            proxy_item_all = r.smembers('ip_pool2')

            for item in proxy_item_all:
                # print(item)
                item_json = eval(item)

                # print(item_json)
                ip_formal = item_json['host']
                port_formal = item_json['port']

                ip_port_formal = ip_formal + ":" + str(port_formal)

                if ip_port_formal not in ip_list_formal:
                    ip_list_formal.append(ip_port_formal)

            try:
                # 验证代理是否可用
                telnetlib.Telnet(ip, port=port, timeout=2)
                # print('success', ip, port)
                ip_port = ip + ':' + str(port)

                if ip_port not in ip_list_formal:
                    print("==> add to ip_pool2<==")
                    r.sadd('ip_pool2', json.dumps(proxy_item))
                else:
                    print('duplicate')

            except:
                print('fail', ip, port)


if __name__ == '__main__':
    try:
        verify_ip_pool()
        print('='*20)
    except Exception as e:
        print(e)
