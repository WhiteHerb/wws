from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.accounts.signup_main, name='signup_main'),
    path('login/', views.accounts.login_main, name='login_main'),
    path('logout/', views.accounts.logout_main, name='logout_main'),
    path('school/',views.accounts.set_school, name='set_school'),
]