"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=1, msg='success', data=None, **kwargs):
        dic = {'code': code, 'msg': msg}
        if data:
            dic = {'code': code, 'msg': msg, 'data': data}
        super().__init__(data=dic, status=None, headers=None)
