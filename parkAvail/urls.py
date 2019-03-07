from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('park_list', views.park_list, name='park_list'),
]
