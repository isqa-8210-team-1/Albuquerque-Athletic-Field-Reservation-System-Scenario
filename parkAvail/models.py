from django.db import models
from django.utils import timezone


# Model for parks
class Park(models.Model):
    park_name = models.CharField(max_length=50)
    park_attendant = models.CharField(max_length=50)
    attendant_email = models.EmailField(max_length=100)
    park_address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    attendant_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.park_name)
