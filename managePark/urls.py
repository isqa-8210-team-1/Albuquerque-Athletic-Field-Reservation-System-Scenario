
from django.urls import path, include
from . import views

urlpatterns = [
    path('park_list', views.park_list, name='park_list'),
    path('park_new', views.park_new, name='park_new'),
    path('property_new', views.property_new, name='property_new'),
    path('park/<int:pk>/edit/', views.park_edit, name='park_edit'),
    path('park/<int:pk>/delete/', views.park_delete, name='park_delete'),
    path('backend_dashboard', views.backend_dashboard, name='backend_dashboard'),

]
