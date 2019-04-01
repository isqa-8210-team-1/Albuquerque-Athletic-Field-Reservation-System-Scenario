
from django.urls import path, include
from . import views

app_name = 'parkAvail'

urlpatterns = [
    path('', views.prop_list, name='prop_list'),
    path('<slug:park_slug>/', views.prop_list, name='prop_list_by_park'),
    path('<int:id>/<slug:slug>/', views.prop_detail, name='prop_detail'),
]
