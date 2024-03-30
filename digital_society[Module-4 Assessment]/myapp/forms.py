from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = '__all__'

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'