from django.shortcuts import render, redirect, HttpResponse
from main.verify_froms.reg import RegForm
from main import models
from django.http import JsonResponse
from django.contrib import auth
from PIL import Image, ImageFont, ImageDraw
from random import randint, choice
from io import BytesIO
from django.contrib.auth.decorators import login_required
from time import localtime


# Create your views here.


def home(request):
    return render(request, 'home.html')


def reg(request):
    # 创建前端模板的
    form_obj = RegForm()
    if request.is_ajax():
        back_dict = {'code': 200, 'msg': ''}
        form_obj = RegForm(request.POST)
        # 判断数据是否合法
        if form_obj.is_valid():
            # print(form_obj.cleaned_data)
            cleaned_data = form_obj.cleaned_data  # 校验通过的字典赋值给变量
            # 将字典里面的confirm——password键值对删除
            cleaned_data.pop('confirm_password')  # {'username': 'jonescy', 'password': '123', 'email': 'qwe@qq.com'}
            # 操作数据库保存数据
            models.Users.objects.create_user(**cleaned_data)
            back_dict['url'] = '/login/'
        else:
            back_dict['code'] = 404
            back_dict['msg'] = form_obj.errors
        return JsonResponse(back_dict)

    return render(request, 'register.html', locals())


def login(request):
    if request.is_ajax():
        back_dict = {'code': 200, 'msg': ''}
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        if request.session.get('code').lower() == code.lower():
            user_obj = auth.authenticate(username=username, password=password)
            if user_obj:

                auth.login(request, user_obj)
                back_dict['url'] = '/'
            else:
                back_dict['code'] = 201
                back_dict['msg'] = '用户名或密码错误'
        else:
            back_dict['code'] = 202
            back_dict['msg'] = '验证码错误'
        return JsonResponse(back_dict)

    return render(request, 'login.html')


def writer(request):
    return render(request, 'writer.html')


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
    return render(request, 'reset_password.html')


def get_random():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def get_code(request):
    # 推导步骤4：写图片验证码
    img_obj = Image.new('RGB', (120, 35), get_random())
    img_draw = ImageDraw.Draw(img_obj)  # 产生一个画笔对象

    img_font = ImageFont.truetype('main/static/font/222.ttf', size=20)  # 字体样式 大小
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


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def account_settings(request):
    back_dic = {'code': 200, 'msg': ''}
    if request.is_ajax():
        avatar = request.FILES.get('avatar')

        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = int(request.POST.get('phone'))
        desc = request.POST.get('desc')
        self_site = request.POST.get('self_site')

        # 存文件数据
        if avatar:
            user_obj = models.Users.objects.filter(username=request.user.username).first()
            user_obj.avatar = avatar
            user_obj.save()
            back_dic['msg'] = '更换完成'
        else:
            back_dic['code'] = 201
            back_dic['msg'] = '无图片'
        # 存入普通数据
        models.Users.objects.filter(username=request.user).update(username=username, email=email, phone=phone,
                                                                  self_site=self_site, desc=desc)
        return JsonResponse(back_dic)
    return render(request, 'account_settings.html', locals())


def date_time():
    current_year = localtime().tm_year
    current_month = localtime().tm_mon
    current_day = localtime().tm_mday
    return current_year, current_month, current_day


@login_required
def profile_settings(request):
    year = date_time()[0]
    year_list = [i for i in range(1960, year + 1)]
    month_list = [i for i in range(1, 13)]
    user_obj = models.PersonalInfo.objects.filter(user_id=request.user.id).first()
    if request.is_ajax():
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        born = request.POST.get('born')
        hometown = request.POST.get('hometown')
        location = request.POST.get('location')
        marriage = request.POST.get('marriage')
        position = request.POST.get('position')
        company = request.POST.get('company')
        work_situation = request.POST.get('work_situation')

        if not user_obj:
            models.PersonalInfo.objects.create(
                name=name,
                gender=gender,
                born=born,
                hometown=hometown,
                location=location,
                marriage=marriage,
                company=company,
                position=position,
                work_situation=work_situation,
                user_id=request.user.id
            )
        else:
            models.PersonalInfo.objects.update(
                name=name,
                gender=gender,
                born=born,
                hometown=hometown,
                location=location,
                marriage=marriage,
                company=company,
                position=position,
                work_situation=work_situation,
                user_id=request.user.id
            )

    return render(request, 'profile_settings.html', locals())


@login_required
def other_settings(request):
    if request.is_ajax():
        pass
    return render(request, 'other_settings.html', locals())
