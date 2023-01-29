from django import forms 
from .models import Shows, UserInfo
from django.contrib.auth.models import User


class ShowForm(forms.ModelForm):
    class Meta:
        model = Shows
        fields = "__all__"


class UserForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username', 'password', 'email']


class UserInfoForms(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ['profile_pic']