from __future__ import unicode_literals
from django.contrib import admin
from .models import Park, Prop, Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['prop_name', 'day', 'timeslot', 'notes']


admin.site.register(Event, EventAdmin)


