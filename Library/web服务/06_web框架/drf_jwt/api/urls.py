from api import views
from django.urls import path


urlpatterns = [
    path('test/', views.test_cache),
    path('test2/', views.test_cache2),

]