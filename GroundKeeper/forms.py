from django import forms
from .models import FieldCondition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class FieldConditionForm(forms.ModelForm):
    field = FieldCondition
    class Meta:
        model = FieldCondition
        fields = ('reservation_number', 'property_name','timeslot', 'created_date', 'comments')
