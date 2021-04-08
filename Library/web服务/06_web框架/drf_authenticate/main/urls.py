from django.urls import path
from main import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', views.BookView)
urlpatterns = [
    path('login/', views.Login.as_view()),
    path('test/', views.TestView.as_view()),
    path('test2/', views.TestSuperUser.as_view()),
    path('test3/', views.TestAnonUser.as_view()),
    path('test4/', views.TestAnonUser2.as_view()),
    path('test5/', views.TestLoginUser.as_view()),
    path('test6/', views.TestFilter.as_view()),
    path('test7/', views.TestOrdering.as_view()),
    path('test8/', views.TestView8.as_view()),
    path('test9/', views.TestView9.as_view()),

]
urlpatterns += router.urls
