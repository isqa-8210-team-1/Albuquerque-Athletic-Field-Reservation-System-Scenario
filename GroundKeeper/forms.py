from django import forms
from .models import FieldCondition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class FieldConditionForm(forms.ModelForm):
    field = FieldCondition

    class Meta:
        model = FieldCondition
        fields = ('reservation_number', 'park_name', 'property_name','Report_Time_Date', 'Property_Status_Description', 'Personnel_Time', 'Expenses', 'Status', 'comments')


