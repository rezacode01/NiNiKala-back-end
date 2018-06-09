"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('khaneBeDoosh/api/v2/auth/profile', views.profile, name='profile'),
    path('khaneBeDoosh/api/v2/login', views.login, name='login'),
    path('khaneBeDoosh/api/v2/house', views.search, name='search'),
    path('khaneBeDoosh/api/v2/house/bonten/1000', views.product, name='product'),
    path('khaneBeDoosh/api/v2/auth/charge', views.charge, name='charge'),
    path('khaneBeDoosh/api/v2/auth/add-to-card', views.addToCard, name='addToCard'),

]
