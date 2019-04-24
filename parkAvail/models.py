from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Model for parks
class Park(models.Model):
    name = models.CharField(max_length=50, default='', db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default='')
    park_address = models.CharField(max_length=200,  null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    park_attendant = models.CharField(max_length=50, null=True, blank=True)
    attendant_email = models.EmailField(max_length=100, null=True, blank=True)
    attendant_phone = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    class Meta:
        ordering = ('name',)
        verbose_name = 'park'
        verbose_name_plural = 'parks'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('parkAvail:prop_list_by_park',
                           args=[self.slug])


class Prop(models.Model):
    park_under = models.ForeignKey(Park, related_name='props', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='https://afrteam.s3.amazonaws.com/static/props/%Y/%m/%d',
                              blank=True)
    property_description = models.TextField()
    property_guest_capacity = models.IntegerField()
    price = models.IntegerField( null=True)
    location_in_park = models.CharField(max_length=50, null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('parkAvail:prop_detail',
                           args=[self.id, self.slug])


