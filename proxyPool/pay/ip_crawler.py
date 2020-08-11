# 代理池2

import redis
import time
import json
import requests
import telnetlib


class IpProxies:

    def ip_generator(self):
        r = redis.StrictRedis(host='127.0.0.1', port=6379)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        # API接口
        http_ip = 'http://d.jghttp.golangapi.com/getip?num=19&type=2&pro=&city=0&yys=0&port=2&pa' \
                  'ck=28654&ts=1&ys=1&cs=1&lb=1&sb=0&pb=45&mr=1&regions='
        response = requests.get(http_ip, headers=headers)
        ip_json = response.json()

        for item in ip_json['data']:
            ip = item['ip'].strip()
            port = item['port']

            expire_time = item['expire_time']
            time_array = time.strptime(expire_time, '%Y-%m-%d %H:%M:%S')
            expire_time_stamp = int(time.mktime(time_array))

            proxy_item = {'schema': "http", 'host': ip, 'port': port, 'expire_time': expire_time_stamp,
                          'account': '', 'password': '', 'count': 2}
            ip_port_list_formal = []

            proxy_temp_all = r.smembers('ip_pool1')  # 把redis作为代理池中间件 如果要调用的时候就去redis上面读取
            # 对代理池中的代理ip去重
            for proxy_temp in proxy_temp_all:
                # print(proxy_temp)
                item_json = eval(proxy_temp)
                # print(item_json)
                ip_formal = item_json['host']
                port_formal = str(item_json['port'])

                ip_port_formal = ip_formal + ':' + port_formal

                if ip_port_formal not in ip_port_list_formal:
                    ip_port_list_formal.append(ip_port_formal)
                else:
                    print('duplicating:', proxy_temp)
                    r.srem('ip_pool1', proxy_item)

            ip_port = ip + ':' + str(port)
            if ip_port not in ip_port_list_formal:
                print('Add', json.dumps(proxy_item))
                r.sadd('ip_pool1', json.dumps(proxy_item))


if __name__ == '__main__':
    IpProxies().ip_generator()
