from django.db import models
from django.utils import timezone
from parkAvail.models import Prop, Park
from datetime import datetime


class FieldCondition(models.Model):
    reservation_number = models.CharField(max_length=50)

    park_name= models.ForeignKey(Park, verbose_name='park_name', default='1', on_delete=models.SET_DEFAULT)
    property_name = models.ForeignKey(Prop, verbose_name='property_name', default='1',on_delete=models.SET_DEFAULT)

    Report_Time_Date = models.DateTimeField(default=datetime.now(), help_text='Report Time&Date')

    Property_Status_Description = models.TextField(max_length=10)


    personnel_time = (
        ('1hr', '1hr- Good'),
        ('2hrs', '2hrs- Better'),
        ('5hrs', '5hrs- Awful'),
    )

    Personnel_Time = models.CharField(
        max_length=20,
        choices=personnel_time,
        blank=True,
        default='--',
        help_text='Personnel Time Spent',
    )

    expenses = (
        ('Good', '$2'),
        ('Better', '$10'),
        ('Awful', '$50'),
    )

    Expenses = models.CharField(
        max_length=20,
        choices=expenses,
        blank=True,
        default='--',
        help_text='Expenses',
    )

    status = (
        ('1','Pending'),
        ('2','Successful'),
    )

    Status = models.CharField(
        max_length=20,
        choices=status,
        blank=True,
        default='1',
        help_text='Payment status',
    )
    comments = models.TextField(max_length=200, default='', blank=True)

    def created(self):
        self.Report_Time_Date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural="Field Condition"

    def __str__(self):
        return self.reservation_number


