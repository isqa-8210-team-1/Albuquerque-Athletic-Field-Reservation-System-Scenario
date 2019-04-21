
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'reservSystem'

urlpatterns = [
    url(r'^calendar/$', views.CalendarView.as_view(), name='prop_calendar'),
    url(r'^new/$', views.prop_event, name='prop_event_new'),
    url(r'^edit/(?P<event_id>\d+)/$', views.prop_event, name='prop_event_edit'),
    #url(r'^confirmation/$', views.reservation, name='reservation'),
]
