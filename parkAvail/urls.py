from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('park_list', views.park_list, name='park_list'),
    path('park_new', views.park_new, name='park_new'),
    path('property_new', views.property_new, name='property_new'),
    #path('park/<int:pk>/properties/', views.properties, name='properties'),


    path('properties', views.properties, name='properties'),
    url(r'^(?P<park_slug>[-\w]+)/$', views.properties, name='property_list_by_park'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.property_detail, name='property_detail'),

]
