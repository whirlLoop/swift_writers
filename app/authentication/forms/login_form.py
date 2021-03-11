from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.EmailInput(
        attrs={'autofocus': True, 'placeholder': 'Enter your email'}))
