from django.test import TestCase
import os
from pathlib import Path
# Create your tests here.
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(__file__))
# print(os.path.join(os.path.abspath(__file__), 'site_theme'))
# print(os.path.join(os.path.dirname(__file__), 'site_theme'))
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BBS.settings')
    import django
    django.setup()
    from app01 import models
    # user_obj = models.Users.objects.filter(username='tank').first()
    # blog = user_obj.self_site
    # article_list = models.Article.objects.filter(self_site=blog)
    # print(article_list)
    from django.db.models.functions import TruncMonth
    from django.db.models import Count
    data_queryset = models.Article.objects.annotate(month=TruncMonth('publish_time')).values('month').annotate(count_num=Count('id')).values_list('month', 'count_num')
    print(data_queryset)
    for i in data_queryset:
        print(i)
