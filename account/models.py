from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.role=5
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100, verbose_name='First name', null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name='Last name', null=True, blank=True)
    organization = models.CharField(max_length=100, blank=True, verbose_name='Organization', null=True)
    #role = models.CharField(max_length=100, verbose_name='Role')
    ROLE_CHOICES = (
        (1, 'renter'),
        (2, 'proxyrenter'),
        (3, 'groundskeeper'),
        (4, 'employee'),
        (5, 'admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    street_address = models.CharField(max_length=200, verbose_name='Street address', null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name='City', null=True, blank=True)
    state = models.CharField(max_length=50, verbose_name='State', null=True, blank=True)
    zipcode = models.CharField(max_length=10, verbose_name='Zip code', null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        if self.is_admin:
            return self.is_admin
        elif self.role == 3 or self.role == 4:
            return True
        return False

# Add relationship to renter in this class
class Renter(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
