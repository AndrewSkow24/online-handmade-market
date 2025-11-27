import secrets
import string

from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, redirect

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, FormView
from .models import User
from .forms import UserRegForm, UserProfileView, UserResetPassForm
from django.contrib.auth.views import PasswordResetView
from django import forms

import random


class UserRegView(CreateView):
    model = User
    form_class = UserRegForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"
        send_mail(
            "Подтверждение почты",
            f"Ссылка для подтверждения регистрации: {url} .",
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


def email_confirm(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileView
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class PasswordResetView(FormView):
    """

    Восстановление пароля зарегистрированного пользователя на
    автоматически сгенерированный пароль. +


    Создайте новый контроллер для восстановления пароля.
    В интерфейсе кнопка «Восстановить пароль»
    должна отображаться на странице входа. +

    Пользователь вводит адрес электронной почты,
    в контроллере происходит генерация пароля,
    перезапись пароля для пользователя с
    соответсвующим адресом электронной почты
    и отправка сообщения с новым паролем на адрес почты.
    Пароль можно сгенерировать с помощью библиотеки
    random
    .

    Помните, что пароль в базе данных хранится в захешированном виде.
    Для установки пароля пользователю можно воспользоваться функцией
    make_password()
     (посмотреть в документации про эту функцию).
    """

    model = User
    form_class = UserResetPassForm
    # fields = [
    #     "email",
    # ]
    success_url = reverse_lazy("users:login")
    template_name = "users/reset_pass.html"

    def form_valid(self, form):
        # найти пользователя с такой почтой
        current_email = form.cleaned_data.get("email")

        current_user = get_object_or_404(User, email=current_email)
        if current_user():
            characters_for_pass = string.ascii_letters + string.digits
            new_password = ""

            for char in range(8):
                new_password += random.choice(characters_for_pass)

            hash_pass = make_password(new_password)

            current_user.password = hash_pass
            current_user.save()

            send_mail(
                "Ваш новый пароль",
                f"Новый пароль: {new_password} .",
                EMAIL_HOST_USER,
                [current_email],
            )
