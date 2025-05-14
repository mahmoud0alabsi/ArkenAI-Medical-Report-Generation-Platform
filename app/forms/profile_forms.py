from django import forms
from app.models.users.models import *

class EditProfileInfoForm(forms.ModelForm):
    
    first_name= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}),
        required=True, max_length=32, help_text='First name')

    last_name= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Last Name'}),
        required=True, max_length=32, help_text='Last name')

    institution_name= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Organization'}),
        required=True, max_length=32, help_text='Organization')


    class Meta:
        model = ProfileInfo
        fields = ('first_name', 'last_name', 'institution_name')
