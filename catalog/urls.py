from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    # For model Product
    # Create
    path("product/new/", views.ProductCreateView.as_view(), name="product_create"),
    # Read
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    # Update
    path(
        "product/<int:pk>/update/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    # Delete
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    # extra
    path("contacts/", views.ContactList.as_view(), name="contacts"),
    path("send_us/", views.send_us, name="send_us"),
]
