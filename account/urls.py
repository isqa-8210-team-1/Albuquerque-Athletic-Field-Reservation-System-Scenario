from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    #url(
        #r'users/(?P<user_id>\w+)$',
        #views.UserProfileView.as_view(),
        #name='user_profile',
    #),
    #path('', views.HomePageView.as_view(), name='home'),
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.HomePageView, name = 'home'),
    path('user/<int:pk>/',views.profile_view, name='profile_view'),
    path('user/<int:pk>/edit/',views.profile_edit, name='profile_edit'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.registerFullProfile, name='register'),
    path('contact/', views.contact, name='contact'),
    path('FAQ/', views.FAQ, name='FAQ'),
    # path('admin/', admin.site.urls),
    path('', include('GroundKeeper.urls')),
]