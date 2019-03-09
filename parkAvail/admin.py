from django.contrib import admin
from .models import Park, Property


class ParkAdmin(admin.ModelAdmin):
    list_display = ['park_name', 'slug', 'park_attendant', 'attendant_email', 'park_address', 'city', 'state', 'zipcode', 'attendant_phone' ]
    prepopulated_fields = {'slug': ('park_name',)}
admin.site.register(Park, ParkAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['property_name', 'slug', 'property_description', 'property_guest_capacity','location_in_park']
    prepopulated_fields = {'slug': ('property_name',)}
admin.site.register(Property, PropertyAdmin)
