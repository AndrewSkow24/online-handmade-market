from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from . import views


app_name = CatalogConfig.name

urlpatterns = [
    # For model Product
    # Create
    path("product/new/", views.ProductCreateView.as_view(), name="product_create"),
    # Read
    path("", views.ProductListView.as_view(), name="product_list"),
    path(
        "category/<int:category_pk>/",
        views.ProductListCategoryView.as_view(),
        name="products_by_category",
    ),
    path(
        "product/<int:pk>/",
        cache_page(30)(views.ProductDetailView.as_view()),
        name="product_detail",
    ),
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
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    # extra
    path("contacts/", views.ContactList.as_view(), name="contacts"),
    path("send_us/", views.send_us, name="send_us"),
]
