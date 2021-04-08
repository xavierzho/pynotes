from django.shortcuts import render, redirect, HttpResponse
from app01.cust_forms.reg import RegForm
from app01 import models
from django.http import JsonResponse, Http404
from django.contrib import auth
from PIL import Image, ImageDraw, ImageFont
from random import randint, choice
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from json import loads
from django.db.models import F
from django.db import transaction
import os
from BBS import settings
# Create your views here.


def register(request):
    form_obj = RegForm()
    if request.method == 'POST':
        # 校验数据是否合法
        form_obj = RegForm(request.POST)
        back_dic = {'code': 1000, 'msg': ''}
        # 判断数据是否合法
        if form_obj.is_valid():

            # print(form_obj.cleaned_data)
            form_data = form_obj.cleaned_data
            form_data.pop('confirm_password')
            # 用户头像
            file_obj = request.FILES.get('avatar')
            print(file_obj)
            if file_obj:
                form_data['avatar'] = file_obj

            # 操作数据
            models.Users.objects.create_user(**form_data)
            back_dic['url'] = '/login/'
        else:
            back_dic['code'] = 2000
            back_dic['msg'] = form_obj.errors
        return JsonResponse(back_dic)
    return render(request, 'register.html', locals())


def login(request):
    if request.is_ajax():
        back_dic = {'code': 200, 'msg': ''}
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        code = request.POST.get('code')
        # 先校验验证码是否正确
        if request.session.get('code').lower() == code.lower():
            # 比对用户名和密码是否正确
            user_obj = auth.authenticate(request, username=username, password=password)
            # print(user_obj.username)
            # print(user_obj.password)
            if user_obj:

                # if not user_obj.username:
                #     back_dic['code'] = 201
                #     back_dic['msg'] = '用户名错误'
                # elif not user_obj.password:
                #     back_dic['code'] = 202
                #     back_dic['msg'] = '密码错误'
                # else:
                # 保存用户状态
                auth.login(request, user_obj)
                back_dic['url'] = '/'
            else:
                back_dic['code'] = 202
                back_dic['msg'] = '用户名或密码错误'
        else:
            back_dic['code'] = 203
            back_dic['msg'] = '验证码错误'
        return JsonResponse(back_dic)
    return render(request, 'login.html')


"""
图片相关的模块
    pip install pillow
Image:生成图片
ImageDraw：能够再图片上涂画
ImageFont：控制字体样式
"""

"""
BytesIO:临时帮你存储数据，返回的是二进制数据
StringIO：临时存储数据，返回的是字符串

"""


def get_random():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def get_code(request):
    # 推到步骤1：直接获取后端现成的图片二进制数据发送给前端
    # with open('static/img/verify_code/111.jpg', mode='rb') as f:
    #     data = f.read()
    # return HttpResponse(data)

    # # 推到步骤2：利用pillow模块动态生成图片
    # img_obj = Image.new('RGB', (120, 35), get_random())

    # # 先将图片对象保存起来
    # with open('static/img/verify_code/123.png', mode='wb') as f:
    #     img_obj.save(f, 'png')
    # # 将图片对象读取出来
    # with open('static/img/verify_code/123.png', mode='rb') as f:
    #     data = f.read()
    #
    # return HttpResponse(data)

    # # 推到步骤3：文件存储繁琐IO操作效率低，借助于内存管理模块
    # img_obj = Image.new('RGB', (120, 35), get_random())
    # io_obj = BytesIO()  # 生成一个内存管理器对象
    # img_obj.save(io_obj, 'png')
    # return HttpResponse(io_obj.getvalue())  # 从内存管理器中读取图片二进制数据
    #

    # 推导步骤4：写图片验证码
    img_obj = Image.new('RGB', (120, 35), get_random())
    img_draw = ImageDraw.Draw(img_obj)  # 产生一个画笔对象

    img_font = ImageFont.truetype('app01/static/font/222.ttf', size=20)  # 字体样式 大小
    # 随机验证码（五位数--包含：数字，小写字母，大写字母）
    code = ''
    for i in range(5):
        random_upper = chr(randint(65, 90))
        random_lower = chr(randint(97, 122))
        random_int = str(randint(0, 9))
        # 从上面三个里面随机选择一个
        tmp = choice([random_lower, random_int, random_upper])
        # 将产生的随机字符串写入到图片上
        """
        为什么一个个写而不是写好之后再写？
        因为一个个写能够控制每个字体的间隙，生成好之后再写间隙无法控制
        """
        img_draw.text((i * 20, 8), tmp, get_random(), img_font)
        # 拼接字符串
        code += tmp

    print(code)
    # 随机验证码再登录的视图函数里面需要用到比对是否正确，所以要找地方存起来，其他视图也能拿到
    request.session['code'] = code
    io_obj = BytesIO()
    img_obj.save(io_obj, 'png')
    return HttpResponse(io_obj.getvalue())


