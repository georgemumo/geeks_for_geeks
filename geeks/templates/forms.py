from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'email', '<PASSWORD1>', '<PASSWORD2>', 'phone_no', 'first_name', 'last_name')
