"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf goes here ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls'), name='community'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('', home.views.Home.home_main, name='home'),
    path('home/', include('home.urls'), name='home'),
    path('rater/', include('rater.urls'), name='rater'),
    path('rankcal/', include('rankcal.urls'), name='rankcal'),
]
urlpatterns += staticfiles_urlpatterns()
