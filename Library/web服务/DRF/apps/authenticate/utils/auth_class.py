from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from ..models import UserToken
from rest_framework.response import Response
# 全局异常处理
from rest_framework.views import exception_handler
from rest_framework import status


class UserAuthenticate(BaseAuthentication):
    def authenticate(self, request):
        """
        认证逻辑，如果认证通过返回2个值，如果失败，抛出异常：APIException或者AuthenticationFailed
        :param request:
        :return:
        """
        token = request.query_params.get('token')
        if token:
            user_token = UserToken.objects.filter(token=token).first()
            if user_token:
                # 认证通过
                return user_token.user, token
            else:
                raise AuthenticationFailed('认证失败！')
        else:
            raise AuthenticationFailed('请求地址中需要携带token')


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
        print()
        # return response
        return Response(data={'status': 888, 'msg': str(response.data.get('detail'))},
                        status=status.HTTP_400_BAD_REQUEST)
