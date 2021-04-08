from django.contrib import admin
from app01 import models
# Register your models here.


admin.site.register(models.Users)
admin.site.register(models.Article)
admin.site.register(models.SelfSite)
admin.site.register(models.Tags)
admin.site.register(models.Category)
admin.site.register(models.UpOrDown)
admin.site.register(models.ArticleComment)
admin.site.register(models.Article2Tag)


