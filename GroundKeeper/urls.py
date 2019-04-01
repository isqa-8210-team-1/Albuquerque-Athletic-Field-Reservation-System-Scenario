from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'GroundKeeper'
urlpatterns = [

    path('FieldCondition_list/', views.FieldCondition_list, name='FieldCondition_list'),
    path('FieldCondition/<int:pk>/edit/', views.FieldCondition_edit, name='FieldCondition_edit'),
]
