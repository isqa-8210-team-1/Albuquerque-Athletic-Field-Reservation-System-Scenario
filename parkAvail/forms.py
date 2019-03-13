from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Park, Property


class ParkForm(forms.ModelForm):
    class Meta:
        model = Park
        fields = ('park_name', 'park_attendant', 'attendant_email', 'park_address', 'city', 'state', 'zipcode',
                  'attendant_phone')


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('park_name', 'property_name', 'property_description', 'property_guest_capacity', 'location_in_park')
