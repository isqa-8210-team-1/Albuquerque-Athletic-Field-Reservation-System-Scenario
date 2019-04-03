from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.urls import reverse
from parkAvail.models import Prop, Park
from django.core.exceptions import ValidationError
from datetime import *


class Event(models.Model):
    prop_name = models.ForeignKey(Prop, related_name='prop_name', on_delete=models.CASCADE)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    Team_Name = models.CharField(u'Team Name', help_text=u'Team name', blank=True, null=True, max_length=255)
    Size_of_the_team = models.CharField(u'size of the team', help_text=u'Capacity', blank=True, null=True, max_length=3)
    Name_of_the_organization = models.CharField(u'Name of the Organization', help_text=u'Organization name', max_length=100,blank=True,null=True)

    TimeSlot = (
        ('M1', 'M1- 6.00 A.M to 8.00 A.M'),
        ('M2', 'M2- 8.15 A.M to 10.15 A.M'),
        ('M3', 'M3- 10.30 A.M to 12.30 P.M'),
        ('E1', 'E1- 3.00 P.M to 5.00 P.M'),
        ('E2', 'E2- 5.15 P.M to 7.15 P.M'),
    )

    timeslot = models.CharField(
        max_length=3,
        choices=TimeSlot,
        blank=True,
        default='m',
        help_text='Available Timeslot',
    )

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def __date__(self):
        return self.day

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.timeslot))

    @property
    def get_html_url(self):
        url = reverse('reservSystem:prop_event_edit', args=(self.id,))
        return f'<font color="red"><a href="{url}"> {self.timeslot} </a></font>'

    def check_overlap(self, fixed_timeslot, new_timeslot, new_prop, fixed_prop):
        overlap = False
        if new_timeslot == fixed_timeslot and new_prop == fixed_prop:  # edge case
            overlap = True
        return overlap

    def clean(self):
        #if self.day < date.today(): # checks for bookings done with previous dates
        #    raise ValidationError('Bookings cannot be done for previous dates')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.timeslot, self.timeslot, event.prop_name, self.prop_name):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.timeslot))
