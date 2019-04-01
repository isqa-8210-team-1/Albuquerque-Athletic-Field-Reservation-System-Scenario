
from django.db import models
from django.utils import timezone
from parkAvail.models import Prop, Park


class FieldCondition(models.Model):
    reservation_number = models.CharField(max_length=50)

    property_name = models.ForeignKey(Prop, related_name='properties', on_delete=models.CASCADE)
    # park_address=models.ForeignKey(Park, related_name='parkaddress', on_delete=models.CASCADE)
    # booked_date = models.ForeignKey(Prop, related_name='day', on_delete=models.CASCADE)

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
    )
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)

    comments = models.TextField(max_length=200,default='', blank=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.reservation_number)


