from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subjects/', views.subjects, name='subjects'),
    path('resources/<str:subject>/', views.resources, name='resources'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]