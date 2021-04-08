from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models


# Create your views here.
def func(request, year):
    return HttpResponse('func')


def index(request, args):
    return HttpResponse('index')


def home(request):
    # print(reverse('xxx')) 报错
    # print(reverse('xxx', args=(1,)))  # 需要指定参数
    # 有名分组反向解析，方法1
    # print(reverse('ooo', kwargs={'year': 123}))
    # 简便写法
    # print(reverse('ooo', args=(123,)))
    print(reverse(''))
    return render(request, 'home.html')


def user_list(request):
    user_queryset = models.User.objects.all()
    return render(request, 'userList.html', locals())


def edit(request, modify):

    print(reverse('app01_edit', args=(modify,)))
    edit_obj = models.User.objects.filter(id=modify).first()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.User.objects.filter(id=modify).update(username=username, password=password)
        return redirect('/app01/user list/')
    return render(request, 'edit.html', locals())


def delete(request, del_id):
    models.User.objects.filter(id=del_id).delete()
    return redirect('/app01/user list/')


def search(request, edit_id):
    # user_queryset = models.User.objects.all()
    return render(request, 'userList.html', locals())


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = models.User.objects.filter(username=username).first()
        if user_obj:
            if password == user_obj.password:
                return render(request, 'home.html')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')
    return render(request, 'login.html')


def register(request):
    print(reverse('app01:reg'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询数据
        user_obj = models.User.objects.filter(username=username).first()
        if user_obj:
            if username == user_obj.username:
                return HttpResponse("用户已存在")
            else:
                models.User.objects.create(username=username, password=password)

    return render(request, 'reg.html')
