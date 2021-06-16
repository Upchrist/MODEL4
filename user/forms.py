from django import forms
from django.forms import ModelForm, fields
from django.forms import TextInput
from django.forms import widgets
from django.forms.widgets import FileInput, TextInput, EmailInput, FileInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='username')
    first_name = forms.CharField(max_length=50, help_text='first_name')
    last_name = forms.CharField(max_length=50, help_text='last_name')
    email = forms.CharField(max_length=50, help_text='email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


STATE = [
    ('Abia', 'Abia'),
    ('Akwa-Ibom', 'Akwa-Ibom'),
    ('Edo', 'Edo'),
    ('Imo', 'Imo'),
    ('lagos', 'lagos'),
    ('ogun', 'Ogun'),
    ('ondo', 'Ondon'),
    ('Rivers', 'Rivers'),

]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'address', 'city', 'state', 'country', 'image')
        widgets ={
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last_name'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email_Address'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'City'}),
            'state': Select(attrs={'class': 'input', 'placeholder': 'State'}, choices= STATE),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
            'image': FileInput(attrs={'placeholder': 'image'}),

        }