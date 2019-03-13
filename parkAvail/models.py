from django.db import models
from django.utils import timezone
from django.urls import reverse


# Model for parks
class Park(models.Model):
    park_name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=200,db_index=True, unique=True)
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
    ordering = ('park_name',)
    verbose_name = 'park'
    verbose_name_plural = 'parks'


def __str__(self):
    return self.park_name


class Property(models.Model):
    park_name = models.ForeignKey(Park, on_delete=models.CASCADE, related_name='properties')
    property_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    property_description = models.TextField()
    property_guest_capacity = models.IntegerField()
    location_in_park = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


class MetaP:
    ordering = ('property_name',)


def __str__(self):
    return self.property_name


    #def __str__(self):
     #   return self.park_name
