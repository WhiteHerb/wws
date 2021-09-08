from django.urls import path
from . import views

urlpatterns = [
    path('', views.community.post_list, name='post_list'),
    path(r'post/<int:pk>/', views.community.post_detail, name='post_detail'),
    path('post/new/',views.community.post_new, name='post_new'),
]