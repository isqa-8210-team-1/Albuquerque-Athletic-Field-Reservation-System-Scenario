from django.contrib import admin

from .models import FieldCondition



# Register your models here.
class GroundsKeeperList(admin.ModelAdmin):
    list_display = ( 'reservation_number', 'park_name','property_name','Report_Time_Date', 'Property_Status_Description', 'Personnel_Time', 'Expenses', 'Status', 'comments')
    list_filter = ( 'reservation_number')
    search_fields = ('reservation_number', )
    ordering = ['reservation_number']

admin.site.register(FieldCondition)