from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field import modelfields


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="аватар", null=True, blank=True
    )
    phone_number = modelfields.PhoneNumberField(
        verbose_name="Номер телефона", null=True, blank=True
    )
    # в дальнешем сделать выбором а не ручным вводом
    country = models.CharField(
        max_length=255, verbose_name="Cтрана", null=True, blank=True
    )
    token = models.CharField(
        max_length=255, verbose_name="Token", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
