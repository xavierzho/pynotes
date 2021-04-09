from django.shortcuts import render, redirect, reverse
from apps.books import models
from apps.books.componets.pager import Pagination


def home(request):
    return render(request, 'home.html')


# Create your views here.
def book_list(request):
    # 查询所有书籍的信息
    book_queryset = models.Book.objects.all()

    return render(request, 'book_list.html', locals())


def book_add(request):
    if request.method == 'POST':
        # 获取前端提交过来的所有数据
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        # 获取作者列表
        author_list = request.POST.getlist('author')
        # orm操作数据库存储数据
        # 书籍表
        # print(publish_id)
        book_obj = models.Book.objects.create(title=title, price=price, publish_date=publish_date,
                                              publish_id=publish_id)
        # 书籍和作者关系表,*表示打散列表
        book_obj.author.add(*author_list)
        # 跳转到书籍列表页面
        """
        redirect括号内可以写别名，也可以写路径
        但是如果别名需要额外给参数的话，就必须使用reverse()
        """
        return redirect(reverse("books_list"))
    # 获取系统中出版社信息和作者信息
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()

    return render(request, 'book_add.html', locals())


def book_edit(request, edit_id):
    # 获取当前用户要编辑的对象，展示给用户看
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        # 获取作者列表
        author_list = request.POST.getlist('author')
        # 修改数据
        models.Book.objects.filter(pk=edit_id).update(title=title,
                                                      price=price,
                                                      publish_date=publish_date,
                                                      publish_id=publish_id
                                                      )
        edit_obj.author.set(author_list)
        return redirect('books_list')
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'book_edit.html', locals())


def book_del(request, del_id):
    # 直接删除
    models.Book.objects.filter(pk=del_id).delete()
    # 跳转到展示页
    return redirect(reverse("books_list"))


# 自定义分页器
def botch(request):
    book_queryset = models.Book.objects.all()
    # 1.实例化传值生成对象
    page_obj = Pagination(current_page=request.GET.get('page', 1), all_count=book_queryset.count())
    # 2.直接对总数据进行切片操作
    page_queryset = book_queryset[page_obj.start: page_obj.end]
    return render(request, 'botch.html', locals())
