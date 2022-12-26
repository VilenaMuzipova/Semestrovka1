from django.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^main/$', views.main, name='main'),
]