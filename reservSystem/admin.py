from __future__ import unicode_literals
from django.contrib import admin
from .models import Event
from parkAvail.admin import Prop
import csv
from django.http import HttpResponse
import datetime


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'park_name', 'prop_name', 'day', 'timeslot', 'notes', 'Team_Name', 'Size_of_the_team', 'Name_of_the_organization']
    actions = [export_to_csv]

admin.site.register(Event, EventAdmin)








