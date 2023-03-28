from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from allauth.account.forms import SetPasswordForm
from django.shortcuts import render, redirect

class UserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
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
            'company',
            'per_company_number',
            'company_number'
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        pass


class MyCustomSetPasswordForm(SetPasswordForm):
    class Meta:
        pass


class UserCustomChangeForm(UserChangeForm):
  
    password=None

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'address',
            'phone_number', 
            'email', 
            'birth',
            'user_type',
            'company',
            'per_company_number',
            'company_number'
        ]

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        pass