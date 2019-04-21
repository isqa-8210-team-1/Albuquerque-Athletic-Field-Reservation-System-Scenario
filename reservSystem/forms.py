from django import forms
from django.forms import DateInput
from .models import *


class ParkForm(forms.ModelForm):
    class Meta:
        model = Park
        fields = ('name', 'park_attendant', 'attendant_email', 'park_address', 'city', 'state', 'zipcode',
                  'attendant_phone')


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Prop
        fields = ('park_under', 'name', 'property_description', 'property_guest_capacity', 'location_in_park')


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('prop_name', 'day', 'timeslot', 'notes', 'Team_Name', 'Size_of_the_team', 'Name_of_the_organization')

        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'day': DateInput(attrs={'class': 'datepicker'}, format='%m/%d/%Y'),
        }
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        # self.fields['day'].input_formats = ('%m/%d/%Y',)
        self.fields['day'].input_formats = ['%Y-%m-%d']
