from django.shortcuts import render, HttpResponse,redirect
from app01 import models
# Create your views here.


def ab_render(request):
    user_dict = {'username': 'jones', 'age': 22}
    # 第一种传值方式
    # return render(request, 'ab_render.html', {'data': user_dict, 'date': 123})
    # 第二种传值方式:当传值特别多的时候
    # locals()会将所在的名称空间中所有的名字传递给html页面
    print(locals())
    return render(request, 'ab_render.html', locals())


def login(request):
    """
    get和post请求都应该有不同的处理机制
    :param request: 请求相关的数据对象，里面有很多简易的方法
    :return:
    """
    # print(request.method)  # 返回请求方式，并且全大写形式字符串
    # if request.method == 'GET':
    #     print('来了老弟')
    #     return render(request, 'login.html', locals())
    # elif request.method == 'POST':
    #     return HttpResponse('收到了 宝贝')
    if request.method == 'POST':
        # 获取用户数据
        # print(request.POST)  # 获取用户提交的post请求数据（不包含文件）
        # <QueryDict: {'username': ['jonescy'], 'password': ['123']}>
        username = request.POST.get('username')
        password = request.POST.get('password')
        # hobby = request.POST.get('hobby')
        """
        get 只会获取最后一个元素
        getlist 获取列表
        """
        # hobby = request.POST.getlist('hobby')
        # print(hobby, type(hobby))
        # 获取用户名和密码，然后利用orm操作数，校验数据是否正确
        # 去数据库中查询数据
        user_obj = models.User.objects.filter().first()
        # 列表套数据对象
        # print(res)
        # user_obj = res[0]
        # print(user_obj)
        # print(user_obj.username)
        # print(user_obj.password)
        if user_obj:
            if password == user_obj.password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')
        # return HttpResponse('收到了 宝贝')
    # print(request.GET.get('hobby'))  # 获取用户请求数据
    # print(request.GET.getlist('hobby'))
    return render(request, 'login.html')


def reg(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 直接获取用户数据存入数据库
        # res = models.User.objects.create(username=username, password=password)
        # 返回值就是被创建对象的本身
        # print(res)
        # 第二种方式
        user_obj = models.User(username=username, password=password)
        user_obj.save()  # 保存数据
    # 先给用户返回注册页面
    return render(request, 'reg.html')


def user_list(request):
    # 查询出用户表里面的所有数据

    # 方式一
    # data = models.User.objects.filter()
    # print(data)
    # 方式二
    user_queryset = models.User.objects.all()

    # return render(request, 'userlist.html', {'user_queryset': user_queryset})
    return render(request, 'userlist.html', locals())


def edit_user(request):
    # 获取url问号后面的参数
    edit_id = request.GET.get('user_id')
    # 查询当前用户想要编辑的数据对象
    edit_obj = models.User.objects.filter(id=edit_id).first()
    print(edit_obj)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去数据库中修改对应的数据内容
        # 修改方式1：批量更新操作，能识别只修改被修改的字段
        # 将filter查询出来的列表中所有的对象全部更新
        # models.User.objects.filter(id=edit_id).update(username=username, password=password)
        # 修改方式2：局部更新，当字段特别多的时候效率非常低，从头到尾将数据的所有的字段全部更新一边，无论字段是否被修改
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.save()
        # 跳转到数据展示的页面
        return redirect('/userlist/')

    # 将数据对象展示到页面上
    return render(request, 'edit_user.html')


def del_user(request):
    # 获取用户想要删除的数据id值
    del_id = request.GET.get('user_id')
    # 二次确认功能（待增加）
    # 直接去数据库中找到对应的数据删除即可
    models.User.objects.filter(id=del_id).delete()
    """
    批量删除
    """
    # 跳转到展示页面

    return redirect('/userlist/')
