from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'address',
            'phone_number', 
            'email', 
            'birth',
            'user_type',
        ]