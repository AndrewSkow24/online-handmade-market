from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from pytils.translit import slugify


# Create
class PostCreateView(CreateView):
    model = Post
    fields = ("title", "body", "preview", "is_published")
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


# Read
class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True).order_by("-created_at")
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

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs.get("slug")])


# Delete
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
