from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app01 import validation_reg_info


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去用户表中校验数据
        # 1.表在那？
        # 2.密码如何比对？

        user_obj = auth.authenticate(request, username=username, password=password)
        """
        自动查找auth_user表，同时比对用户名和密码
        注意：
            必须同时传入用户名和密码
        """
        # print(user_obj)  # 返回的是用户对象，如果数据不符合返回None
        # print(user_obj.username)  # jonescy
        # print(user_obj.password)  # pbkdf2_sha256$216000$WJ8LDlR2SilO$uQTFFgYVeBFM9eotIqfnanPHxjTZpq3nw//ocLSQiQo=
        # 判断用户是否存在
        # print(user_obj)
        if user_obj:
            # 保存用户状态
            # print('1111')
            auth.login(request, user_obj)  # 类似于request.get_session['username'] = user_obj
            # 只要执行了该方法，就可以在任何地方铜鼓request.user获取到当前登录的用户对象
            return redirect('/home/')
    return render(request, 'login.html')


# @login_required(login_url='/login/')  # 局部配置
@login_required
def home(request):
    # print(request.user)  # 用户对象  AnonymousUser匿名用户
    # 判断用户是否登录
    if request.user.is_authenticated:
        # 自动去django_session里面查找对应的用户对象给你封装到request.user对象里面
        print(request.user)

    return HttpResponse('home')


# @login_required(login_url='/login/')

def index(request):
    if request.method == 'GET':
        # for i in request.META.items():
        #     print(i)
        return render(request, 'index.html')
    else:
        print(request.POST)
        print('body content', request.body)
        my_file = request.FILES.get('myfile')
        name = my_file.field_name
        print(type(name), name)
        # with open(my_file.name, 'wb') as f:
        #     for line in my_file:
        #         f.write(line)
        print('my middleware content', request.data)
        return HttpResponse('ok')


@login_required
def set_password(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('new_password')
        # 先校验老密码是否正确
        if request.user.check_password(old_password):
            # 先校验密码是否一致
            if new_password == confirm_password:
                #  修改密码，这里并不会影响数据库,仅操作了对象的属性
                request.user.set_password(new_password)
                # 影响数据库
                request.user.save()

        return redirect('/login/')
    return render(request, 'set_password.html', locals())


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login/')


def register(request):
    if request.method == "POST":
        print(request.POST)
        form = validation_reg_info.RegInfo(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            # 操作auth_user表写入数据
            form.cleaned_data.pop('confirm_password')
            from django.contrib.auth.models import User
            # 创建普通用户
            User.objects.create_user(**form.cleaned_data)
        else:
            print(form.errors)

        return redirect('/login/')
    return render(request, 'register.html')
