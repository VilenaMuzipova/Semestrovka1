from django.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    #path('', views.main, name='main'),
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),

]