from django import forms
from .models import FieldCondition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field



class FieldConditionForm(forms.ModelForm):
    field = FieldCondition
    class Meta:
        model = FieldCondition
        fields = ('reservation_number', 'Report_Time_Date', 'Property_Status_Description', 'Personnel_Time', 'Expenses', 'Status', 'comments')


