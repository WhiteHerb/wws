from django.urls import path
from . import views

urlpatterns = [
    path('', views.rankcal.main, name='main'),
    
]