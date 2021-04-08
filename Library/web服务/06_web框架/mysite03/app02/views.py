from django.shortcuts import render, HttpResponse, redirect, reverse


# Create your views here.
def reg(request):
    # 名称空间解析
    # print(reverse('app02:reg'))
    return render(request, 'reg1.html')


def home(request):
    return render(request, 'home.html')


def index(request):
    # The view app02.views.index didn't return an HttpResponse object. It returned None instead.
    # 没有返回一个对象
    from django.template import Template, Context
    res = Template('<h1>{{ user }}</h1>')
    conn = Context({'user': {'username': 'jones', 'password': 12313}})
    ret = res.render(conn)
    print(ret)
    return HttpResponse(ret)


def ab_json(request):
    user_dict = {'username': 'jones好帅我好喜欢！', 'password': 12313, 'hobby': 'girl'}
    # import json
    # # 转化成json格式字符串
    # json_str = json.dumps(user_dict)
    # # 将该字符串返回
    from django.http import JsonResponse
    # # 读源码掌握用法
    # return JsonResponse(user_dict, json_dumps_params={'ensure_ascii': False})
    lis = [11, 22, 33, 44, 55]
    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    return JsonResponse(lis, safe=False)


def ab_file(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)  # 获取文件数据
        # file_obj = request.FILES.get('file')  # 文件对象
        # print(file_obj.name)  # 获取文件名
        # 保存方式
        # with open(file_obj.name, 'wb') as f:
        #     for line in file_obj.chunks():
        #         f.write(line)
        print(request.body)
    # print(request.path)
    # print(request.path_info)
    #
    # print(request.get_full_path())

    return render(request, 'form.html')


from django.views import View


class MyLogin(View):
    def get(self, request):
        return render(request, 'login1.html')

    def post(self, request):
        return HttpResponse('post方法')


class MyIndex(View):
    def get(self, request):
        # 模板语法可以传递的后端python数据类型
        n = 123
        f = 1221.121
        s = 'qwiije'
        l = ['123', '23', 'saj', '123', '敏敏', '新新']
        t = (111, 333, 44, 55, 77)
        b = False
        d = {'username': 'jones', 'age': 22, 'info': '这个人有点意思', 'hobby': ['1231', 213, 231, {'info': 666}]}
        se = {'jji', 'yangyang', 'wusuowei'}

        def func(xxx):
            return '我被执行了'

        class MyClass(object):
            def get_self(self):
                return 'self'

            @staticmethod
            def get_func():
                return 'func'

            @classmethod
            def get_class(cls):
                return 'cls'

            # 对象被展示到前端页面上，相当于打印了，所以页会执行__str__
            def __str__(self):
                return '到底会不会执行__str__'

            # 实例化对象就会执行
            def __call__(self, *args, **kwargs):
                return '会不会执行__call__'

        obj = MyClass()
        file_size = 123123543
        import datetime
        current_time = datetime.datetime.now()
        info = '工欲善其事必先利其器。像我们从零开始撸一个App的话，选择最合适的语言是首要任务。如果你跟我一样对Java蹒跚的步态和僵硬的语法颇感无奈，那么Kotlin在很大程度上不会令你失望。虽然为了符合JVM规范和兼容Java，它引入了一些较为复杂的概念和语法，很多同学就是因此放弃入门。其实越深入进去，就会越 ...'
        egl = 'my name is jones,my age is 18 am form china'
        msg = 'I love you and you?'
        hhh = '<h1>敏敏</h1>'
        sss = '<script>alert(123)</script>'
        from django.utils.safestring import mark_safe
        hhh2 = mark_safe('<script>alert(123)</script>')
        ll = []
        return render(request, 'index.html', locals())

    def post(self, request):
        return HttpResponse('post方法')
