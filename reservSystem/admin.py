from __future__ import unicode_literals
from django.contrib import admin
from .models import Event
from parkAvail.admin import Prop


class EventAdmin(admin.ModelAdmin):
    list_display = ['prop_name', 'day', 'timeslot', 'notes', 'Team_Name', 'Size_of_the_team', 'Name_of_the_organization']


admin.site.register(Event, EventAdmin)




