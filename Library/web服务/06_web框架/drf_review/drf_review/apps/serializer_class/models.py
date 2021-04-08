from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        abstract = True


class Book(BaseModel):
    language_choice = (
        (1, '简体中文'),
        (2, '繁体中文'),
        (3, '英文'),
        (4, '德文'),
        (5, '甲骨文'),
    )
    name = models.CharField(max_length=32, unique=True)
    publish = models.ForeignKey(to="Publish", on_delete=models.PROTECT, db_constraint=False)
    authors = models.ManyToManyField(to='Author', db_constraint=False)
    brief = models.CharField(max_length=64, null=True)
    publish_date = models.DateField(default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    language = models.IntegerField(choices=language_choice, default=1)

    class Meta:
        verbose_name_plural = '图书表'

    def __str__(self):
        return self.name

    @property
    def language_name(self):
        return self.get_language_display()

    # @property
    # def publish_name(self):
    #     return self.publish.name

    @property
    def author_list(self):
        lis = []
        authors_obj = self.authors.all()
        for author in authors_obj:
            lis.append(author.name)
        return lis


class Publish(BaseModel):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64, unique=False, default=None)
    email = models.EmailField(default=None)

    class Meta:
        verbose_name_plural = '出版社表'

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=32)
    country_fullname = models.CharField(max_length=32, null=True)
    country_symbol = models.CharField(max_length=10, null=True)
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE, db_constraint=False)

    class Meta:
        verbose_name_plural = '作者表'

    def __str__(self):
        return self.name


class AuthorDetail(BaseModel):
    age = models.IntegerField()
    phone = models.CharField(max_length=18, unique=False)
    addr = models.CharField(max_length=64, unique=False)

    class Meta:
        verbose_name_plural = '作者详情表'

    def __str__(self):
        return self.phone
