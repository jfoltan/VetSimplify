from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, label="Jméno")
    last_name = forms.CharField(max_length=50, required=True, label="Příjmení")
    username = forms.CharField(max_length=50, required=True, label="Uživatelské jméno")
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