def home(request):
    # 查询本网站所有的文章数据，这里可以使用分页器
    article_queryset = models.Article.objects.all()

    return render(request, 'home.html', locals())


@login_required
def writer(request):
    category_list = models.Category.objects.filter(self_site=request.user.self_site)
    tag_list = models.Tags.objects.filter(self_site=request.user.self_site)

    return render(request, 'writer.html', locals())


@login_required
def add_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        tag_list = request.POST.getlist('tag')
        # 文章简介
        # 直接切取content150个字符
        desc = content[0:150]
        article_obj = models.Article.objects.create(title=title, content=content, desc=desc, category_id=category_id,
                                                    self_site=request.user.self_site)
        # 文章和标签的关系表是我们自己创建的，无法用add set remove clear方法
        # 自己去操作关系表 一次性可能创建多条数据，批量插入
        article_obj_list = []
        for i in tag_list:
            article_obj_list.append(models.Article2Tag(article=article_obj, tag_id=i))
        # 批量插入
        models.Article2Tag.objects.bulk_create(article_obj_list)
        # 跳转到后台管理文章展示页
        return redirect('')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def reset_password(request):
    back_dic = {'code': 200, "msg": ''}
    if request.is_ajax():
        if request.method == "POST":
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')
            is_right = request.user.check_password(old_password)
            if is_right:
                if new_password == confirm_new_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    back_dic['msg'] = '修改成功'
                else:
                    back_dic['code'] = 401
                    back_dic['msg'] = '两次密码不相同'
            else:
                back_dic['code'] = 402
                back_dic['msg'] = '旧密码不正确'
        return JsonResponse(back_dic)


def site(request, username, *args, **kwargs):
    # 先校验当前用户的个人站点是否存在
    user_obj = models.Users.objects.filter(username=username).first()
    # 用户存在返回404页面
    if not user_obj:
        return render(request, 'error404.html')
    blog = user_obj.self_site
    # 查询个人站点下的所有文章
    article_list = models.Article.objects.filter(self_site=blog)
    # 判断是否有值
    if kwargs:
        # print(kwargs)  # {'condition': 'tag|category|archive', 'param':1}
        condition = kwargs.get('condition')
        param = kwargs.get('param')
        # 判断用户想按照哪个条件
        if condition == 'category':
            article_list = article_list.filter(category_id=param)
        elif condition == 'tag':
            article_list = article_list.filter(tags__id=param)
        else:
            year, month = param.split('-')  # 2020-11 [2020,11]
            article_list = article_list.filter(publish_time__year=year, publish_time__month=month)

    # # 1.查询当前用户下的所有分类以及分类下的文章数
    # categories = models.Category.objects.filter(self_site=blog).annotate(count_num=Count('article__pk')).values_list('name', 'count_num', 'pk')
    # # print(categories)
    # # 2.查询当前用户下所有的标签以及标签下的文章数
    # tags = models.Tags.objects.filter(self_site=blog).annotate(count_num=Count('article__pk')).values_list('name', 'count_num', 'pk')
    # # print(tags)

    return render(request, 'site.html', locals())


