from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("contacts/", views.ContactList.as_view(), name="contacts"),
    path("send_us/", views.send_us, name="send_us"),
]
