from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.ContactList.as_view(), name="contacts"),
    path("send_us/", views.send_us, name="send_us"),
]