def article_detail(request, username, article_id):
    """
    需要校验username 和article_id是否存在，但是我们这里先只完成正确的情况
    :param request:
    :param username:
    :param article_id:
    :return:
    """
    # 查询文章对象
    user_obj = models.Users.objects.filter(username=username).first()
    blog = user_obj.self_site
    article_obj = models.Article.objects.filter(pk=article_id, blog__users__username=username).first()
    if not article_obj:
        return render(request, 'error404.html')
    # 获取当前文章的所有的评论内容
    comment_list = models.ArticleComment.objects.filter(article=article_obj)
    return render(request, 'article_detail.html', locals())


def up_or_down(request):
    """
    1.校验用户是否登录
    2.自己不能给自己的文章点赞点踩
    3.当前用户是否以及给当前文章点过了
    4.操作数据
    :param request:
    :return:
    """
    if request.is_ajax():
        back_dic = {'code': 200, 'msg': ''}
        # 1.判断用户是否登录
        if request.user.is_authenticated:

            article_id = request.POST.get('article_id')
            is_up = request.POST.get('is_up')
            # if is_up == 'true':
            #     is_up = True
            # elif is_up == 'false':
            #     is_up = False
            is_up = loads(is_up)
            # 2.判断当前用户是否自己写的
            article_obj = models.Article.objects.filter(pk=article_id).first()
            if not article_obj.self_site.users == request.user:
                # 3.校验当前用户是否已经点击
                is_click = models.UpOrDown.objects.filter(user=request.user, article=article_obj)
                if not is_click:
                    # 4.操作数据库记录数据
                    # 判断当前用户点了赞还是踩，从而给哪个字段+1
                    if is_up:
                        # 给点赞数+1
                        models.Article.objects.filter(pk=article_id).update(up_num=F('up_num') + 1)
                        back_dic['msg'] = '点赞成功'
                    else:
                        # 给点踩数+1
                        models.Article.objects.filter(pk=article_id).update(down_num=F('down_num') + 1)
                        back_dic['msg'] = '点踩成功'
                    # 操作点赞点踩表
                    models.UpOrDown.objects.create(user=request.user, article=article_obj, is_up=is_up)
                else:
                    back_dic['code'] = 201
                    back_dic['msg'] = '你已经点过了'
            else:
                back_dic['code'] = 202
                back_dic['msg'] = '自己不能给自己评价哦！'
        else:
            back_dic['code'] = 203
            back_dic['msg'] = '请先<a href="/login/">登录</a>'
        return JsonResponse(back_dic)


def comment(request):
    if request.is_ajax():
        if request.method == "POST":
            back_dic = {'code': 200, 'msg': ''}
            if request.user.is_authenticated:
                article_id = request.POST.get('article_id')
                content = request.POST.get('comment')
                parent_id = request.POST.get('parent_id')
                # 直接操作评论表存储数据  两张表需要操作
                with transaction.atomic():
                    models.Article.objects.filter(pk=article_id).update(comment_num=F('comment_num') + 1)
                    models.ArticleComment.objects.create(user=request.user, article_id=article_id, content=content,
                                                         parent_id=parent_id)
                back_dic['msg'] = '评论成功'
            else:
                back_dic['code'] = 201
                back_dic['msg'] = '用户为登录'
            return JsonResponse(back_dic)


def upload_img(request):
    back_dic = {'error': 0, 'message': ''}  # 提前定义给编辑返回的格式

    # 用户写的文章上传的图片，也算静态资源，也应该放到media文件夹下
    if request.method == 'POST':
        # 获取用户上传的图片数据、对象
        file_obj = request.FILES.get('imgFile')
        # 手动拼接存储路径
        file_dir = os.path.join(settings.BASE_DIR, 'media', 'article_img')
        # 优化操作 先判断当前文件夹是否存在
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir)
        # 拼接图片的完整路径
        file_path = os.path.join(file_dir, file_obj.name)
        with open(file_path, 'wb') as f:
            for line in file_obj:
                f.write(line)
        back_dic['url'] = f'/media/article_img/{file_obj.name}'
    return JsonResponse(back_dic)
