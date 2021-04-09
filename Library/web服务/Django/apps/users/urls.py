"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from django.urls import path
from apps.users import views

urlpatterns = [
    path("login/", views.login, name="u_login"),
    path("reg/", views.register, name="u_reg"),
    path("profile/", views.profile, name="u_profile"),
    path("logout/", views.logout, name="u_logout"),
    path("list/", views.users_list, name="u_list"),
    path("code/", views.get_code, name="u_code"),
    path("unreg/", views.unreg, name="unreg"),
    path("restpwd/", views.reset_pwd, name="reset_pwd"),
    path('settings/account/', views.account_settings, name='u_account'),
    path('settings/profile/', views.profile_settings, name='u_profile'),
    path('settings/others/', views.other_settings, name='u_others'),
]
