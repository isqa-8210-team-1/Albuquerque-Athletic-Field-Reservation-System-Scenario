from django import forms
from .models import MyUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationFullForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email','first_name', 'last_name', 'organization', 'street_address', 'city', 'state', 'zipcode', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class SignupForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email','password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UpdateProfileForm(forms.ModelForm):
    user = MyUser

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zipcode')

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(Field('email', type='hidden'))
        self.helper.layout = Layout(Field('password', type='hidden'))

class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Subject = forms.CharField(required=False)
    Message = forms.CharField(
    required=True,
    widget=forms.Textarea)