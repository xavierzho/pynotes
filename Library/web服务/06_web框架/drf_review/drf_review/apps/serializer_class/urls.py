from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('books', views.BookView)
urlpatterns = [
    path('', include(router.urls))
]
