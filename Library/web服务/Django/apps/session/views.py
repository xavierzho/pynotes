from django.shortcuts import redirect, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator  # CBV加装饰器


# Create your views here.
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


"""
CBV中django不建议你直接给类的方法添加装饰器
无论装饰器是否影响正常的工作
"""


# 校验用户是否登录的装饰器
def login_auth(function):
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()
        if request.COOKIES.get('username'):
            return function(request, *args, **kwargs)
        else:
            return redirect(f'/app02/login/?next={target_url}')

    return inner


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


@method_decorator(csrf_protect, name='post')  # 针对csrf_protect，第二种方式也可行
# @method_decorator(csrf_exempt, name='post')  # 针对csrf_exempt,第二种方式不可行
class MyCsrfToken(View):
    # @method_decorator(csrf_protect)  # 针对csrf_protect，第三种方式也可行
    # @method_decorator(csrf_exempt)  # 针对csrf_exempt,第三种方式可行
    def dispatch(self, request, *args, **kwargs):
        return super(MyCsrfToken, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('get')

    # @method_decorator(csrf_protect)  # 针对csrf_protect，第一种方式可行
    # @method_decorator(csrf_exempt)  # 针对csrf_exempt, 第一种方式不行
    def post(self, request):
        return HttpResponse('post')


