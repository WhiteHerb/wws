from django.urls import path
from . import views

urlpatterns = [
    path('', views.rater.main, name='main'),
    path('chekcsite/', views.rater.check, name='checksite'),
    path('ranksite/', views.rater.rank, name='ranksite'),
    path('addasnwersite/', views.rater.addanswer, name='addanswersite'),
    
]