import os
from django.shortcuts import render
from django.http.response import JsonResponse
from Django import settings
from . import models
from json import loads
from django.db.models import F
from django.db import transaction


# Create your views here.
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
