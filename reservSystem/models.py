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
    #start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    # end_time = models.TimeField(u'Final time', help_text=u'Final time')

    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    TimeSlot = (
        ('M1', '6.00 A.M to 8.00 A.M'),
        ('M2', '8.15 A.M to 10.15 A.M'),
        ('M3', '10.30 A.M to 12.30 P.M'),
        ('E1', '3.00 P.M to 5.00 P.M'),
        ('E2', '5.15 P.M to 7.15 P.M'),

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


#    def get_absolute_url(self):
#           return reverse('parkAvail:prop_day',
#                           args=[self.id])

"""""    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (
                new_end >= fixed_start and new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap




    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
        if self.day < date.today():
            raise ValidationError('Bookings cannot be done for previous dates')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))

"""




