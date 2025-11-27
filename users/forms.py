from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordResetForm,
)
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


class UserResetPassForm(PasswordResetForm):
    class Meta:
        model = User
        fields = [
            "email",
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Указанный адрес электронной почты не был зарегистрирован ранее"
            )
        return email


class UserProfileView(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "country", "phone_number", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()
