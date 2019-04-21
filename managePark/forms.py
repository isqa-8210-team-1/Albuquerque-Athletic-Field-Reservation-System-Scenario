from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from parkAvail.models import Park, Prop


class ParkForm(forms.ModelForm):
    class Meta:
        model = Park
        fields = ('name', 'slug', 'park_attendant', 'attendant_email', 'park_address', 'city', 'state', 'zipcode',
                  'attendant_phone')


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Prop
        fields = ('park_under', 'slug', 'name', 'image', 'property_description', 'property_guest_capacity', 'location_in_park')
