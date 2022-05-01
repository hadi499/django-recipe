from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('detail/<int:pk>/', views.detail, name='blog-detail'),
]
