import jwt
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.utils import jwt_decode_handler
from api import models
from rest_framework import exceptions


def jwt_response_payload_handler(token, user=None, request=None):
    # 返回什么，前端就能看到什么
    return {
        'status': 200,
        'msg': '登录成功',
        'username': user.username,
        'token': token
    }


# class JWTAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         jwt_value = request.META.get('HTTP_AUTHORIZATION')
#         if not jwt_value:
#             raise exceptions.AuthenticationFailed('你没有携带认证信息')
#         else:
#             # jwt提供的三段token，取出payload
#             try:
#                 payload = jwt_decode_handler(jwt_value)
#             except jwt.exceptions.ExpiredSignature:
#                 raise exceptions.AuthenticationFailed('签名过期')
#             except jwt.exceptions.InvalidIssuer:
#                 raise exceptions.AuthenticationFailed('非法用户')
#             except Exception as e:
#                 raise exceptions.AuthenticationFailed(str(e))
#             # 因为payload就是用户信息的字典，需要转成用户对象
#             # 方式一：直接取数据库查
#             # user = models.Users.objects.get(pk=payload.get('user_id'))
#             # 方式二：转成用户对象
#             user = models.Users(id=payload.get('user_id'), username=payload.get('username'))
#             return user, jwt_value


class JWTAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        jwt_value = request.META.get('HTTP_AUTHORIZATION')
        if not jwt_value:
            raise exceptions.AuthenticationFailed('你没有携带认证信息')
        else:
            # jwt提供的三段token，取出payload
            try:
                payload = jwt_decode_handler(jwt_value)
            except jwt.exceptions.ExpiredSignature:
                raise exceptions.AuthenticationFailed('签名过期')
            except jwt.exceptions.InvalidIssuer:
                raise exceptions.AuthenticationFailed('非法用户')
            except Exception as e:
                raise exceptions.AuthenticationFailed(str(e))
            # 因为payload就是用户信息的字典，需要转成用户对象
            # 方式一：直接取数据库查
            # user = models.Users.objects.get(pk=payload.get('user_id'))
            # 方式二：转成用户对象
            user = self.authenticate_credentials(payload)
            return user, jwt_value

