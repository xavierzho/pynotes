
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from app01 import models
from django.core import serializers


# Create your views here.


def ab_ajax(request):
    if request.method == "POST":
        # print(request.POST)  # <QueryDict: {'username': ['jones'], 'password': ['123']}>
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        # 转成整型相加
        res = int(i1) + int(i2)
        d = {'code': 100, 'msg': res}
        return HttpResponse(json.dumps(d))
        # return JsonResponse(d)
    return render(request, 'index.html')


def index(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
    return render(request, 'index2.html')


def send_json(request):
    if request.is_ajax():
        # print(request.FILES)
        # print(request.body)  # b'{"username":"jones","age":123}'
        json_bytes = request.body
        # json_str = json_bytes.decode('utf-8')
        # json_dict = json.loads(json_str)
        # print(json_dict, type(json_dict))
        # json.loads()可以自动解码,然后反序列化
        json_dict = json.loads(json_bytes)
        print(json_dict, type(json_dict))
    return render(request, 'send_json.html')


def send_file(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)

    return render(request, 'send_file.html')


def ab_ser(request):
    user_queryset = models.User.objects.all()
    # # 构造数据
    # user_list = []
    # for user_obj in user_queryset:
    #     tmp = {
    #         'pk': user_obj.pk,
    #         'username': user_obj.username,
    #         'age': user_obj.age,
    #         'gender': user_obj.get_gender_display()
    #     }
    #     user_list.append(tmp)
    # # return render(request, 'ab_ser.html', locals())
    # return JsonResponse(user_list, safe=False)

    # 序列化组件
    res = serializers.serialize('json', user_queryset)
    return HttpResponse(res)


def botch(request):
    # # 给book表插入1W条数据
    # for i in range(10000):
    #     models.Book.objects.create(title='第%s本书' % i)
    # # 再将所有的数据查询并展示到前端页面
    # book_queryset = models.Book.objects.all()

    # # 批量插入
    # book_list = []
    # for i in range(100000):
    #     book_obj = models.Book(title=f'第{i}本书')
    #     book_list.append(book_obj)
    # # 使用orm提供的bulk_create能够大大的减少操作时间
    # models.Book.objects.bulk_create(book_list)

    # # 分页
    #
    # # 想访问那一页
    # current_page = request.GET.get('page', 1)  # 如果获取不到页码,默认展示第一页
    # # 数据类型转换
    # try:
    #     current_page = int(current_page)
    # except Exception:
    #     current_page = 1
    # # 每页返回多少条
    # per_page_num = 10
    # # 起始位置
    # start_page = (current_page-1) * per_page_num
    # # 终止位置
    # end_page = current_page * per_page_num
    # book_list = models.Book.objects.all()
    # # 计算到底需要多少页
    # all_count = book_list.count()
    # page_count, more = divmod(all_count, per_page_num)
    # if more:
    #     page_count += 1
    #
    # page_html = ''
    # xxx = current_page
    # if current_page < 6:
    #     current_page = 6
    # for i in range(current_page-5, current_page+6):
    #     if xxx == i:
    #         page_html += f'<li class="active"><a href="?page={i}">{i}</a></li>'
    #     else:
    #         page_html += f'<li><a href="?page={i}">{i}</a></li>'
    # book_queryset = book_list[start_page: end_page]
    from utils.pager import Pagination
    book_queryset = models.Book.objects.all()
    # 1.实例化传值生成对象
    page_obj = Pagination(current_page=request.GET.get('page', 1), all_count=book_queryset.count())
    # 2.直接对总数据进行切片操作
    page_queryset = book_queryset[page_obj.start: page_obj.end]
    return render(request, 'botch.html', locals())


def reg(request):
    back_dic = {'username': '', 'password': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        if 'jinpingmei' in username:
            back_dic['username'] = '不符合社会用户名要求'
        if len(password) < 3:
            back_dic['password'] = '密码太短了不安全'
    """
    无论是post还是get请求
    页面都能获取到字典，只不过get请求过来的时候字典是空的
    """
    return render(request, 'reg.html', locals())


from django import forms


class MyForms(forms.Form):
    # username 和password 都是最小三位，最大8位
    username = forms.CharField(min_length=3,
                               max_length=8,
                               label='用户名',
                               error_messages={
                                   'min_length': '用户名最少3位',
                                   'max_length': "用户名最大8位",
                                   'required': '用户名不能为空',
                               },
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control',})
                               )
    password = forms.CharField(min_length=3,
                               max_length=8,
                               label='输入密码',
                               error_messages={
                                   'min_length': '密码最少3位',
                                   'max_length': "密码最大8位",
                                   'required': '密码不能为空',
                               },
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control',})
                               )
    confirm_password = forms.CharField(min_length=3,
                                       max_length=8,
                                       label='再次输入密码',
                                       error_messages={
                                           'min_length': '密码最少3位',
                                           'max_length': "密码最大8位",
                                           'required': '确认密码不能为空',
                                       },
                                       widget=forms.widgets.PasswordInput(attrs={'class': 'form-control ', })
                                       )
    # email字段必须符合邮箱格式 xxx@qq.com
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'required': '邮箱不能为空',
            'invalid': '邮箱格式不正确'
        },
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    from django.core.validators import RegexValidator
    phone = forms.CharField(
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )

    # 钩子函数
    # 局部钩子
    def clean_username(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        if '666' in username:
            # 提示前端展示错误信息
            # 错误提示1
            # self.add_error('username', '光喊666是不行的')
            # 错误提示2:一般不用
            from django.core.exceptions import ValidationError
            raise ValidationError('光喊666是不行的')
        # 将钩子函数勾出来的数据，返回
        return username

    # 全局钩子
    def clean(self):
        # 获取字段
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password == password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data


def render_tag(request):
    # 1.产生一个空对象
    form_obj = MyForms()
    if request.method == 'POST':
        # 3.获取用户数据并校验
        form_obj = MyForms(request.POST)
        # 4.判断数据是否合法
        if form_obj.is_valid():
            # 5.如果合法操作数据库
            return HttpResponse('OK')
        # 6.不合法有错误的情况
        else:
            # 将错误信息展示到前端
            form_obj.errors
    # 2.直接将该空对象传递给html页面
    return render(request, 'render_tag.html', locals())
