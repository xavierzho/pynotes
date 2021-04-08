from django.shortcuts import render, HttpResponse, redirect


# 校验用户是否登录的装饰器
def login_auth(function):
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()
        if request.COOKIES.get('username'):
            return function(request, *args, **kwargs)
        else:
            return redirect(f'/app02/login/?next={target_url}')

    return inner


# Create your views here.
@login_auth
def home(request):
    # 获取cookie信息 判断有没有，没有不让你登录
    # if request.COOKIES.get('username') == 'jones':
    #     return render(request, 'home.html')
    # return render(request, 'login.html')
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'jones' and password == '123':
            # 获取用户上一次想要访问的url
            target_url = request.GET.get('next')  # 可能为None
            if target_url:
                obj = redirect(target_url)
            else:
                # 保存用户登录状态
                obj = redirect('/app02/')
            # 让浏览器记录cookie数据,max_age,expires,都是设置超时时间，以秒为单位，expires针对ie浏览器
            obj.set_cookie('username', username)
            # 跳转到一个需要用户登录之后的页面
            return obj
    return render(request, 'login.html')


@login_auth
def index(request):
    return HttpResponse('我是index页面，只有登录过后才能看的哦')


@login_auth
def func(request):
    return HttpResponse('我是func页面，只有登录过后才能看的哦')


@login_auth
def logout(request):
    obj = redirect('app02_home')
    obj.delete_cookie('username')
    return obj


def set_session(request):
    request.session['hobby'] = 'girl1'
    request.session['hobby2'] = 'girl2'
    request.session['hobby3'] = 'girl3'
    request.session['hobby4'] = 'girl4'
    request.session['hobby5'] = 'girl5'
    """
    内部发生了什么事？
        1.django会自动生成一个随机字符串
        2.django内部自动将随机字符串和对应的数据存储到django_session表中
            2.1先在内存中生成数据的缓存
            2.2在响应结果django中间件的时候才真正操作数据库
        3.将返回的随机字符串返回给客户端浏览器保存
    
    """
    return HttpResponse('嘿嘿嘿')


def get_session(request):
    if request.session.get('hobby'):
        print(request.session)
        # print(request.session.get('hobby1'))
        # print(request.session.get('hobby2'))
        # print(request.session.get('hobby3'))
        # print(request.session.get('hobby4'))
        # print(request.session.get('hobby5'))
    # request.session.set_expiry()

    """
    内部发生了什么事
        1.自动从浏览器请求中获取sessionid对应的随机字符串
        2.拿着随机字符串取django_session表中查找对应的数据
        3.如果比对上，则将对应的数据取出，并以字典的形式封装到request.session中
            如果比对不上，则request.session.get()返回None
    """

    return HttpResponse('关门了')


def del_session(request):
    request.session.flush()
    return HttpResponse('过期了')


from django.views import View
from django.utils.decorators import method_decorator
"""
CBV中django不建议你直接给类的方法添加装饰器
无论装饰器是否影响正常的工作
"""


# @method_decorator(login_auth, name='post')
# @method_decorator(login_auth, name='get')
class MyLogin(View):
    @method_decorator(login_auth)  # 方式三：他会直接作用于当前类所有的方法
    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        """
        看CBV源码可以得出，CBV里面所有的方法在执行之前都需要经过
        dispatch方法，（该方法看成是一个路由分发方法）
        """
    # @method_decorator(login_auth)  # 方式一
    def get(self, request):
        return HttpResponse('get请求')

    def post(self, request):
        return HttpResponse('post请求')

