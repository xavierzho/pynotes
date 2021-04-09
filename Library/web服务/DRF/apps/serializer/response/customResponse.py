"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from rest_framework.response import Response


class Message:
    def __init__(self):
        self.status = 200
        self.msg = 'OK'

    @property
    def get_dict(self):
        return self.__dict__


if __name__ == '__main__':
    res = Message()
    # res.data = {'name': 'jones'}
    res.status = 201
    res.msg = '查询失败'
    print(res.get_dict)


class CommonResponse(Response):
    def __init__(self, status, msg, data):
        super().__init__(status=status, data=data)
        self.msg = msg

    @property
    def get_dict(self):
        return self.__dict__