"""testdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name=''),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),

    path('reg',views.reg,name='reg'),
    path('getform',views.getform,name='getform'),

    path('more',views.more,name='more'),
    path('moredata',views.moredata,name='moredata'),
    path('more_update',views.more_update,name='more_update'),

    path('action',views.action,name='action'),
    path('edit',views.edit,name='edit'),

    path('upload_product',views.upload_product,name='upload_product'),
    path('uploaddata',views.uploaddata,name='uploaddata'),

    path('signup', views.signup, name='signup'),
    path('reguser',views.reguser,name='reguser'),
    path('loginform',views.loginform,name='loginform'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logoutuser',views.logoutuser,name='loguotuser'),

    path('ajax',views.ajax,name='ajax'),
    path('create',views.create,name='create'),

    path('show',views.show,name='show'),
    path('delete',views.delete,name='delete')



]
