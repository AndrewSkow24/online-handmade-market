from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


# Create
class PostCreateView(CreateView):
    model = Post
    fields = ("title", "body", "preview", "is_published")
    success_url = reverse_lazy("blog:post_list")


# Read
class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter_views += 1
        self.object.save()
        return self.object


# Update
class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "body", "preview", "is_published")
    success_url = reverse_lazy("blog:post_list")


# Delete
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
