from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.home_main, name='home_main'),
    path('community/', views.Home.go_to_community, name='go_to_community'),
    
]