from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.

def home(request):
    print('我是app03视图函数里面的home')
    obj = HttpResponse('app03——home')
    def render():
        print('内部的render')
        return HttpResponse('O98K')

    obj.render = render
    return obj


# @csrf_protect
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        target_user = request.POST.get('target_user')
        money = request.POST.get('money')
        print(f'{username}给{target_user}转了{money}元')
    return render(request, 'transfer.html')


# CBV加装饰器
from django.views import View
from django.utils.decorators import method_decorator


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
