from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.


def test(request, asd):
    print(asd)
    return HttpResponse('test')


def testadd(request, year):
    print(year)
    return HttpResponse('testadd')


def home(request):
    print(reverse('ooo'))
    return render(request, 'home.html')


def error(request):
    return HttpResponse('NOT FOUND 404')


def index(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse('index')


def func(request):
    return HttpResponse('func')