from django.urls import path
from . import views

urlpatterns = [
    path('show', views.rankcal.main, name='main'),
    path('', views.rankcal.backmain, name='backmain')
    
]