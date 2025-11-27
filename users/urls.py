from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("reg/", views.UserRegView.as_view(), name="registration"),
    path(
        "profile",
        views.UserProfileView.as_view(),
        name="profile",
    ),
    path(
        "email_confirm/<str:token>/",
        views.email_confirm,
        name="email_confirm",
    ),
    path(
        "res_pas/",
        views.PasswordResetView.as_view(),
        name="reset_password",
    ),
]
