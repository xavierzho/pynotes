from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from main.models import UserToken


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
