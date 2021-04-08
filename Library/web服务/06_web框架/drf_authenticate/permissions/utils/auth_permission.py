from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        不是超级用户不能访问
        :param request:
        :param view: 视图类
        :return:
        """
        print(view.get(request))
        user = request.user
        # 如果该字段使用choice，通过get_字段名_display()就能取出choice的值
        print(user.get_user_type_display())
        if user.user_type == 1:
            return True

        else:
            return False
