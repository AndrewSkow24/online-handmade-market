from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2",
        ]


class UserProfileView(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "country", "phone_number", "avatar")
