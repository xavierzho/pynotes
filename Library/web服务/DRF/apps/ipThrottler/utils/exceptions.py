# 全局异常处理
from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response


def except_handler(exc, context):
    """

    :param exc:错误信息
    :param context:发送错误的函数或者类
    :return:
    """
    response = exception_handler(exc, context)
    # 处理数据库异常

    # 两种情况：1.是None，drf没有处理
    # 2.处理了，不符合我们期望要求
    if not response:
        if isinstance(exc, ZeroDivisionError):
            return Response(data={'status': 777, 'msg': '除以0的错误' + str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'status': 999, 'msg': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={'status': 888, 'msg': str(response.data.get('detail'))},
                        status=status.HTTP_400_BAD_REQUEST
               )