"""
@Author: Jonescyna@gmail.com
@Created: 2021/4/9
"""
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view())
]