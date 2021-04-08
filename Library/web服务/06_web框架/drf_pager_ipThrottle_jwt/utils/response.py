from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=200, msg='success', data=None, status=None, headers=None, **kwargs):
        dic = {'code': code, 'msg': msg}
        if data:
            dic = {'code': code, 'msg': msg, 'data': data}
            dic.update(kwargs)
        super().__init__(data=dic, status=None, headers=None)
