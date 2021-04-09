from django import template
from apps.article import models
from django.db.models import Count
from django.db.models.functions import TruncMonth

register = template.Library()


# 自定义inclusion_tag
@register.inclusion_tag('left_menu.html')
def left_menu(username):
    # 构造侧边栏需要的数据
    user_obj = models.Users.objects.filter(username=username).first()

    blog = user_obj.self_site
    # 查询个人站点下的所有文章
    article_list = models.Article.objects.filter(self_site=blog)
    # 1.查询当前用户下的所有分类以及分类下的文章数
    categories = models.Category.objects.filter(self_site=blog).annotate(count_num=Count('article__pk')).values_list(
        'name', 'count_num', 'pk')
    # print(categories)
    # 2.查询当前用户下所有的标签以及标签下的文章数
    tags = models.Tags.objects.filter(self_site=blog).annotate(count_num=Count('article__pk')).values_list('name',
                                                                                                           'count_num',
                                                                                                           'pk')

    # 默认的
    data_queryset = models.Article.objects.annotate(month=TruncMonth('publish_time')).values('month').annotate(count_num=Count('id')).values_list('month', 'count_num')

    return locals()
