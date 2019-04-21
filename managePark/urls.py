
from django.urls import path, include
from . import views

urlpatterns = [
    path('park_list', views.park_list, name='park_list'),
    path('park_new', views.park_new, name='park_new'),
    path('property_new', views.property_new, name='property_new'),
    path('park/<int:pk>/edit/', views.park_edit, name='park_edit'),
    path('park/<int:pk>/delete/', views.park_delete, name='park_delete'),
    path('park/<int:pk>/property/', views.property, name='property'),
    path('<int:pp>/property/<int:pk>/edit/', views.property_edit, name='property_edit'),
    path('<int:pp>/property/<int:pk>/delete/', views.property_delete, name='property_delete'),
]
