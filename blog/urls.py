from django.urls import path

from . import views
from .views import PostDeleteView
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    # list
    path("", views.PostListView.as_view(), name="post_list"),
    #     С
    path("new/", views.PostCreateView.as_view(), name="post_create"),
    #     R
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    #     U
    path("<slug:slug>/update/", views.PostUpdateView.as_view(), name="post_update"),
    #     D
    path("<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
