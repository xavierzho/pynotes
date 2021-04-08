from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
router = SimpleRouter()
router.register('', views.LoginView, 'login')
router.register('register', views.Register, 'register')
urlpatterns = [
    path('', include(router.urls))
]
