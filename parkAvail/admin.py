from __future__ import unicode_literals
from django.contrib import admin
from .models import Park, Prop


class ParkList(admin.ModelAdmin):
    list_display = ['name', 'park_address', 'city', 'state',
                    'zipcode', 'park_attendant', 'attendant_email', 'attendant_phone']
    list_filter = ('name', 'zipcode', 'park_attendant')
    search_fields = ('name', 'zipcode', 'park_attendant')
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Park, ParkList)


class PropertyList(admin.ModelAdmin):
    list_display = ['park_under', 'name', 'slug', 'property_description', 'property_guest_capacity',
                    'location_in_park', 'price']
    list_filter = ['park_under', 'name', 'property_guest_capacity']
    # list_editable = ['park_under', 'property_description', 'property_guest_capacity']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Prop, PropertyList)


