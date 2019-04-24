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

    re_path(r'^accounts/password_reset/$', auth_views.PasswordResetView.as_view(template_name='authentication/password_r_form.html',
                                                                                email_template_name = 'authentication/password_r_email.html',
                                                                                subject_template_name = 'authentication/password_reset_subject.txt'),
            name='password_reset'),
    re_path(r'^accounts/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_r_done.html'), name='password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_r_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_r_complete.html'), name='password_reset_complete'),

]