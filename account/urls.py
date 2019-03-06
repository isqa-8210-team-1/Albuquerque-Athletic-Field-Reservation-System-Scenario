from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(
        #r'users/(?P<user_id>\w+)$',
        #views.UserProfileView.as_view(),
        #name='user_profile',
    #),
    #path('', views.HomePageView.as_view(), name='home'),
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('', views.HomePageView, name = 'home'),
    path('users/<int:pk>/',views.profile_view, name='profile_view'),
    path('users/<int:pk>/edit/',views.profile_edit, name='profile_edit'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.registerFullProfile, name='register'),
]