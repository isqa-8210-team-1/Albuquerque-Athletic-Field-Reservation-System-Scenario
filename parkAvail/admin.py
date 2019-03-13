from django.contrib import admin
from .models import Park, Property


class ParkList(admin.ModelAdmin):
    list_display = ['park_name', 'park_address', 'city', 'state',
                    'zipcode', 'park_attendant', 'attendant_email', 'attendant_phone']
    list_filter = ('park_name', 'zipcode', 'park_attendant')
    search_fields = ('park_name', 'zipcode', 'park_attendant')
    ordering = ['park_name']
    prepopulated_fields = {'slug': ('park_name',)}


admin.site.register(Park, ParkList)


class PropertyList(admin.ModelAdmin):
    list_display = ['park_name', 'property_name', 'slug', 'property_description', 'property_guest_capacity',
                    'location_in_park']
    prepopulated_fields = {'slug': ('property_name',)}


admin.site.register(Property, PropertyList)
