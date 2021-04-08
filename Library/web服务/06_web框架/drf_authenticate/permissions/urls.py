from django.urls import path
from permissions import views

urlpatterns = [
    path('books/', views.BookView.as_view())
]
