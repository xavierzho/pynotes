from rest_framework.throttling import SimpleRateThrottle, BaseThrottle
import time


class IPThrottle(SimpleRateThrottle):
    scope = 'ip'

    def get_cache_key(self, request, view):
        # print(request.META)
        print(request.META.get('REMOTE_ADDR'))
        return request.META.get('REMOTE_ADDR')


class CustomizeThrottle:
    # 所有的对象都是这个字典
    VISIT_DIC = {}

    def __init__(self):
        self.history_list: list = []

    def allow_request(self, request, view):

        addr = request.META.get('REMOTE_ADDR')
        ctime = time.time
        if addr not in self.VISIT_DIC:
            self.VISIT_DIC[addr] = [ctime, ]
            return True
        # 拿出当前访问者的列表
        self.history_list = self.VISIT_DIC[addr]
        while True:
            if ctime() - self.history_list[-1] > 60:
                self.history_list.pop()
            else:
                break
        if len(self.history_list) < 3:
            self.history_list.insert(0, ctime)
            return True
        else:
            return False

    def wait(self):
        # 当前时间减去表中最后一个时间
        ctime = time.time

        return 60 - (ctime() - self.history_list[-1])
